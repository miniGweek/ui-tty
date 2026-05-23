#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


@dataclass(frozen=True)
class Issue:
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


IGNORED_PARTS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "dist",
    "build",
    ".venv",
    "venv",
}

GOVERNED_DIRECTORIES = [
    "docs/outcomes/",
    "docs/plans/",
    "docs/architecture/",
    "docs/design/",
    "docs/specs/",
    "docs/tasks/",
    "docs/verification/",
    "docs/engineering/",
]

GOVERNED_TEMPLATES = [
    "docs/templates/outcome-brief.md",
    "docs/templates/delivery-plan.md",
    "docs/templates/architecture-overview.md",
    "docs/templates/adr.md",
    "docs/templates/design.md",
    "docs/templates/spec.md",
    "docs/templates/task-contract.md",
    "docs/templates/verification-record.md",
    "docs/templates/production-readiness-checklist.md",
    "docs/templates/variant-profile.md",
]

INDEXED_PATHS = [
    "docs/outcomes/",
    "docs/plans/",
    "docs/architecture/",
    "docs/design/",
    "docs/specs/",
    "docs/tasks/",
    "docs/verification/",
    "docs/templates/",
    "docs/prompts/",
    "docs/engineering/",
    "scripts/",
    "tests/",
]

BANNED_WORDING = [
    "out-of-distribution",
    "left-shifted",
    "context bleed",
    "folklore",
    "smuggled",
    "busywork",
    "we just",
    "backstop",
    "moat",
    "table stakes",
    "happy to",
    "AI-for-AI",
    "BigArchPrompt",
    "congnitive",
    "architecutre",
    "convenitonal",
]

LOCAL_LINK_PATTERN = re.compile(r"(?<!!\[)\[[^\]]+\]\(([^)]+)\)")
INLINE_MARKDOWN_PATH_PATTERN = re.compile(r"`([^`]+\.md(?:#[^`]*)?)`")
PROMPT_FILE_PATTERN = re.compile(r"PRM-\d{3}[-A-Za-z0-9]+\.md")


def rel_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if IGNORED_PARTS.intersection(path.relative_to(root).parts):
            continue
        yield path


def has_prompt_trace(path: Path) -> bool:
    return "## Prompt Trace" in read_text(path)


def lint_repo(root: Path) -> list[Issue]:
    root = root.resolve()
    issues: list[Issue] = []
    issues.extend(check_ascii(root))
    issues.extend(check_markdown_links(root))
    issues.extend(check_inline_markdown_paths(root))
    issues.extend(check_prompt_inventory(root))
    issues.extend(check_prompt_trace(root))
    issues.extend(check_index_and_map(root))
    issues.extend(check_banned_wording(root))
    return issues


def check_ascii(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files(root):
        text = read_text(path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            if any(ord(char) > 127 for char in line):
                issues.append(
                    Issue(
                        rel_path(path, root),
                        f"line {line_number}: non-ASCII character",
                    )
                )
                break
    return issues


def check_markdown_links(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files(root):
        text = read_text(path)
        for match in LOCAL_LINK_PATTERN.finditer(text):
            target = normalize_link_target(match.group(1))
            if should_skip_link(target):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                issues.append(
                    Issue(
                        rel_path(path, root),
                        f"broken local link {target}",
                    )
                )
    return issues



def check_inline_markdown_paths(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files(root):
        relative_path = rel_path(path, root)
        if relative_path.startswith("docs/plans/"):
            continue
        text = read_text(path)
        for match in INLINE_MARKDOWN_PATH_PATTERN.finditer(text):
            target = normalize_link_target(match.group(1))
            if should_skip_markdown_path_reference(target):
                continue
            candidates = resolve_markdown_path_references(path, root, target)
            if not any(candidate.exists() for candidate in candidates):
                issues.append(
                    Issue(
                        relative_path,
                        f"broken Markdown path {target}",
                    )
                )
    return issues


def should_skip_markdown_path_reference(target: str) -> bool:
    return (
        "*" in target
        or "###" in target
        or "short-name" in target
        or should_skip_link(target)
    )


def resolve_markdown_path_references(path: Path, root: Path, target: str) -> list[Path]:
    target_file = target.split("#", 1)[0]
    if target_file.startswith(("docs/", "scripts/", "tests/")):
        return [(root / target_file).resolve()]
    if target_file.startswith("PRM-"):
        return [(root / "docs/prompts" / target_file).resolve()]
    return [
        (path.parent / target_file).resolve(),
        (root / target_file).resolve(),
    ]


def normalize_link_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target)


def should_skip_link(target: str) -> bool:
    lower = target.lower()
    return (
        not target
        or target.startswith("#")
        or lower.startswith("http://")
        or lower.startswith("https://")
        or lower.startswith("mailto:")
    )


def check_prompt_inventory(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    prompt_dir = root / "docs/prompts"
    readme = prompt_dir / "README.md"
    if not prompt_dir.exists() or not readme.exists():
        return issues

    readme_text = read_text(readme)
    listed_prompts = set(PROMPT_FILE_PATTERN.findall(readme_text))
    actual_prompts = {path.name for path in prompt_dir.glob("PRM-*.md")}

    for prompt in sorted(actual_prompts - listed_prompts):
        issues.append(
            Issue(
                f"docs/prompts/{prompt}",
                "prompt not listed in docs/prompts/README.md",
            )
        )
    for prompt in sorted(listed_prompts - actual_prompts):
        issues.append(
            Issue(
                "docs/prompts/README.md",
                f"listed prompt file does not exist: {prompt}",
            )
        )
    return issues


def check_prompt_trace(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for rel in GOVERNED_TEMPLATES:
        path = root / rel
        if path.exists() and not has_prompt_trace(path):
            issues.append(Issue(rel, "missing ## Prompt Trace"))

    for directory in GOVERNED_DIRECTORIES:
        base = root / directory
        if not base.exists():
            continue
        for path in sorted(base.glob("*.md")):
            if path.name == "README.md":
                continue
            rel = path.relative_to(root).as_posix()
            if not has_prompt_trace(path):
                issues.append(Issue(rel, "missing ## Prompt Trace"))
    return issues


def check_index_and_map(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    index = root / "docs/FILE-INDEX.md"
    file_map = root / "docs/FILE-MAP.md"
    index_text = read_text(index) if index.exists() else ""
    map_text = read_text(file_map) if file_map.exists() else ""
    for rel in INDEXED_PATHS:
        if (root / rel).exists() and rel not in index_text:
            issues.append(Issue("docs/FILE-INDEX.md", f"missing important path {rel}"))
        if (root / rel).exists() and rel not in map_text:
            issues.append(Issue("docs/FILE-MAP.md", f"missing important path {rel}"))
    return issues


def check_banned_wording(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    patterns = [(word, re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)) for word in BANNED_WORDING]
    for path in markdown_files(root):
        text = read_text(path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            if "docs-lint: allow banned wording" in line:
                continue
            for word, pattern in patterns:
                if pattern.search(line):
                    issues.append(
                        Issue(
                            rel_path(path, root),
                            f"line {line_number}: banned wording {word!r}",
                        )
                    )
    return issues


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    root = Path(args[0]) if args else Path.cwd()
    issues = lint_repo(root)
    if issues:
        for issue in issues:
            print(issue)
        print(f"{len(issues)} issue(s) found")
        return 1
    print("docs lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
