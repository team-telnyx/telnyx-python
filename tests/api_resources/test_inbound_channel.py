from __future__ import absolute_import, division, print_function

import telnyx


class TestInboundChannels(object):
    def test_is_retrievable(self, request_mock):
        request_mock.stub_response({
            "data": {
                "channels": [7],
                "record_type": "inbound_channels"
            }
        })
        resource = telnyx.InboundChannel.retrieve()
        request_mock.assert_requested("get", "/v2/phone_numbers/inbound_channels")
        assert isinstance(resource, telnyx.InboundChannel)

    def test_is_saveable(self, request_mock):
        request_mock.stub_response({
            "data": {
                "channels": [7],
                "record_type": "inbound_channels"
            }
        })
        inbound_channels = telnyx.InboundChannel.retrieve()

        request_mock.stub_response({
            "data": {
                "channels": [10],
                "record_type": "inbound_channels"
            }
        })
        inbound_channels.channels = 10
        resource = inbound_channels.save()
        request_mock.assert_requested("patch", "/v2/phone_numbers/inbound_channels")
        assert isinstance(resource, telnyx.InboundChannel)
        assert resource is inbound_channels

    def test_is_modifiable(self, request_mock):
        request_mock.stub_response({
            "data": {
                "channels": [10],
                "record_type": "inbound_channels"
            }
        })
        resource = telnyx.InboundChannel.modify(channels=10)
        request_mock.assert_requested("patch", "/v2/phone_numbers/inbound_channels")
        assert isinstance(resource, telnyx.InboundChannel)