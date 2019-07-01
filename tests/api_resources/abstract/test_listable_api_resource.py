from __future__ import absolute_import, division, print_function

import telnyx


class TestListableAPIResource(object):
    class MyListable(telnyx.api_resources.abstract.ListableAPIResource):
        OBJECT_NAME = "mylistable"

    def test_all(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v2/mylistables",
            {
                "data": [
                    {"record_type": "messaging_profile", "name": "jose"},
                    {"record_type": "messaging_profile", "name": "curly"},
                ]
            },
            rheaders={"request-id": "req_id"},
        )

        res = self.MyListable.list()
        request_mock.assert_requested("get", "/v2/mylistables", {})
        assert len(res.data) == 2
        assert all(isinstance(obj, telnyx.MessagingProfile) for obj in res.data)
        assert res.data[0].name == "jose"
        assert res.data[1].name == "curly"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"
