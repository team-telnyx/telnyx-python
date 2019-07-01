from __future__ import absolute_import, division, print_function

import json

from telnyx.telnyx_response import TelnyxResponse


class TestTelnyxResponse(object):
    def test_request_id(self):
        response, headers, body, code = self.mock_telnyx_response()
        assert response.request_id == headers["request-id"]

    def test_code(self):
        response, headers, body, code = self.mock_telnyx_response()
        assert response.code == code

    def test_headers(self):
        response, headers, body, code = self.mock_telnyx_response()
        assert response.headers == headers

    def test_body(self):
        response, headers, body, code = self.mock_telnyx_response()
        assert response.body == body

    def test_data(self):
        response, headers, body, code = self.mock_telnyx_response()
        assert response.data == json.loads(body)

    @staticmethod
    def mock_telnyx_response():
        code = 200
        headers = TestTelnyxResponse.mock_headers()
        body = TestTelnyxResponse.mock_body()
        response = TelnyxResponse(body, code, headers)
        return response, headers, body, code

    @staticmethod
    def mock_headers():
        return {"request-id": "123456"}

    @staticmethod
    def mock_body():
        return '{"data": { "id": "12345", "record_type": "messaging_profile", "name": "New Messaging Profile" }}'
