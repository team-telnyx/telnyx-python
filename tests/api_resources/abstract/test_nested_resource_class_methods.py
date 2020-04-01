from __future__ import absolute_import, division, print_function

import pytest

import telnyx


class TestNestedResourceClassMethods(object):
    @telnyx.api_resources.abstract.nested_resource_class_methods(
        "nested", operations=["create", "retrieve", "update", "delete", "list"]
    )
    class MainResource(telnyx.api_resources.abstract.APIResource):
        OBJECT_NAME = "mainresource"

    def test_nested_resource_class_methods_no_operator(self):
        with pytest.raises(ValueError):
            telnyx.api_resources.abstract.nested_resource_class_methods(
                "a", operations=None
            )

    def test_create_nested(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v2/mainresources/id/nesteds",
            {"id": "nested_id", "object": "nested", "foo": "bar"},
        )
        nested_resource = self.MainResource.create_nested("id", foo="bar")
        request_mock.assert_requested(
            "post", "/v2/mainresources/id/nesteds", {"foo": "bar"}, None
        )
        assert nested_resource.foo == "bar"

    def test_retrieve_nested(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v2/mainresources/id/nesteds/nested_id",
            {"id": "nested_id", "object": "nested", "foo": "bar"},
        )
        nested_resource = self.MainResource.retrieve_nested("id", "nested_id")
        request_mock.assert_requested(
            "get", "/v2/mainresources/id/nesteds/nested_id", {}, None
        )
        assert nested_resource.foo == "bar"

    def test_modify_nested(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v2/mainresources/id/nesteds/nested_id",
            {"id": "nested_id", "object": "nested", "foo": "baz"},
        )
        nested_resource = self.MainResource.modify_nested("id", "nested_id", foo="baz")
        request_mock.assert_requested(
            "post", "/v2/mainresources/id/nesteds/nested_id", {"foo": "baz"}, None
        )
        assert nested_resource.foo == "baz"

    def test_delete_nested(self, request_mock):
        request_mock.stub_request(
            "delete",
            "/v2/mainresources/id/nesteds/nested_id",
            {"id": "nested_id", "object": "nested", "deleted": True},
        )
        nested_resource = self.MainResource.delete_nested("id", "nested_id")
        request_mock.assert_requested(
            "delete", "/v2/mainresources/id/nesteds/nested_id", {}, None
        )
        assert nested_resource.deleted is True

    def test_list_nesteds(self, request_mock):
        request_mock.stub_request(
            "get", "/v2/mainresources/id/nesteds", {"object": "list", "data": []}
        )
        nested_resource = self.MainResource.list_nesteds("id")
        request_mock.assert_requested("get", "/v2/mainresources/id/nesteds", {}, None)
        assert isinstance(nested_resource.data, list)

    def test_invalid_operation(self):
        class Foo:
            pass

        decorator = telnyx.api_resources.abstract.nested_resource_class_methods(
            "nested", operations=["foo"]
        )

        with pytest.raises(ValueError):
            decorator(Foo)

    def test_rewrite_reserved_words(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v2/mainresources/id/nesteds",
            {"id": "nested_id", "object": "nested", "from": "foo"},
        )
        nested_resource = self.MainResource.create_nested("id", from_="foo")
        request_mock.assert_requested(
            "post", "/v2/mainresources/id/nesteds", {"from": "foo"}, None
        )
        assert nested_resource.from_ == "foo"
