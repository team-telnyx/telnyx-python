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

    def test_is_savable(self, request_mock):
        _ = telnyx.Verification.create(
            phone_number=TEST_PHONE_NUMBER, type="sms", verify_profile_id=VERIFY_PROFILE
        )
        request_mock.assert_requested("post", "/v2/verifications")

    def test_can_verify_by_phone_number(self, request_mock):
        resource = telnyx.Verification.retrieve(TEST_RESOURCE_ID)
        resource.verify_by_phone_number(
            code=VERIFY_CODE, phone_number=TEST_PHONE_NUMBER
        )
        request_mock.assert_requested(
            "post",
            "/v2/verifications/by_phone_number/%s/actions/verify" % TEST_PHONE_NUMBER,
        )
