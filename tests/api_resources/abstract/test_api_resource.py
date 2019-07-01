from __future__ import absolute_import, division, print_function

import pytest

import telnyx


class TestAPIResource(object):
    class MyResource(telnyx.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

    def test_retrieve_and_refresh(self, request_mock):
        url = "/v2/myresources/foo%2A"
        request_mock.stub_request(
            "get",
            url,
            {"id": "foo2", "bobble": "scrobble"},
            rheaders={"request-id": "req_id"},
        )

        res = self.MyResource.retrieve("foo*", myparam=5)

        request_mock.assert_requested("get", url, {"myparam": 5}, None)
        assert res.bobble == "scrobble"
        assert res.id == "foo2"
        assert res.api_key == "KEY123"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

        url = "/v2/myresources/foo2"
        request_mock.stub_request("get", url, {"frobble": 5})

        res = res.refresh()

        request_mock.assert_requested("get", url, {"myparam": 5}, None)
        assert res.frobble == 5
        with pytest.raises(KeyError):
            res["bobble"]

    def test_convert_to_telnyx_object(self):
        sample = {
            "foo": "bar",
            "adict": {"record_type": "messaging_profile", "id": 42, "amount": 7},
            "alist": [{"record_type": "messaging_profile", "name": "chilango"}],
        }

        converted = telnyx.util.convert_to_telnyx_object(sample, "akey")

        # Types
        assert isinstance(converted, telnyx.telnyx_object.TelnyxObject)
        assert isinstance(converted.adict, telnyx.MessagingProfile)
        assert len(converted.alist) == 1
        assert isinstance(converted.alist[0], telnyx.MessagingProfile)

        # Values
        assert converted.foo == "bar"
        assert converted.adict.id == 42
        assert converted.alist[0].name == "chilango"

        # Stripping
        # TODO: We should probably be stripping out this property
        # self.assertRaises(AttributeError, getattr, converted.adict, 'object')

    def test_raise_on_incorrect_id_type(self):
        for obj in [None, 1, 3.14, dict(), list(), set(), tuple(), object()]:
            with pytest.raises(telnyx.error.InvalidRequestError):
                self.MyResource.retrieve(obj)
