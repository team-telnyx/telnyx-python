import pytest
import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"
TEST_PHONE_NUMBER = "+13125000000"
VERIFY_CODE = "12345"
VERIFY_PROFILE = "12ade33a-21c0-473b-b055-b3c836e1c292"


class TestVerification(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.Verification.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/verifications/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.Verification)

    def test_can_verify_by_phone_number(self, request_mock):
        telnyx.Verification.verify_by_phone_number(
            phone_number=TEST_PHONE_NUMBER,
            code=VERIFY_CODE,
            verify_profile_id=VERIFY_PROFILE,
        )
        request_mock.assert_requested(
            "post",
            "/v2/verifications/by_phone_number/%s/actions/verify" % TEST_PHONE_NUMBER,
        )

    def test_can_verify_by_id(self, request_mock):
        telnyx.Verification.verify_by_id(
            verification_id=TEST_RESOURCE_ID,
            code=VERIFY_CODE,
            verify_profile_id=VERIFY_PROFILE,
        )
        request_mock.assert_requested(
            "post",
            "/v2/verifications/%s/actions/verify" % TEST_RESOURCE_ID,
        )

    def test_can_list_verifications(self, request_mock):
        resources = telnyx.Verification.by_phone_number(TEST_PHONE_NUMBER)
        request_mock.assert_requested("get", "/v2/verifications/by_phone_number/%s" %TEST_PHONE_NUMBER)
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.Verification)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_verify_by_sms(self, request_mock):
        telnyx.Verification.sms(
            phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE
        )
        request_mock.assert_requested("post", "/v2/verifications/sms")

    def test_verify_by_call(self, request_mock):
        telnyx.Verification.call(
            phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE
        )
        request_mock.assert_requested("post", "/v2/verifications/call")

    def test_verify_by_flashcall(self, request_mock):
        telnyx.Verification.flashcall(
            phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE
        )
        request_mock.assert_requested("post", "/v2/verifications/flashcall")
