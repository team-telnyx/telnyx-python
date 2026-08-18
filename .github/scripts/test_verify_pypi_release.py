#!/usr/bin/env python3
# pyright: basic
import unittest

from verify_pypi_release import AvailabilityError, validate_release

VERSION = "4.175.0"


def file(kind: str, suffix: str):
    return {
        "packagetype": kind,
        "filename": "telnyx-%s%s" % (VERSION, suffix),
        "size": 10,
        "url": "https://files.pythonhosted.org/packages/telnyx-%s%s" % (VERSION, suffix),
        "digests": {"sha256": "a" * 64},
    }


class PyPIAvailabilityTests(unittest.TestCase):
    def payload(self):
        return {
            "info": {"version": VERSION},
            "urls": [file("bdist_wheel", "-py3-none-any.whl"), file("sdist", ".tar.gz")],
        }

    def test_accepts_exact_wheel_and_sdist(self):
        self.assertEqual(set(validate_release(self.payload(), VERSION)), {"bdist_wheel", "sdist"})

    def test_rejects_wrong_metadata_version(self):
        payload = self.payload()
        payload["info"]["version"] = "4.174.0"
        with self.assertRaisesRegex(AvailabilityError, "version"):
            validate_release(payload, VERSION)

    def test_rejects_missing_distribution_type(self):
        payload = self.payload()
        payload["urls"] = payload["urls"][:1]
        with self.assertRaisesRegex(AvailabilityError, "sdist"):
            validate_release(payload, VERSION)

    def test_rejects_invalid_digest_size_or_host(self):
        for field, value, message in (
            ("digests", {"sha256": "bad"}, "SHA-256"),
            ("size", 0, "size"),
            ("url", "https://example.com/file.whl", "untrusted"),
        ):
            with self.subTest(field=field):
                payload = self.payload()
                payload["urls"][0][field] = value
                with self.assertRaisesRegex(AvailabilityError, message):
                    validate_release(payload, VERSION)


if __name__ == "__main__":
    unittest.main()
