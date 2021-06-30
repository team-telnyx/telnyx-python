from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestTelephonyCredential(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.TelephonyCredential.list()
        request_mock.assert_requested("get", "/v2/telephony_credentials")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.TelephonyCredential)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.TelephonyCredential.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/telephony_credentials/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.TelephonyCredential)

    def test_is_creatable(self, request_mock):
        resource = telnyx.TelephonyCredential.create(
            connection_id="some-connection-id",
        )
        request_mock.assert_requested("post", "/v2/telephony_credentials")
        assert isinstance(resource, telnyx.TelephonyCredential)

    def test_is_saveable(self, request_mock):
        telephony_credential = telnyx.TelephonyCredential.retrieve(TEST_RESOURCE_ID)
        telephony_credential.tag = "some_tag"
        resource = telephony_credential.save()
        request_mock.assert_requested(
            "patch", "/v2/telephony_credentials/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.TelephonyCredential)
        assert resource is telephony_credential

    def test_is_modifiable(self, request_mock):
        resource = telnyx.TelephonyCredential.modify(TEST_RESOURCE_ID, tag="some_tag")
        request_mock.assert_requested(
            "patch", "/v2/telephony_credentials/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.TelephonyCredential)

    def test_is_deletable(self, request_mock):
        resource = telnyx.TelephonyCredential.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/telephony_credentials/%s" % TEST_RESOURCE_ID
        )
