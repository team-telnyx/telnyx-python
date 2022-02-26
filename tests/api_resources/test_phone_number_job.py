from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


class TestPhoneNumberJob(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.PhoneNumberJob.list()
        request_mock.assert_requested("get", "/v2/phone_numbers/jobs")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.PhoneNumberJob.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/phone_numbers/jobs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PhoneNumberJob)

    def test_update_emergency_settings(self, request_mock):
        telnyx.PhoneNumberJob.update_emergency_settings(
            emergency_address_id="53829456729313",
            emergency_enabled=True,
            phone_numbers=[],
        )
        request_mock.assert_requested(
            "post", "/v2/phone_numbers/jobs/update_emergency_settings"
        )

    def test_update_phone_numbers(self, request_mock):
        telnyx.PhoneNumberJob.update_phone_numbers(phone_numbers=[])
        request_mock.assert_requested(
            "post", "/v2/phone_numbers/jobs/update_phone_numbers"
        )

    def test_delete_phone_numbers(self, request_mock):
        telnyx.PhoneNumberJob.delete_phone_numbers(phone_numbers=[])
        request_mock.assert_requested(
            "post", "/v2/phone_numbers/jobs/delete_phone_numbers"
        )
