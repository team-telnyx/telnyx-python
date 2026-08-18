#!/usr/bin/env python3
"""Static safety contracts for the DOT-2061 Python rollout."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class ReleasePRGateWorkflowTests(unittest.TestCase):
    def test_release_please_pr_runs_every_full_ci_job(self):
        ci = (ROOT / ".github/workflows/ci.yml").read_text()
        predicate = "startsWith(github.head_ref, 'release-please--')"
        self.assertEqual(ci.count(predicate), 3)
        for name in ("name: lint", "name: build", "name: test"):
            self.assertIn(name, ci)
        self.assertIn("python3 .github/scripts/test_release_pr_auto_merge.py -v", ci)
        self.assertIn("python3 .github/scripts/test_release_pr_ci_gate.py -v", ci)

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
