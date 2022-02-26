from __future__ import absolute_import, division, print_function

import calendar
import datetime
import json
import platform
import time

import telnyx
from telnyx import error, http_client, six, util
from telnyx.multipart_data_generator import MultipartDataGenerator
from telnyx.six.moves.urllib.parse import urlencode, urlsplit, urlunsplit
from telnyx.telnyx_response import TelnyxResponse


def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _encode_nested_dict(key, data, fmt="%s[%s]"):
    d = {}
    for subkey, subvalue in six.iteritems(data):
        d[fmt % (key, subkey)] = subvalue
    return d


def _api_encode(data):
    for key, value in six.iteritems(data):
        key = util.utf8(key)
        if value is None:
            continue
        elif isinstance(value, list) or isinstance(value, tuple):
            for sv in value:
                if isinstance(sv, dict):
                    subdict = _encode_nested_dict("%s[]" % key, sv)
                    for k, v in _api_encode(subdict):
                        yield (k, v)
                else:
                    yield ("%s[]" % key, util.utf8(sv))
        elif isinstance(value, dict):
            subdict = _encode_nested_dict(key, value)
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, util.utf8(value))


def _build_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlsplit(url)

    if base_query:
        query = "%s&%s" % (base_query, query)

    return urlunsplit((scheme, netloc, path, query, fragment))


