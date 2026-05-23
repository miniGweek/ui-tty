import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINTER_PATH = REPO_ROOT / "scripts" / "docs_lint.py"


def load_linter():
    spec = importlib.util.spec_from_file_location("docs_lint", LINTER_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class DocsLintPolicyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(self.tmp))
        self.write_minimal_repo()

    def write(self, path, text):
        target = self.tmp / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def write_minimal_repo(self):
        self.write(
            "docs/FILE-INDEX.md",
            "\n".join(
                [
                    "# File Index",
                    "",
                    "| Path | Purpose |",
                    "| --- | --- |",
                    "| `docs/outcomes/` | Outcome briefs. |",
                    "| `docs/plans/` | Delivery plans. |",
                    "| `docs/architecture/` | Architecture docs. |",
                    "| `docs/design/` | Design docs. |",
                    "| `docs/specs/` | Specs. |",
                    "| `docs/tasks/` | Task contracts. |",
                    "| `docs/verification/` | Verification records. |",
                    "| `docs/templates/` | Templates. |",
                    "| `docs/prompts/` | Governed prompts. |",
                    "| `docs/engineering/` | Engineering docs. |",
                    "| `scripts/` | Local automation scripts. |",
                    "| `tests/` | Test suite. |",
                    "",
                ]
            ),
        )
        self.write(
            "docs/FILE-MAP.md",
            "\n".join(
                [
                    "# File Map",
                    "",
                    "| Work Type | Location | Notes |",
                    "| --- | --- | --- |",
                    "| Outcome brief | `docs/outcomes/` | Start here. |",
                    "| Delivery plan | `docs/plans/` | Sequence work. |",
                    "| Architecture overview | `docs/architecture/` | System shape. |",
                    "| Design doc | `docs/design/` | Implementation approach. |",
                    "| Spec | `docs/specs/` | Behavior. |",
                    "| Task contract | `docs/tasks/` | Executable work. |",
                    "| Verification record | `docs/verification/` | Evidence. |",
                    "| Template | `docs/templates/` | Artifact formats. |",
                    "| Governed prompt | `docs/prompts/` | Planning prompts. |",
                    "| Production engineering doc | `docs/engineering/` | Standards. |",
                    "| Script | `scripts/` | Local automation. |",
                    "| Test | `tests/` | Tests. |",
                    "",
                ]
            ),
        )
        self.write(
            "docs/prompts/README.md",
            "# Prompts\n\n- `PRM-000-standing-guardrails.md`\n",
        )
        self.write("docs/prompts/PRM-000-standing-guardrails.md", "# Guardrails\n")
        for name in [
            "outcome-brief.md",
            "delivery-plan.md",
            "architecture-overview.md",
            "adr.md",
            "design.md",
            "spec.md",
            "task-contract.md",
            "verification-record.md",
            "production-readiness-checklist.md",
            "variant-profile.md",
        ]:
            self.write(f"docs/templates/{name}", f"# {name}\n\n## Prompt Trace\n")
        self.write("docs/outcomes/O-001-example.md", "# Example\n\n## Prompt Trace\n")
        self.write("docs/outcomes/README.md", "# Outcome Briefs\n")

    def issue_text(self, issues):
        return "\n".join(str(issue) for issue in issues)

    def test_allows_root_and_prompt_inline_markdown_paths(self):
        self.write("AGENTS.md", "# Agents\n")
        self.write(
            "docs/engineering/links.md",
            "# Links\n\nUse `AGENTS.md` and `PRM-000-standing-guardrails.md`.\n\n## Prompt Trace\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertNotIn("broken Markdown path", self.issue_text(issues))

    def test_allows_placeholder_inline_markdown_paths(self):
        self.write(
            "docs/engineering/placeholders.md",
            "# Placeholders\n\nUse `docs/outcomes/O-001-short-name.md` and `PRM-###-short-name.md`.\n\n## Prompt Trace\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertNotIn("broken Markdown path", self.issue_text(issues))

    def test_allows_plan_references_to_future_markdown_paths(self):
        self.write(
            "docs/plans/P-002-future.md",
            "# Plan\n\nFuture output: `docs/engineering/future.md`.\n\n## Prompt Trace\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertNotIn("broken Markdown path", self.issue_text(issues))

    def test_rejects_non_ascii_markdown(self):
        self.write(
            "docs/outcomes/O-002-non-ascii.md",
            "# Non ASCII\n\n## Prompt Trace\n\n" + chr(0x201C) + "quoted text\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn("non-ASCII character", self.issue_text(issues))

    def test_rejects_broken_local_markdown_link(self):
        self.write(
            "docs/outcomes/O-002-link.md",
            "# Link\n\nSee [missing](../missing.md).\n\n## Prompt Trace\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn("broken local link ../missing.md", self.issue_text(issues))

    def test_rejects_broken_inline_markdown_path(self):
        self.write(
            "docs/engineering/checks.md",
            "# Checks\n\nUse `docs/prompts/README2.md`.\n\n## Prompt Trace\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn(
            "broken Markdown path docs/prompts/README2.md",
            self.issue_text(issues),
        )

    def test_rejects_prompt_missing_from_readme(self):
        self.write("docs/prompts/PRM-010-stage-0-intake-task-contract.md", "# Intake\n")
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn(
            "prompt not listed in docs/prompts/README.md",
            self.issue_text(issues),
        )

    def test_rejects_readme_prompt_entry_without_file(self):
        self.write(
            "docs/prompts/README.md",
            "# Prompts\n\n- `PRM-000-standing-guardrails.md`\n- `PRM-999-missing.md`\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn("listed prompt file does not exist", self.issue_text(issues))

    def test_rejects_template_without_prompt_trace(self):
        self.write("docs/templates/spec.md", "# Spec\n")
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn(
            "docs/templates/spec.md: missing ## Prompt Trace",
            self.issue_text(issues),
        )

    def test_rejects_governed_artifact_without_prompt_trace(self):
        self.write("docs/design/D-001-example.md", "# Design\n")
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn(
            "docs/design/D-001-example.md: missing ## Prompt Trace",
            self.issue_text(issues),
        )

    def test_allows_readme_without_prompt_trace(self):
        self.write("docs/design/README.md", "# Design Docs\n")
        issues = load_linter().lint_repo(self.tmp)
        self.assertNotIn("docs/design/README.md", self.issue_text(issues))

    def test_rejects_banned_wording(self):
        self.write(
            "docs/outcomes/O-002-language.md",
            "# Language\n\n## Prompt Trace\n\nThis is table stakes.\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn("banned wording 'table stakes'", self.issue_text(issues))

    def test_rejects_missing_file_index_entry(self):
        self.write(
            "docs/FILE-INDEX.md",
            "# File Index\n\n| Path | Purpose |\n| --- | --- |\n",
        )
        issues = load_linter().lint_repo(self.tmp)
        self.assertIn("missing important path docs/prompts/", self.issue_text(issues))

    def test_cli_returns_nonzero_on_failure(self):
        self.write("docs/design/D-001-example.md", "# Design\n")
        result = subprocess.run(
            [sys.executable, str(LINTER_PATH), str(self.tmp)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertIn(
            "docs/design/D-001-example.md: missing ## Prompt Trace",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
