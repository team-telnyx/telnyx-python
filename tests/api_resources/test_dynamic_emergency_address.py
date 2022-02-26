from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "0ccc7b54-4df3-4bca-a65a-3da1ecc777f1"


class TestDynamicEmergencyAddress(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.DynamicEmergencyAddress.list()
        request_mock.assert_requested("get", "/v2/dynamic_emergency_addresses")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.DynamicEmergencyAddress)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.DynamicEmergencyAddress.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/dynamic_emergency_addresses/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.DynamicEmergencyAddress)

    def test_is_creatable(self, request_mock):
        resource = telnyx.DynamicEmergencyAddress.create(
            administrative_area="IL",
            house_number="311",
            locality="Chicago",
            postal_code="60654",
            street_name="Superior",
            country_coude="US"
        )

    def test_is_deletable(self, request_mock):
        resource = telnyx.DynamicEmergencyAddress.retrieve(TEST_RESOURCE_ID)
        resource.delete()
