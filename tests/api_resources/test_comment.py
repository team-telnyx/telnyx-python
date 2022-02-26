from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


@pytest.mark.skip(reason="Filter off")
class TestComment(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Comment.list(
            filter={
                "comment_record_type": "sub_number_order",
                "comment_record_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
            }
        )
        request_mock.assert_requested("get", "/v2/comments")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.Comment)

    def test_is_creatable(self, request_mock):
        resource = telnyx.Comment.create()
        request_mock.assert_requested("post", "/v2/comments")
        assert isinstance(resource, telnyx.Comment)
