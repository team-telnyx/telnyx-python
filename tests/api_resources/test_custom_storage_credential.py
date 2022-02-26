from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


@pytest.mark.skip(reason="Not implemented yet")
class TestCustomStorageCredential(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.CustomStorageCredential.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/custom_storage_credentials/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CustomStorageCredential)

    def test_is_creatable(self, request_mock):
        resource = telnyx.CustomStorageCredential.create(
            backend="gcs", configuration=[]
        )
        request_mock.assert_requested("post", "/v2/custom_storage_credentials")
        assert isinstance(resource, telnyx.CustomStorageCredential)

    def test_is_modifiable(self, request_mock):
        resource = telnyx.CustomStorageCredential.modify(
            TEST_RESOURCE_ID,
            active=False,
            webhook_event_url="https://update.com",
            application_name="updated name",
        )
        request_mock.assert_requested(
            "patch", "/v2/custom_application/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FaxApplication)

    def test_is_deletable(self, request_mock):
        resource = telnyx.CustomStorageCredential.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/custom_storage_credentials/%s" % TEST_RESOURCE_ID
        )
