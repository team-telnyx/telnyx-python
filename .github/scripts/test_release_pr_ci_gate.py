#!/usr/bin/env python3
"""Static safety contracts for the DOT-2061 Python rollout."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class ReleasePRGateWorkflowTests(unittest.TestCase):
    def test_classifier_owns_every_full_ci_job(self):
        ci = (ROOT / ".github/workflows/ci.yml").read_text()
        self.assertIn("name: classify production CI", ci)
        self.assertIn("classify_production_ci.py --event-path", ci)
        self.assertEqual(ci.count("needs: classify-production-ci"), 3)
        self.assertEqual(
            ci.count("if: needs.classify-production-ci.outputs.run_full == 'true'"), 3
        )
        for name in ("name: lint", "name: build", "name: test"):
            self.assertIn(name, ci)
        self.assertIn("python3 .github/scripts/test_release_pr_auto_merge.py -v", ci)
        self.assertIn("python3 .github/scripts/test_release_pr_ci_gate.py -v", ci)
        self.assertIn("python3 .github/scripts/test_classify_production_ci.py -v", ci)
        self.assertIn("python3 .github/scripts/test_validate_next_provenance.py -v", ci)
        self.assertIn("python3 .github/scripts/test_verify_pypi_release.py -v", ci)

    def test_publish_verifies_exact_pypi_version_after_publish(self):
        workflow = (ROOT / ".github/workflows/publish-pypi.yml").read_text()
        self.assertIn("name: verify PyPI availability", workflow)
        self.assertIn("needs: publish", workflow)
        self.assertIn("verify_pypi_release.py", workflow)
        self.assertIn("--version \"$VERSION\"", workflow)

    def test_next_readiness_is_lightweight_and_fail_closed(self):
        workflow = (ROOT / ".github/workflows/next-readiness.yml").read_text()
        self.assertIn("branches: [next]", workflow)
        self.assertIn("name: next-readiness", workflow)
        self.assertIn("validate_next_provenance.py", workflow)
        self.assertIn("--expected-next", workflow)
        self.assertIn("MERGE_TOKEN: ${{ secrets.SDK_WRITE_TOKEN }}", workflow)
        self.assertIn("persist-credentials: false", workflow)
        self.assertNotIn("scripts/bootstrap", workflow)
        self.assertNotIn("scripts/test", workflow)
        self.assertNotIn("scripts/lint", workflow)

    def test_readiness_uses_trusted_policy_and_never_merges(self):
        workflow = (ROOT / ".github/workflows/release-pr-readiness.yml").read_text()
        self.assertIn("pull_request_target:", workflow)
        self.assertIn("ref: ${{ github.event.repository.default_branch || 'main' }}", workflow)
        self.assertIn("persist-credentials: false", workflow)
        self.assertIn("--expected-head", workflow)
        self.assertIn("--dry-run", workflow)
        self.assertNotIn("--merge", workflow)
        self.assertNotIn("github.event.pull_request.head.sha }}\n          fetch-depth", workflow)

    def test_readiness_publishes_exact_head_status_fail_closed(self):
        workflow = (ROOT / ".github/workflows/release-pr-readiness.yml").read_text()
        self.assertIn("context=release-provenance", workflow)
        self.assertIn("state=pending", workflow)
        self.assertIn("STATE=failure", workflow)
        self.assertIn("[ \"$STATE\" = success ]", workflow)
        self.assertIn("statuses: write", workflow)

    def test_auto_merge_workflow_remains_separate(self):
        readiness = (ROOT / ".github/workflows/release-pr-readiness.yml").read_text()
        self.assertNotIn("release-pr-auto-merge.yml", readiness)
        self.assertNotIn("merge normally", readiness)


if __name__ == "__main__":
    unittest.main()
