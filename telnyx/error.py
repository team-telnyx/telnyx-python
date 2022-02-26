from __future__ import absolute_import, division, print_function

from telnyx.six import python_2_unicode_compatible


@python_2_unicode_compatible
class TelnyxError(Exception):
    def __init__(
        self,
        errors=None,
        http_status=None,
        http_body=None,
        json_body=None,
        http_headers=None,
    ):

        self.errors = errors
        self.http_status = http_status
        self.json_body = json_body
        self.http_headers = http_headers or {}
        self.request_id = self.http_headers.get("request-id", None)
        message = self.build_message()
        self._message = message

        super(TelnyxError, self).__init__(message)

        if http_body and hasattr(http_body, "decode"):
            try:
                http_body = http_body.decode("utf-8")
            except BaseException:
                http_body = (
                    "<Could not decode body as UTF-8. "
                    "Please report to support@telnyx.com>"
                )
        self.http_body = http_body

    def build_message(self):
        return "{message}{other_errors_message}{full_details}".format(
            message=self.extract_message(),
            other_errors_message=self.other_errors_message(),
            full_details=self.full_details(),
        )

    def full_details(self):
        if isinstance(self.errors, list) and len(self.errors) > 0:
            return "Full details: {errors}".format(errors=self.errors)
        else:
            return ""

    def extract_message(self):
        if isinstance(self.errors, list):
            if len(self.errors) > 0:
                return self.errors[0].get("title", "")
            else:
                return ""
        elif self.errors is None:
            return ""
        else:
            return self.errors

    def other_errors_message(self):
        count = self.errors_count()
        if count > 2:
            return "plus {count} other errors. ".format(count=count)
        elif count == 2:
            return "plus 1 other error. "
        else:
            return ""

    def errors_count(self):
        if isinstance(self.errors, list):
            return len(self.errors)
        else:
            return 1

    def __str__(self):
        msg = self._message or "<empty message>"
        if self.request_id is not None:
            return "Request {0}: {1}".format(self.request_id, msg)
        else:
            return msg

    # Returns the underlying `Exception` (base class) message, which is usually
    # the raw message returned by Telnyx's API. This was previously available
    # in python2 via `error.message`. Unlike `str(error)`, it omits "Request
    # req_..." from the beginning of the string.
    @property
    def user_message(self):
        return self._message

    def __repr__(self):
        return "%s(message=%r, http_status=%r, request_id=%r)" % (
            self.__class__.__name__,
            self._message,
            self.http_status,
            self.request_id,
        )


class APIConnectionError(TelnyxError):
    def __init__(
        self,
        message,
        http_body=None,
        http_status=None,
        json_body=None,
        http_headers=None,
        should_retry=False,
    ):
        super(APIConnectionError, self).__init__(
            message, http_body, http_status, json_body, http_headers
        )
        self.should_retry = should_retry


class InvalidRequestError(TelnyxError):
    # 400
    pass


class AuthenticationError(TelnyxError):
    # 401
    pass


class PermissionError(TelnyxError):
    # 403
    pass


class ResourceNotFoundError(TelnyxError):
    # 404
    pass


class MethodNotSupportedError(TelnyxError):
    # 405
    pass


class TimeoutError(TelnyxError):
    # 408
    pass


class UnsupportedMediaTypeError(TelnyxError):
    # 415
    pass


class InvalidParametersError(TelnyxError):
    # 422
    pass


class RateLimitError(TelnyxError):
    # 429
    pass


class APIError(TelnyxError):
    # 500
    pass


class ServiceUnavailableError(TelnyxError):
    # 503
    pass


class SignatureVerificationError(TelnyxError):
    def __init__(self, message, sig_header, timestamp_header, http_body=None):
        super(SignatureVerificationError, self).__init__(message, http_body)
        self.sig_header = sig_header
        self.timestamp_header = timestamp_header
