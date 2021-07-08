import telnyx

TEST_RESOURCE_ID = "123"
TEST_PHONE_NUMBER = "+13125000000"
VERIFY_CODE = "12345"
VERIFY_PROFILE = "32567"


class TestVerification(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.Verification.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/verifications/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.Verification)

    def test_can_verify_by_phone_number(self, request_mock):
        resource = telnyx.Verification.retrieve(TEST_RESOURCE_ID)
        resource.verify_by_phone_number(
            code=VERIFY_CODE, phone_number=TEST_PHONE_NUMBER
        )
        request_mock.assert_requested(
            "post",
            "/v2/verifications/by_phone_number/%s/actions/verify" % TEST_PHONE_NUMBER,
        )

    def test_verify_by_sms(self, request_mock):
        telnyx.Verification.sms(phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE)
        request_mock.assert_requested("post", "/v2/verifications/sms")

    def test_verify_by_psd2(self, request_mock):
        telnyx.Verification.psd2(
            phone_number=TEST_PHONE_NUMBER,
            verify_profile_id=VERIFY_PROFILE,
            amount='99.99',
            currency='USD',
            payee='Acme'
        )
        request_mock.assert_requested("post", "/v2/verifications/psd2")

    def test_verify_by_call(self, request_mock):
        telnyx.Verification.call(phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE)
        request_mock.assert_requested("post", "/v2/verifications/call")

    def test_verify_by_flashcall(self, request_mock):
        telnyx.Verification.flashcall(
            phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE
        )
        request_mock.assert_requested("post", "/v2/verifications/flashcall")

    def test_verify_by_whatsapp(self, request_mock):
        telnyx.Verification.whatsapp(
            phone_number=TEST_PHONE_NUMBER, verify_profile_id=VERIFY_PROFILE
        )
        request_mock.assert_requested("post", "/v2/verifications/whatsapp")
