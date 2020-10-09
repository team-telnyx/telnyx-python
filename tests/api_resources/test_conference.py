from __future__ import absolute_import, division, print_function

import telnyx

CONFERENCE_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
_call_control_id = "AgDIxmoRX6QMuaIj_uXRXnPAXP0QlNfXczRrZvZakpWxBlpw48KyZQ=="


def create_conference():
    return telnyx.Conference.create(
        name="Business",
        call_control_id=_call_control_id,
        client_state="aGF2ZSBhIG5pY2UgZGF5ID1d",
        command_id="891510ac-f3e4-11e8-af5b-de00688a4901",
    )


class TestConference(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Conference.list()
        request_mock.assert_requested("get", "/v2/conferences")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.Conference)

    def test_is_creatable(self, request_mock):
        resource = create_conference()
        request_mock.assert_requested("post", "/v2/conferences")
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_join(self, request_mock):
        resource = create_conference()
        resource.join(call_control_id=_call_control_id)
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/join" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_join(self, request_mock):
        resource = create_conference()
        resource.create_join(CONFERENCE_ID, call_control_id=_call_control_id)
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/join" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_mute(self, request_mock):
        resource = create_conference()
        resource.mute(call_control_ids=[_call_control_id])
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/mute" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_mute(self, request_mock):
        resource = create_conference()
        resource.create_mute(CONFERENCE_ID, call_control_ids=[_call_control_id])
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/mute" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_unmute(self, request_mock):
        resource = create_conference()
        resource.unmute(call_control_ids=[_call_control_id])
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/unmute" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_unmute(self, request_mock):
        resource = create_conference()
        resource.create_unmute(CONFERENCE_ID, call_control_ids=[_call_control_id])
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/unmute" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_hold(self, request_mock):
        resource = create_conference()
        resource.hold(
            call_control_ids=[_call_control_id],
            audio_url="http://example.com/message.wav",
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/hold" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_hold(self, request_mock):
        resource = create_conference()
        resource.create_hold(
            CONFERENCE_ID,
            call_control_ids=[_call_control_id],
            audio_url="http://example.com/message.wav",
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/hold" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_unhold(self, request_mock):
        resource = create_conference()
        resource.unhold(
            call_control_ids=[_call_control_id],
            audio_url="http://example.com/message.wav",
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/unhold" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_unhold(self, request_mock):
        resource = create_conference()
        resource.create_unhold(
            CONFERENCE_ID,
            call_control_ids=[_call_control_id],
            audio_url="http://example.com/message.wav",
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/unhold" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_speak(self, request_mock):
        resource = create_conference()
        resource.speak(
            call_control_ids=[_call_control_id],
            voice="female",
            payload="I hope this unit tests passes",
            language="en-AU",
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/speak" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_speak(self, request_mock):
        resource = create_conference()
        resource.create_speak(
            CONFERENCE_ID,
            voice="female",
            payload="I hope this unit tests passes",
            language="en-AU",
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/speak" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_record_start(self, request_mock):
        resource = create_conference()
        resource.record_start(
            call_control_ids=[_call_control_id], format="wav", channels="single"
        )
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/record_start" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_record_start(self, request_mock):
        resource = create_conference()
        resource.create_record_start(CONFERENCE_ID, format="wav", channels="single")
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/record_start" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_record_stop(self, request_mock):
        resource = create_conference()
        resource.record_stop(call_control_ids=[_call_control_id])
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/record_stop" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)

    def test_can_call_create_record_stop(self, request_mock):
        resource = create_conference()
        resource.create_record_stop(CONFERENCE_ID)
        request_mock.assert_requested(
            "post", "/v2/conferences/%s/actions/record_stop" % CONFERENCE_ID
        )
        assert isinstance(resource, telnyx.Conference)
