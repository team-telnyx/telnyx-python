from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestSIMCardActions(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.SIMCardAction.list()
        request_mock.assert_requested("get", "/v2/sim_card_actions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.SIMCardAction)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.SIMCardAction.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/sim_card_actions/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.SIMCardAction)
