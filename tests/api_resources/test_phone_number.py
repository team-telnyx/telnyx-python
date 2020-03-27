from __future__ import absolute_import, division, print_function

import pytest

import telnyx
from telnyx import error

TEST_RESOURCE_ID = "1293384261075731499"


class TestPhoneNumber(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.PhoneNumber.list()
        request_mock.assert_requested("get", "/v2/phone_numbers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.PhoneNumber)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/phone_numbers/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.PhoneNumber)

    def test_is_saveable(self, request_mock):
        phone_number = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        phone_number.tags = ["foo", "bar"]
        resource = phone_number.save()
        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PhoneNumber)
        assert resource is phone_number

    def test_is_modifiable(self, request_mock):
        resource = telnyx.PhoneNumber.modify(TEST_RESOURCE_ID, tags=["foo", "bar"])
        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PhoneNumber)

    def test_is_deletable(self, request_mock):
        resource = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/phone_numbers/%s" % TEST_RESOURCE_ID
        )

    def test_voice_instance_is_retrievable(self, request_mock):
        phone_number = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource = phone_number.voice()

        request_mock.assert_requested(
            "get", "/v2/phone_numbers/%s/voice" % TEST_RESOURCE_ID
        )

        assert isinstance(resource, telnyx.VoiceSettings)

    def test_voice_is_listable(self, request_mock):
        resources = telnyx.PhoneNumber.all_voice()

        request_mock.assert_requested("get", "/v2/phone_numbers/voice")

        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.VoiceSettings)

    def test_voice_instance_is_saveable(self, request_mock):
        phone_number = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource = phone_number.voice()
        resource.call_forwarding = {}
        resource.save()

        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/voice" % TEST_RESOURCE_ID
        )

    def test_voice_is_saveable(self, request_mock):
        resource = telnyx.PhoneNumber.all_voice().data[0]
        resource.call_forwarding = {}
        resource.save()

        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/voice" % resource.id
        )

    def test_enable_emergency(self, request_mock):
        resource = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource = resource.enable_emergency(
            emergency_enabled=True, emergency_address_id="123"
        )
        request_mock.assert_requested(
            "post", "/v2/phone_numbers/%s/actions/enable_emergency" % TEST_RESOURCE_ID
        )

    def test_messaging_instance_is_retrievable(self, request_mock):
        phone_number = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource = phone_number.messaging()

        request_mock.assert_requested(
            "get", "/v2/phone_numbers/%s/messaging" % TEST_RESOURCE_ID
        )

        assert isinstance(resource, telnyx.MessagingSettings)

    def test_messaging_is_listable(self, request_mock):
        resources = telnyx.PhoneNumber.all_messaging()

        request_mock.assert_requested("get", "/v2/phone_numbers/messaging")

        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingSettings)

    def test_messaging_instance_is_saveable(self, request_mock):
        phone_number = telnyx.PhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource = phone_number.messaging()
        resource.call_forwarding = {}
        resource.save()

        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/messaging" % TEST_RESOURCE_ID
        )

    def test_messaging_is_saveable(self, request_mock):
        resource = telnyx.PhoneNumber.all_messaging().data[0]
        resource.call_forwarding = {}
        resource.save()

        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/messaging" % resource.id
        )


class TestVoiceSettings(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.VoiceSettings.list()
        request_mock.assert_requested("get", "/v2/phone_numbers/voice")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.VoiceSettings)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.VoiceSettings.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/phone_numbers/%s/voice" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.VoiceSettings)

    def test_is_saveable(self, request_mock):
        voice_settings = telnyx.VoiceSettings.retrieve(TEST_RESOURCE_ID)
        voice_settings.tech_prefix_enabled = True
        resource = voice_settings.save()
        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/voice" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.VoiceSettings)
        assert resource is voice_settings

    def test_is_modifiable(self, request_mock):
        resource = telnyx.VoiceSettings.modify(
            TEST_RESOURCE_ID, tech_prefix_enabled=True
        )
        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/voice" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.VoiceSettings)

    def test_instance_url_invalid(self):
        with pytest.raises(error.InvalidRequestError):
            telnyx.VoiceSettings(id=1).instance_url()


class TestMessagingSettings(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.MessagingSettings.list()
        request_mock.assert_requested("get", "/v2/phone_numbers/messaging")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingSettings)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.MessagingSettings.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/phone_numbers/%s/messaging" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingSettings)

    def test_is_saveable(self, request_mock):
        messaging_settings = telnyx.MessagingSettings.retrieve(TEST_RESOURCE_ID)
        messaging_settings.messaging_profile_id = "123"
        resource = messaging_settings.save()
        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/messaging" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingSettings)
        assert resource is messaging_settings

    def test_is_modifiable(self, request_mock):
        resource = telnyx.MessagingSettings.modify(
            TEST_RESOURCE_ID, messaging_profile_id="123"
        )
        request_mock.assert_requested(
            "patch", "/v2/phone_numbers/%s/messaging" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingSettings)

    def test_instance_url_invalid(self):
        with pytest.raises(error.InvalidRequestError):
            telnyx.MessagingSettings(id=1).instance_url()
