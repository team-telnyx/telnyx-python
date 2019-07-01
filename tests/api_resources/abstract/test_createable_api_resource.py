from __future__ import absolute_import, division, print_function

import telnyx


class TestCreateableAPIResource(object):
    class MyCreatable(telnyx.api_resources.abstract.CreateableAPIResource):
        OBJECT_NAME = "mycreatable"

    def test_create(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v2/mycreatables",
            {"data": {"record_type": "messaging_profile", "foo": "bar"}},
            rheaders={"request-id": "req_id"},
        )

        res = self.MyCreatable.create()

        request_mock.assert_requested("post", "/v2/mycreatables", {})
        assert isinstance(res, telnyx.MessagingProfile)
        assert res.foo == "bar"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

    def test_idempotent_create(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v2/mycreatables",
            {"data": {"record_type": "messaging_profile", "foo": "bar"}},
        )

        res = self.MyCreatable.create()

        request_mock.assert_requested("post", "/v2/mycreatables", {}, {})
        assert isinstance(res, telnyx.MessagingProfile)
        assert res.foo == "bar"
