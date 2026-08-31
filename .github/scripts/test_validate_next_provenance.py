#!/usr/bin/env python3
# pyright: basic
import unittest

from release_pr_auto_merge import GateError
from validate_next_provenance import (
    PRODUCTION_POLICY_PATHS,
    api_tree,
    changed_paths,
    require_policy_parity,
    require_only_allowed_changes,
)

A = ("100644", "blob", "a" * 40)
B = ("100644", "blob", "b" * 40)


class PythonNextProvenanceTests(unittest.TestCase):
    def test_release_version_overlay_helpers_are_production_policy(self):
        self.assertTrue(
            {
                ".github/scripts/copy_pyproject_version.py",
                ".github/scripts/test_copy_pyproject_version.py",
            }.issubset(PRODUCTION_POLICY_PATHS)
        )

    def test_generated_tree_change_is_rejected(self):
        with self.assertRaisesRegex(GateError, "src/generated.go"):
            require_only_allowed_changes(
                {"src/generated.go": A},
                {"src/generated.go": B},
                {".github/workflows/ci.yml"},
                "promotion",
            )

    def test_only_enumerated_production_transform_is_allowed(self):
        require_only_allowed_changes(
            {"src/generated.go": A, "go.mod": A},
            {"src/generated.go": A, "go.mod": B},
            {"go.mod"},
            "promotion",
        )

    def test_add_delete_and_modify_are_all_detected(self):
        self.assertEqual(
            changed_paths({"same": A, "deleted": A, "changed": A}, {"same": A, "added": B, "changed": B}),
            {"deleted", "added", "changed"},
        )

    def test_policy_must_exist_and_match_default_exactly(self):
        with self.assertRaisesRegex(GateError, "ci.yml"):
            require_policy_parity(
                {".github/workflows/ci.yml": A},
                {},
                {".github/workflows/ci.yml"},
            )
        with self.assertRaisesRegex(GateError, "ci.yml"):
            require_policy_parity({}, {}, {".github/workflows/ci.yml"})
        require_policy_parity(
            {path: A for path in PRODUCTION_POLICY_PATHS},
            {path: A for path in PRODUCTION_POLICY_PATHS},
            PRODUCTION_POLICY_PATHS,
        )

    def test_truncated_or_malformed_api_tree_fails_closed(self):
        with self.assertRaisesRegex(GateError, "truncated"):
            api_tree({"truncated": True, "tree": []})
        with self.assertRaisesRegex(GateError, "invalid staging tree entry"):
            api_tree({"truncated": False, "tree": [{"path": "x"}]})

    def test_api_tree_keeps_only_blob_identity(self):
        payload = {
            "truncated": False,
            "tree": [
                {"path": "x", "mode": "100644", "type": "blob", "sha": "a" * 40},
                {"path": "dir", "mode": "040000", "type": "tree", "sha": "b" * 40},
            ],
        }
        self.assertEqual(api_tree(payload), {"x": A})


if __name__ == "__main__":
    unittest.main()
