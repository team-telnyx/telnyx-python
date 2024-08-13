import telnyx
from unittest.mock import patch

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
        resource = telnyx.Verification.retrieve(TEST_RESOURCE_ID)
        resource.verify_by_phone_number(
            code=VERIFY_CODE,
            phone_number=TEST_PHONE_NUMBER,
            verify_profile_id=VERIFY_PROFILE,
        )
        request_mock.assert_requested(
            "post",
            "/v2/verifications/by_phone_number/%s/actions/verify" % TEST_PHONE_NUMBER,
        )

    def test_verify_verification_code_by_id(self, request_mock):
        resource = telnyx.Verification.retrieve(TEST_RESOURCE_ID)
        with patch.object(telnyx.api_requestor.APIRequestor, 'request', return_value=({"data": {"success": True}}, "api_key")) as mock_request:
            resource.verify_verification_code_by_id(
                code=VERIFY_CODE,
            )
            mock_request.assert_called_with(
                "post",
                "/v2/verifications/%s/actions/verify" % TEST_RESOURCE_ID,
                {"code": VERIFY_CODE},
            )

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
