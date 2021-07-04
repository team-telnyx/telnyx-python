from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "tier_1_support"
CALL_CONTROL_ID = "AgDIxmoRX6QMuaIj_uXRXnPAXP0QlNfXczRrZvZakpWxBlpw48KyZQ=="


class TestQueue(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.Queue.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/queues/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.Queue)

    def test_can_call_retrieve_call(self, request_mock):
        resource = telnyx.Queue.retrieve(TEST_RESOURCE_ID)
        queue_call = resource.retrieve_call(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "get", "/v2/queues/%s/calls/%s" % (resource.name, CALL_CONTROL_ID)
        )
        assert isinstance(queue_call, telnyx.QueueCall)

    def test_can_call_list_calls(self, request_mock):
        resource = telnyx.Queue.retrieve(TEST_RESOURCE_ID)
        queue_calls = resource.list_calls()
        request_mock.assert_requested("get", "/v2/queues/%s/calls" % resource.name)
        assert isinstance(queue_calls.data[0], telnyx.QueueCall)
