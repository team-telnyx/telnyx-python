from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestDocument(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Document.list()
        request_mock.assert_requested("get", "/v2/documents")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        telnyx.Document.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/documents/%s" % TEST_RESOURCE_ID)

    def test_is_creatable(self, request_mock):
        resource = telnyx.Document.create(
            filename="test-document.pdf",
            url="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
            file="https://test.com",
        )
        resource
        request_mock.assert_requested("post", "/v2/documents")

    def test_is_modifiable(self, request_mock):
        resource = telnyx.Document.modify(
            TEST_RESOURCE_ID,
            active=False,
            webhook_event_url="https://update.com",
            application_name="updated name",
        )
        resource
        request_mock.assert_requested("patch", "/v2/documents/%s" % TEST_RESOURCE_ID)

    @pytest.mark.skip(reason="Nested get")
    def test_is_deletable(self, request_mock):
        resource = telnyx.Document.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested("delete", "/v2/documents/%s" % TEST_RESOURCE_ID)

    def test_document_links(self, request_mock):
        resources = telnyx.DocumentLink.list()
        request_mock.assert_requested("get", "/v2/document_links")
        assert isinstance(resources.data, list)

    @pytest.mark.skip(reason="Nested get")
    def test_download(self, request_mock):
        resource = telnyx.Document.retrieve(TEST_RESOURCE_ID)
        resource.download()
