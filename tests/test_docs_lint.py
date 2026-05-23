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


class DocsLintTests(unittest.TestCase):
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
                    "| Production engineering doc | `docs/engineering/` | Production standards. |",
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

    def test_minimal_valid_repo_passes(self):
        linter = load_linter()
        issues = linter.lint_repo(self.tmp)
        self.assertEqual([], issues)


if __name__ == "__main__":
    unittest.main()
