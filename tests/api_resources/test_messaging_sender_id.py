from __future__ import absolute_import, division, print_function

import telnyx


TEST_RESOURCE_ID = "123"


class TestMessagingSenderId(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.MessagingSenderId.list()
        request_mock.assert_requested("get", "/v2/messaging_sender_ids")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingSenderId)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.MessagingSenderId.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_sender_ids/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingSenderId)

    def test_is_creatable(self, request_mock):
        resource = telnyx.MessagingSenderId.create(country="US", type="custom")
        request_mock.assert_requested("post", "/v2/messaging_sender_ids")
        assert isinstance(resource, telnyx.MessagingSenderId)

    def test_is_saveable(self, request_mock):
        messaging_sender_id = telnyx.MessagingSenderId.retrieve(TEST_RESOURCE_ID)
        messaging_sender_id.name = "value"
        resource = messaging_sender_id.save()
        request_mock.assert_requested(
            "patch", "/v2/messaging_sender_ids/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingSenderId)
        assert resource is messaging_sender_id

    def test_is_modifiable(self, request_mock):
        resource = telnyx.MessagingSenderId.modify(TEST_RESOURCE_ID, name="Test")
        request_mock.assert_requested(
            "patch", "/v2/messaging_sender_ids/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingSenderId)

    def test_is_deletable(self, request_mock):
        resource = telnyx.MessagingSenderId.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/messaging_sender_ids/%s" % TEST_RESOURCE_ID
        )