class APIRequestor(object):
    def __init__(self, key=None, client=None, api_base=None):
        self.api_base = api_base or telnyx.api_base
        self.api_key = key

        from telnyx import proxy, verify_ssl_certs as verify

        self._client = (
            client
            or telnyx.default_http_client
            or http_client.new_default_http_client(verify_ssl_certs=verify, proxy=proxy)
        )

        self._last_request_metrics = None

    @classmethod
    def format_app_info(cls, info):
        str = info["name"]
        if info["version"]:
            str += "/%s" % (info["version"],)
        if info["url"]:
            str += " (%s)" % (info["url"],)
        return str

    def request(self, method, url, params=None, headers=None):
        rbody, rcode, rheaders, my_api_key = self.request_raw(
            method.lower(), url, params, headers
        )
        resp = self.interpret_response(rbody, rcode, rheaders)
        return resp, my_api_key

    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_list = resp["errors"]
        except (KeyError, TypeError):
            raise error.APIError(
                [
                    {
                        "title": "Invalid response object from API: %r (HTTP response code "
                        "was %d)" % (rbody, rcode)
                    }
                ],
                rbody,
                rcode,
                resp,
            )

        err = self.specific_api_error(rbody, rcode, resp, rheaders, error_list)

        raise err

    def specific_api_error(self, rbody, rcode, resp, rheaders, error_list):
        for err in error_list:
            util.log_info(
                "Telnyx API error received",
                error_code=err.get("code"),
                error_detail=err.get("detail"),
                error_source=err.get("source"),
                error_title=err.get("title"),
            )

        if rcode == 400:
            return error.InvalidRequestError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 401:
            return error.AuthenticationError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 403:
            return error.PermissionError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 404:
            return error.ResourceNotFoundError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 405:
            return error.MethodNotSupportedError(
                error_list, rbody, rcode, resp, rheaders
            )
        elif rcode == 408:
            return error.TimeoutError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 415:
            return error.UnsupportedMediaTypeError(
                error_list, rbody, rcode, resp, rheaders
            )
        elif rcode == 422:
            return error.InvalidParametersError(
                error_list, rbody, rcode, resp, rheaders
            )
        elif rcode == 429:
            return error.RateLimitError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 500:
            return error.APIError(error_list, rbody, rcode, resp, rheaders)
        elif rcode == 503:
            return error.ServiceUnavailableError(
                error_list, rbody, rcode, resp, rheaders
            )
        else:
            return error.APIError(error_list, rbody, rcode, resp, rheaders)

    def request_headers(self, api_key, method):
        user_agent = "Telnyx/v2 PythonBindings/%s" % (telnyx.__version__,)
        if telnyx.app_info:
            user_agent += " " + self.format_app_info(telnyx.app_info)

        ua = {
            "bindings_version": telnyx.__version__,
            "lang": "python",
            "publisher": "telnyx",
            "httplib": self._client.name,
        }
        for attr, func in [
            ["lang_version", platform.python_version],
            ["platform", platform.platform],
            ["uname", lambda: " ".join(platform.uname())],
        ]:
            try:
                val = func()
            except Exception as e:
                val = "!! %s" % (e,)
            ua[attr] = val
        if telnyx.app_info:
            ua["application"] = telnyx.app_info

        headers = {
            "X-Telnyx-Client-User-Agent": json.dumps(ua),
            "User-Agent": user_agent,
            "Authorization": "Bearer %s" % (api_key,),
        }

        if (
            method == "post"
            or method == "patch"
            and headers.get("Content-Type") is None
        ):
            headers["Content-Type"] = "application/json"

        return headers

    def request_raw(self, method, url, params=None, supplied_headers=None):
        """
        Mechanism for issuing an API call
        """

        if self.api_key:
            my_api_key = self.api_key
        else:
            from telnyx import api_key

            my_api_key = api_key

        if supplied_headers is None:
            supplied_headers = {}

        if my_api_key is None:
            raise error.AuthenticationError(
                "No API key provided. (HINT: set your API key using "
                '"telnyx.api_key = <API-KEY>"). You can generate API keys '
                "from the Telnyx web interface.  See https://developers.telnyx.com/docs/v2/development/authentication "
                "for details, or email support@telnyx.com if you have any "
                "questions."
            )

        abs_url = "%s%s" % (self.api_base, url)

        if method == "get" or method == "head" or method == "delete":
            encoded_params = self.build_query_params(params)
            if params:
                abs_url = _build_api_url(abs_url, encoded_params)
            post_data = None
        elif method == "post" or method == "patch" or method == "put":
            if (
                supplied_headers.get("Content-Type", "application/json")
                == "application/json"
            ):
                encoded_params = json.dumps(params or {})
                post_data = encoded_params
            elif supplied_headers.get("Content-Type", None) == "multipart/form-data":
                generator = MultipartDataGenerator()
                generator.add_params(params or {})
                post_data = generator.get_post_data()
                encoded_params = params
                supplied_headers[
                    "Content-Type"
                ] = "multipart/form-data; boundary=%s" % (generator.boundary,)
        else:
            raise error.APIConnectionError(
                "Unrecognized HTTP method %r.  This may indicate a bug in the "
                "Telnyx bindings.  Please contact support@telnyx.com for "
                "assistance." % (method,)
            )

        headers = self.request_headers(my_api_key, method)
        if supplied_headers is not None:
            for key, value in six.iteritems(supplied_headers):
                headers[key] = value

        util.log_info("Request to Telnyx api", method=method, path=abs_url)
        util.log_debug("Post details", post_data=encoded_params)

        rbody, rcode, rheaders = self._client.request_with_retries(
            method, abs_url, headers, post_data
        )

        util.log_info("Telnyx API response", path=abs_url, response_code=rcode)
        util.log_debug("API response body", body=rbody)

        return rbody, rcode, rheaders, my_api_key

    def build_query_params(self, params):
        encoded_params = urlencode(list(_api_encode(params or {})))

        # Don't use strict form encoding by changing the square bracket control
        # characters back to their literals. This is fine by the server, and
        # makes these parameter strings easier to read.
        encoded_params = encoded_params.replace("%5B", "[").replace("%5D", "]")
        return encoded_params

    def interpret_response(self, rbody, rcode, rheaders):
        try:
            if hasattr(rbody, "decode"):
                rbody = rbody.decode("utf-8")
            resp = TelnyxResponse(rbody, rcode, rheaders)
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody,
                rcode,
                rheaders,
            )
        if not (200 <= rcode < 300):
            self.handle_error_response(rbody, rcode, resp.data, rheaders)

        return resp
