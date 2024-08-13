import unittest
from telnyx.api_resources.verification import Verification
from telnyx.api_requestor import APIRequestor
from unittest.mock import patch

class TestVerification(unittest.TestCase):
    @patch.object(APIRequestor, 'request')
    def test_verify_verification_code_by_id(self, mock_request):
        verification_id = "12345"
        code = "67890"
        mock_request.return_value = ({"data": "success"}, "api_key")

        verification = Verification()
        response, api_key = verification.verify_verification_code_by_id(verification_id, code)

        self.assertEqual(response["data"], "success")
        self.assertEqual(api_key, "api_key")
        mock_request.assert_called_with(
            "post",
            "/v2/verifications/{}/actions/verify".format(verification_id),
            params={"code": code},
        )

if __name__ == "__main__":
    unittest.main()
