from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestSIMCard(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.SIMCard.list()
        request_mock.assert_requested("get", "/v2/sim_cards")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.SIMCard)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.SIMCard.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/sim_cards/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.SIMCard)

    def test_is_saveable(self, request_mock):
        sim_card = telnyx.SIMCard.retrieve(TEST_RESOURCE_ID)
        sim_card.tags = ["foo", "bar"]
        resource = sim_card.save()
        request_mock.assert_requested("patch", "/v2/sim_cards/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.SIMCard)
        assert resource is sim_card

    def test_is_modifiable(self, request_mock):
        resource = telnyx.SIMCard.modify(TEST_RESOURCE_ID, tags=["foo", "bar"])
        request_mock.assert_requested("patch", "/v2/sim_cards/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.SIMCard)

    def test_enable(self, request_mock):
        resource = telnyx.SIMCard.retrieve(TEST_RESOURCE_ID)
        resource.enable()
        request_mock.assert_requested(
            "post", "/v2/sim_cards/%s/actions/enable" % TEST_RESOURCE_ID
        )

    def test_disable(self, request_mock):
        resource = telnyx.SIMCard.retrieve(TEST_RESOURCE_ID)
        resource.disable()
        request_mock.assert_requested(
            "post", "/v2/sim_cards/%s/actions/disable" % TEST_RESOURCE_ID
        )

    def test_register(self, request_mock):
        telnyx.SIMCard.register()
        request_mock.assert_requested("post", "/v2/actions/register/sim_cards")
