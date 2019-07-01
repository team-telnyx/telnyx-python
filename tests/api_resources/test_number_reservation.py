import telnyx


class TestNumberOrder(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NumberReservation.list()
        request_mock.assert_requested("get", "/v2/number_reservations")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.NumberReservation)
