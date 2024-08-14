from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


class TestOutboundVoiceProfile(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.OutboundVoiceProfile.list()
        request_mock.assert_requested("get", "/v2/outbound_voice_profiles")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.OutboundVoiceProfile)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.OutboundVoiceProfile.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/outbound_voice_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.OutboundVoiceProfile)

    def test_is_creatable(self, request_mock):
        resource = telnyx.OutboundVoiceProfile.create(name="my-profile")
        request_mock.assert_requested("post", "/v2/outbound_voice_profiles")
        assert isinstance(resource, telnyx.OutboundVoiceProfile)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_saveable(self, request_mock):
        outbound_voice_profile = telnyx.OutboundVoiceProfile.retrieve(TEST_RESOURCE_ID)
        outbound_voice_profile.concurrent_call_limit = 10
        outbound_voice_profile.name = "Dan"
        resource = outbound_voice_profile.save()
        request_mock.assert_requested(
            "patch", "/v2/outbound_voice_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.OutboundVoiceProfile)
        assert resource is outbound_voice_profile

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.OutboundVoiceProfile.modify(
            TEST_RESOURCE_ID, concurrent_call_limit=10, name="Dan"
        )
        request_mock.assert_requested(
            "patch", "/v2/outbound_voice_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.OutboundVoiceProfile)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_deletable(self, request_mock):
        resource = telnyx.OutboundVoiceProfile.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/outbound_voice_profiles/%s" % TEST_RESOURCE_ID
        )
