from __future__ import absolute_import, division, print_function

import telnyx


TEST_RESOURCE_ID = "123"


class TestMessagingProfile(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.MessagingProfile.list()
        request_mock.assert_requested("get", "/v2/messaging_profiles")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingProfile)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.MessagingProfile.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingProfile)

    def test_is_creatable(self, request_mock):
        resource = telnyx.MessagingProfile.create(country="US", type="custom")
        request_mock.assert_requested("post", "/v2/messaging_profiles")
        assert isinstance(resource, telnyx.MessagingProfile)

    def test_is_saveable(self, request_mock):
        messaging_profile = telnyx.MessagingProfile.retrieve(TEST_RESOURCE_ID)
        messaging_profile.name = "value"
        resource = messaging_profile.save()
        request_mock.assert_requested(
            "patch", "/v2/messaging_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingProfile)
        assert resource is messaging_profile

    def test_is_modifiable(self, request_mock):
        resource = telnyx.MessagingProfile.modify(TEST_RESOURCE_ID, name="Test")
        request_mock.assert_requested(
            "patch", "/v2/messaging_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingProfile)

    def test_is_deletable(self, request_mock):
        resource = telnyx.MessagingProfile.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/messaging_profiles/%s" % TEST_RESOURCE_ID
        )

    def test_can_call_messaging_phone_numbers(self, request_mock):
        resources = telnyx.MessagingProfile.list_phone_numbers(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_profiles/%s/phone_numbers" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingPhoneNumber)

    def test_can_call_phone_numbers(self, request_mock):
        messaging_profile = telnyx.MessagingProfile.retrieve(TEST_RESOURCE_ID)
        resources = messaging_profile.phone_numbers()
        request_mock.assert_requested(
            "get", "/v2/messaging_profiles/%s/phone_numbers" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingPhoneNumber)

    def test_can_call_messaging_short_codes(self, request_mock):
        resources = telnyx.MessagingProfile.list_short_codes(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_profiles/%s/short_codes" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.ShortCode)

    def test_can_call_short_codes(self, request_mock):
        messaging_profile = telnyx.MessagingProfile.retrieve(TEST_RESOURCE_ID)
        resources = messaging_profile.short_codes()
        request_mock.assert_requested(
            "get", "/v2/messaging_profiles/%s/short_codes" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.ShortCode)

    def test_can_call_messaging_alphanumeric_sender_ids(self, request_mock):
        resources = telnyx.MessagingProfile.list_alphanumeric_sender_ids(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "get",
            "/v2/messaging_profiles/%s/alphanumeric_sender_ids" % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.AlphanumericSenderId)

    def test_can_call_alphanumeric_sender_ids(self, request_mock):
        messaging_profile = telnyx.MessagingProfile.retrieve(TEST_RESOURCE_ID)
        resources = messaging_profile.alphanumeric_sender_ids()
        request_mock.assert_requested(
            "get",
            "/v2/messaging_profiles/%s/alphanumeric_sender_ids" % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.AlphanumericSenderId)
