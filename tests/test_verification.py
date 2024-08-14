import unittest
from unittest.mock import patch
from telnyx.api_resources.verification import Verification

class TestVerification(unittest.TestCase):
    @patch('telnyx.api_requestor.APIRequestor.request')
    def test_verification_by_id(self, mock_request):
        mock_response = {
            "data": {
                "id": "verification_id",
                "status": "verified"
            }
        }
        mock_request.return_value = (mock_response, None)

        verification_id = "verification_id"
        params = {
            "code": "123456"
        }

        response = Verification.verification_by_id(id=verification_id, **params)

        self.assertEqual(response["data"]["id"], verification_id)
        self.assertEqual(response["data"]["status"], "verified")
        mock_request.assert_called_with(
            "post",
            "/v2/verifications/{}/actions/verify".format(verification_id),
            params
        )

if __name__ == '__main__':
    unittest.main()
