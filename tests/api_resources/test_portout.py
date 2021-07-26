from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "f1486bae-f067-460c-ad43-73a92848f902"


class TestPortOut(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.PortOut.list()
        request_mock.assert_requested("get", "/v2/portouts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.PortOut)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.PortOut.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/portouts/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.PortOut)
