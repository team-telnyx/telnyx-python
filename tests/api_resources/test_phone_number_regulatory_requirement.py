from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "123"


class TestPhoneNumberRegulatoryRequirement(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.PhoneNumberRegulatoryRequirement.list()
        request_mock.assert_requested("get", "/v2/phone_number_regulatory_requirements")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.PhoneNumberRegulatoryRequirement)

    def test_is_retrievable(self, request_mock):
        with pytest.raises(telnyx.error.InvalidRequestError):
            telnyx.PhoneNumberRegulatoryRequirement.retrieve(TEST_RESOURCE_ID)
