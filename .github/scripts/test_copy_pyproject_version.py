from __future__ import annotations

import tempfile
import unittest
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).with_name("copy_pyproject_version.py")
WORKFLOW = SCRIPT.parents[1] / "workflows" / "release-please.yml"


def pyproject(*, version: str = "1.2.3", dependency: str = "pynacl >= 1.5, < 2", name: str = "telnyx") -> str:
    return f'''[build-system]
requires = ["hatchling"]

[project]
name = "{name}"
version = "{version}"
dependencies = ["httpx"]

[project.optional-dependencies]
webhooks = ["{dependency}"]
'''


class CopyPyprojectVersionTests(unittest.TestCase):
    def run_script(self, source: Path, target: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(SCRIPT), str(source), str(target)],
            text=True,
            capture_output=True,
        )

    def test_copies_only_project_version_and_preserves_next_dependencies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "release.toml"
            target = root / "next.toml"
            source.write_text(pyproject(version="4.178.0", dependency="standardwebhooks >= 1, < 2"))
            target.write_text(pyproject(version="4.164.0", dependency="pynacl >= 1.5, < 2"))

            result = self.run_script(source, target)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('version = "4.178.0"', target.read_text())
            self.assertIn('webhooks = ["pynacl >= 1.5, < 2"]', target.read_text())
            self.assertNotIn("standardwebhooks", target.read_text())

    def test_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "release.toml"
            target = root / "next.toml"
            source.write_text(pyproject(version="4.178.0"))
            target.write_text(pyproject(version="4.164.0"))

            first = self.run_script(source, target)
            after_first = target.read_text()
            second = self.run_script(source, target)

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(target.read_text(), after_first)

    def test_fails_closed_for_wrong_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "release.toml"
            target = root / "next.toml"
            source.write_text(pyproject(name="not-telnyx"))
            target.write_text(pyproject())
            original = target.read_text()

            result = self.run_script(source, target)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("project.name must be 'telnyx'", result.stderr)
            self.assertEqual(target.read_text(), original)

    def test_fails_closed_for_non_semver_source_version(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "release.toml"
            target = root / "next.toml"
            source.write_text(pyproject(version="latest"))
            target.write_text(pyproject())
            original = target.read_text()

            result = self.run_script(source, target)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("valid semantic version", result.stderr)
            self.assertEqual(target.read_text(), original)

    def test_fails_closed_when_project_version_assignment_is_ambiguous(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "release.toml"
            target = root / "next.toml"
            source.write_text(pyproject())
            target.write_text(pyproject().replace('version = "1.2.3"', 'version = "1.2.3"\nversion = "1.2.4"'))
            original = target.read_text()

            result = self.run_script(source, target)

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_text(), original)

    def test_release_workflow_overlays_version_without_restoring_whole_pyproject(self) -> None:
        workflow = WORKFLOW.read_text()

        self.assertIn(
            'RELEASE_FILES=("CHANGELOG.md" "src/telnyx/_version.py" ".release-please-manifest.json")',
            workflow,
        )
        self.assertIn(
            "for f in CHANGELOG.md src/telnyx/_version.py .release-please-manifest.json; do",
            workflow,
        )
        self.assertEqual(workflow.count("python3 .github/scripts/copy_pyproject_version.py"), 2)
        self.assertNotIn(
            "for f in CHANGELOG.md pyproject.toml src/telnyx/_version.py",
            workflow,
        )


if __name__ == "__main__":
    unittest.main()
