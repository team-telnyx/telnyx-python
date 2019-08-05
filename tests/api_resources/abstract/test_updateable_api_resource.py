from __future__ import absolute_import, division, print_function

import pytest

import telnyx


class TestUpdateableAPIResource(object):
    class MyUpdateable(telnyx.api_resources.abstract.UpdateableAPIResource):
        OBJECT_NAME = "myupdateable"

    @pytest.fixture
    def obj(self, request_mock):
        request_mock.stub_request(
            "patch",
            "/v2/myupdateables/myid",
            {"id": "myid", "thats": "it"},
            rheaders={"request-id": "req_id"},
        )

        return self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "foo": "bar",
                "baz": "boz",
                "nested_object": {"size": "l", "score": 4, "height": 10},
            },
            "mykey",
        )

    def checkSave(self, obj):
        assert obj is obj.save()

        assert obj.thats == "it"
        # TODO: Should we force id to be retained?
        # assert obj.id == 'myid'
        with pytest.raises(AttributeError):
            obj.baz

    def test_save(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.nested_object.size = "m"
        obj.nested_object.info = "a2"
        obj.nested_object.height = None

        self.checkSave(obj)

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {
                "baz": "updated",
                "other": "newval",
                "nested_object": {"size": "m", "info": "a2", "height": ""},
            },
            None,
        )

        assert obj.last_response is not None
        assert obj.last_response.request_id == "req_id"

        # Saving again should not cause any request.
        request_mock.reset_mock()
        self.checkSave(obj)
        request_mock.assert_no_request()

        # Setting the same value should cause a request.
        request_mock.stub_request(
            "patch", "/v2/myupdateables/myid", {"id": "myid", "thats": "it"}
        )

        obj.thats = "it"
        self.checkSave(obj)

        request_mock.assert_requested(
            "patch", "/v2/myupdateables/myid", {"thats": "it"}, None
        )

        # Changing the value should cause a request.
        request_mock.stub_request(
            "patch", "/v2/myupdateables/myid", {"id": "myid", "thats": "it"}
        )

        obj.id = "myid"
        obj.thats = "updated"
        self.checkSave(obj)

        request_mock.assert_requested(
            "patch", "/v2/myupdateables/myid", {"thats": "updated"}, None
        )

    def test_add_key_to_nested_object(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"size": "l", "score": 4, "height": 10}},
            "mykey",
        )

        acct.legal_entity["first_name"] = "bob"

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"legal_entity": {"first_name": "bob"}},
            None,
        )

    def test_save_nothing(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "nested_object": {"key": "value"}}, "mykey"
        )

        assert acct is acct.save()

        request_mock.assert_no_request()

    def test_do_not_replace_nested_object(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"last_name": "smith"}}, "mykey"
        )

        acct.legal_entity = {"first_name": "bob"}

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"legal_entity": {"first_name": "bob", "last_name": "smith"}},
            None,
        )

    def test_array_setting(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {}}, "mykey"
        )

        acct.legal_entity.additional_owners = [{"first_name": "Bob"}]

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"legal_entity": {"additional_owners": [{"first_name": "Bob"}]}},
            None,
        )

    def test_array_none(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"additional_owners": None}}, "mykey"
        )

        acct.foo = "bar"

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch", "/v2/myupdateables/myid", {"foo": "bar"}, None
        )

    def test_array_insertion(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"additional_owners": []}}, "mykey"
        )

        acct.legal_entity.additional_owners.append({"first_name": "Bob"})

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"legal_entity": {"additional_owners": {"0": {"first_name": "Bob"}}}},
            None,
        )

    def test_array_update(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {
                    "additional_owners": [{"first_name": "Bob"}, {"first_name": "Jane"}]
                },
            },
            "mykey",
        )

        acct.legal_entity.additional_owners[1].first_name = "Janet"

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {
                "legal_entity": {
                    "additional_owners": {"0": {}, "1": {"first_name": "Janet"}}
                }
            },
            None,
        )

    def test_array_noop(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {
                "id": "myid",
                "legal_entity": {"additional_owners": [{"first_name": "Bob"}]},
                "currencies_supported": ["usd", "cad"],
            },
            "mykey",
        )

        assert acct is acct.save()

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"legal_entity": {"additional_owners": {"0": {}}}},
            None,
        )

    def test_hash_noop(self, request_mock, obj):
        acct = self.MyUpdateable.construct_from(
            {"id": "myid", "legal_entity": {"address": {"line1": "1 Two Three"}}},
            "mykey",
        )

        assert acct is acct.save()

        request_mock.assert_no_request()

    def test_save_replace_nested_object_with_number(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.nested_object = 3

        self.checkSave(obj)

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"baz": "updated", "other": "newval", "nested_object": 3},
            None,
        )

    def test_save_do_not_overwrite_nested_object(self, request_mock, obj):
        old_nested_object = obj._previous.get("nested_object")
        obj.nested_object = {}
        self.checkSave(obj)

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {"nested_object": old_nested_object},
            None,
        )

    def test_save_do_not_replace_nested_object(self, request_mock, obj):
        old_nested_object = obj._previous.get("nested_object")
        obj.baz = "updated"
        obj.other = "newval"
        obj.nested_object = {"size": "m", "info": "a2", "score": 4}

        self.checkSave(obj)

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {
                "baz": "updated",
                "other": "newval",
                "nested_object": {
                    "size": "m",
                    "info": "a2",
                    "height": old_nested_object.get("height"),
                    "score": 4,
                },
            },
            None,
        )

    def test_save_update_nested_object(self, request_mock, obj):
        obj.baz = "updated"
        obj.other = "newval"
        obj.nested_object.update({"size": "m", "info": "a2", "score": 4})

        self.checkSave(obj)

        request_mock.assert_requested(
            "patch",
            "/v2/myupdateables/myid",
            {
                "baz": "updated",
                "other": "newval",
                "nested_object": {"size": "m", "info": "a2", "score": 4},
            },
            None,
        )
