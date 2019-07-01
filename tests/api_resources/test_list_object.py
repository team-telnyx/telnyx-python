from __future__ import absolute_import, division, print_function

import json

import pytest

import telnyx


class TestListObject(object):
    @pytest.fixture
    def list_object(self):
        return telnyx.ListObject.construct_from(
            {
                "data": ["foo"],
                "metadata": {"page": {"size": 1, "number": 1}},
                "url": "/my/path",
            },
            "mykey",
        )

    def assert_list_response(self, res):
        assert isinstance(res[0], telnyx.MessagingProfile)
        assert res[0].foo == "bar"

    def assert_dict_response(self, res):
        assert isinstance(res, telnyx.MessagingProfile)
        assert res.foo == "bar"

    def test_for_loop(self, list_object):
        seen = []

        for item in list_object:
            seen.append(item)

        assert seen == ["foo"]

    def test_list(self, request_mock, list_object):
        request_mock.stub_request(
            "get",
            "/my/path",
            {"data": [{"record_type": "messaging_profile", "foo": "bar"}]},
        )

        res = list_object.list(myparam="you")

        request_mock.assert_requested("get", "/my/path", {"myparam": "you"}, None)
        self.assert_list_response(res.data)

    def test_create(self, request_mock, list_object):
        request_mock.stub_request(
            "post",
            "/my/path",
            {"data": {"record_type": "messaging_profile", "foo": "bar"}},
        )

        res = list_object.create(myparam="eter")

        request_mock.assert_requested("post", "/my/path", {"myparam": "eter"}, None)
        self.assert_dict_response(res)

    def test_retrieve(self, request_mock, list_object):
        request_mock.stub_request(
            "get",
            "/my/path/myid",
            {"data": {"record_type": "messaging_profile", "foo": "bar"}},
        )

        res = list_object.retrieve("myid", myparam="cow")

        request_mock.assert_requested("get", "/my/path/myid", {"myparam": "cow"}, None)

        self.assert_dict_response(res)

    def test_len(self, list_object):
        assert len(list_object) == 1

    def test_bool(self, list_object):
        assert list_object

        empty = telnyx.ListObject.construct_from({"data": []}, "mykey")
        assert bool(empty) is False

    def test_serialize_empty_list(self):
        empty = telnyx.ListObject.construct_from({"data": []}, "mykey")
        serialized = str(empty)
        deserialized = telnyx.ListObject.construct_from(json.loads(serialized), "mykey")
        assert deserialized == empty

    def test_serialize_nested_empty_list(self):
        empty = telnyx.ListObject.construct_from({"data": []}, "mykey")
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"nested": empty}, "mykey"
        )
        serialized = str(obj)
        deserialized = telnyx.telnyx_object.TelnyxObject.construct_from(
            json.loads(serialized), "mykey"
        )
        assert deserialized.nested == empty


class TestAutoPaging:
    @staticmethod
    def pageable_model_response(ids, has_more, url):
        if has_more:
            total_pages = 2
            page_number = 1
        else:
            total_pages = 1
            page_number = 1

        return {
            "data": [{"id": id, "record_type": "pageablemodel"} for id in ids],
            "metadata": {"page_number": page_number, "total_pages": total_pages},
            "url": url,
        }

    @staticmethod
    def pageable_token_model_response(ids, token, url):
        return {
            "data": [{"id": id, "record_type": "pageablemodel"} for id in ids],
            "metadata": {"next_page_token": token},
            "url": url,
        }

    def test_iter_one_page(self, request_mock):
        url = "/v2/pageablemodels"
        lo = telnyx.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False, url), "mykey"
        )

        request_mock.assert_no_request()

        seen = [item["id"] for item in lo.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_one_page_by_token(self, request_mock):
        url = "/v2/pageablemodels"
        lo = telnyx.ListObject.construct_from(
            self.pageable_token_model_response(["pm_123", "pm_124"], None, url), "mykey"
        )

        request_mock.assert_no_request()

        seen = [item["id"] for item in lo.auto_paging_iter_by_token()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_two_pages(self, request_mock):
        url = "/v2/pageablemodels"
        lo = telnyx.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True, url), "mykey"
        )
        lo._retrieve_params = {"foo": "bar"}

        request_mock.stub_request(
            "get",
            "/v2/pageablemodels",
            self.pageable_model_response(["pm_125", "pm_126"], False, url),
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        request_mock.assert_requested(
            "get",
            "/v2/pageablemodels",
            {"page": {"size": 20, "number": 2}, "foo": "bar"},
            None,
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]

    def test_iter_by_token_two_pages(self, request_mock):
        url = "/v2/pageablemodels"
        lo = telnyx.ListObject.construct_from(
            self.pageable_token_model_response(["pm_123", "pm_124"], "123", url),
            "mykey",
        )
        lo._retrieve_params = {"foo": "bar"}

        request_mock.stub_request(
            "get",
            "/v2/pageablemodels",
            self.pageable_token_model_response(["pm_125", "pm_126"], None, url),
        )

        seen = [item["id"] for item in lo.auto_paging_iter_by_token()]

        request_mock.assert_requested(
            "get", "/v2/pageablemodels", {"page": {"token": "123"}, "foo": "bar"}, None
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]

    def test_class_method_two_pages(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v2/messaging_profiles",
            {"data": [{"id": "123", "record_type": "messaging_profile"}]},
        )

        seen = [item["id"] for item in telnyx.MessagingProfile.auto_paging_iter()]

        request_mock.assert_requested("get", "/v2/messaging_profiles", {})
        assert seen == ["123"]

    def test_class_method_two_pages_by_token(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v2/messaging_profiles",
            {"data": [{"id": "123", "record_type": "messaging_profile"}]},
        )

        seen = [
            item["id"] for item in telnyx.MessagingProfile.auto_paging_iter_by_token()
        ]

        request_mock.assert_requested("get", "/v2/messaging_profiles", {})
        assert seen == ["123"]
