from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "123"


class TestRegulatoryRequirement(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.RegulatoryRequirement.list()
        request_mock.assert_requested("get", "/v2/regulatory_requirements")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.RegulatoryRequirement)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.RegulatoryRequirement.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/regulatory_requirements/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.RegulatoryRequirement)
