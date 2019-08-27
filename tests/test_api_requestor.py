from __future__ import absolute_import, division, print_function

import datetime
import json
import tempfile
import uuid

import pytest

import telnyx
from telnyx import six
from telnyx.six.moves.urllib.parse import urlsplit
from telnyx.telnyx_response import TelnyxResponse

VALID_API_METHODS = ("get", "post", "delete")


class GMT1(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1)

    def dst(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "Europe/Prague"


class APIHeaderMatcher(object):
    EXP_KEYS = ["Authorization", "User-Agent", "X-Telnyx-Client-User-Agent"]
    METHOD_EXTRA_KEYS = {"post": ["Content-Type"]}

    def __init__(
        self,
        api_key=None,
        extra={},
        request_method=None,
        user_agent=None,
        app_info=None,
    ):
        self.request_method = request_method
        self.api_key = api_key or telnyx.api_key
        self.extra = extra
        self.user_agent = user_agent
        self.app_info = app_info

    def __eq__(self, other):
        return (
            self._keys_match(other)
            and self._auth_match(other)
            and self._user_agent_match(other)
            and self._x_telnyx_ua_contains_app_info(other)
            and self._extra_match(other)
        )

    def __repr__(self):
        return (
            "APIHeaderMatcher(request_method=%s, api_key=%s, extra=%s, "
            "user_agent=%s, app_info=%s)"
            % (
                repr(self.request_method),
                repr(self.api_key),
                repr(self.extra),
                repr(self.user_agent),
                repr(self.app_info),
            )
        )

    def _keys_match(self, other):
        expected_keys = list(set(self.EXP_KEYS + list(self.extra.keys())))
        if (
            self.request_method is not None
            and self.request_method in self.METHOD_EXTRA_KEYS
        ):
            expected_keys.extend(self.METHOD_EXTRA_KEYS[self.request_method])
        return sorted(other.keys()) == sorted(expected_keys)

    def _auth_match(self, other):
        return other["Authorization"] == "Bearer %s" % (self.api_key,)

    def _user_agent_match(self, other):
        if self.user_agent is not None:
            return other["User-Agent"] == self.user_agent

        return True

    def _x_telnyx_ua_contains_app_info(self, other):
        if self.app_info:
            ua = json.loads(other["X-Telnyx-Client-User-Agent"])
            if "application" not in ua:
                return False
            return ua["application"] == self.app_info

        return True

    def _extra_match(self, other):
        for k, v in six.iteritems(self.extra):
            if other[k] != v:
                return False

        return True


class QueryMatcher(object):
    def __init__(self, expected):
        self.expected = sorted(expected)

    def __eq__(self, other):
        query = urlsplit(other).query or other

        parsed = telnyx.util.parse_qsl(query)
        return self.expected == sorted(parsed)

    def __repr__(self):
        return "QueryMatcher(expected=%s)" % (repr(self.expected))


class UrlMatcher(object):
    def __init__(self, expected):
        self.exp_parts = urlsplit(expected)

    def __eq__(self, other):
        other_parts = urlsplit(other)

        for part in ("scheme", "netloc", "path", "fragment"):
            expected = getattr(self.exp_parts, part)
            actual = getattr(other_parts, part)
            if expected != actual:
                print('Expected %s "%s" but got "%s"' % (part, expected, actual))
                return False

        q_matcher = QueryMatcher(telnyx.util.parse_qsl(self.exp_parts.query))
        return q_matcher == other

    def __repr__(self):
        return "UrlMatcher(exp_parts=%s)" % (repr(self.exp_parts))


class AnyUUID4Matcher(object):
    def __eq__(self, other):
        try:
            uuid.UUID(other, version=4)
        except ValueError:
            return False
        return True

    def __repr__(self):
        return "AnyUUID4Matcher()"


class TestAPIRequestor(object):
    ENCODE_INPUTS = {
        "dict": {
            "astring": "bar",
            "anint": 5,
            "anull": None,
            "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()),
            "atuple": (1, 2),
            "adict": {"foo": "bar", "boz": 5},
            "alist": ["foo", "bar"],
        },
        "list": [1, "foo", "baz"],
        "string": "boo",
        "unicode": u"\u1234",
        "datetime": datetime.datetime(2013, 1, 1, second=1, tzinfo=GMT1()),
        "none": None,
    }

    ENCODE_EXPECTATIONS = {
        "dict": [
            ("%s[astring]", "bar"),
            ("%s[anint]", 5),
            ("%s[adatetime]", 1356994800),
            ("%s[adict][foo]", "bar"),
            ("%s[adict][boz]", 5),
            ("%s[alist][]", "foo"),
            ("%s[alist][]", "bar"),
            ("%s[atuple][]", 1),
            ("%s[atuple][]", 2),
        ],
        "list": [("%s[]", 1), ("%s[]", "foo"), ("%s[]", "baz")],
        "string": [("%s", "boo")],
        "unicode": [("%s", telnyx.util.utf8(u"\u1234"))],
        "datetime": [("%s", 1356994801)],
        "none": [],
    }

    @pytest.fixture(autouse=True)
    def setup_telnyx(self):
        orig_attrs = {"api_key": telnyx.api_key}
        telnyx.api_key = "KEY123"
        yield
        telnyx.api_key = orig_attrs["api_key"]

    @pytest.fixture
    def http_client(self, mocker):
        http_client = mocker.Mock(telnyx.http_client.HTTPClient)
        http_client._verify_ssl_certs = True
        http_client.name = "mockclient"
        return http_client

    @pytest.fixture
    def requestor(self, http_client):
        requestor = telnyx.api_requestor.APIRequestor(client=http_client)
        return requestor

    @pytest.fixture
    def mock_response(self, mocker, http_client):
        def mock_response(return_body, return_code, headers=None):
            http_client.request_with_retries = mocker.Mock(
                return_value=(return_body, return_code, headers or {})
            )

        return mock_response

    @pytest.fixture
    def check_call(self, http_client):
        def check_call(method, abs_url=None, headers=None, post_data=None):
            if not abs_url:
                abs_url = "%s%s" % (telnyx.api_base, self.valid_path)
            if not headers:
                headers = APIHeaderMatcher(request_method=method)

            http_client.request_with_retries.assert_called_with(
                method, abs_url, headers, post_data
            )

        return check_call

    @property
    def valid_path(self):
        return "/foo"

    def encoder_check(self, key):
        stk_key = "my%s" % (key,)

        value = self.ENCODE_INPUTS[key]
        expectation = [(k % (stk_key,), v) for k, v in self.ENCODE_EXPECTATIONS[key]]

        stk = []
        fn = getattr(telnyx.api_requestor.APIRequestor, "encode_%s" % (key,))
        fn(stk, stk_key, value)

        if isinstance(value, dict):
            expectation.sort()
            stk.sort()

        assert stk == expectation, stk

    def _test_encode_naive_datetime(self):
        stk = []

        telnyx.api_requestor.APIRequestor.encode_datetime(
            stk, "test", datetime.datetime(2013, 1, 1)
        )

        # Naive datetimes will encode differently depending on your system
        # local time.  Since we don't know the local time of your system,
        # we just check that naive encodings are within 24 hours of correct.
        assert abs(stk[0][1] - 1356994800) <= 60 * 60 * 24

    def test_param_encoding(self, requestor, mock_response, check_call):
        mock_response("{}", 200)

        requestor.request("get", "", self.ENCODE_INPUTS)

        expectation = []
        for type_, values in six.iteritems(self.ENCODE_EXPECTATIONS):
            expectation.extend([(k % (type_,), str(v)) for k, v in values])

        check_call("get", QueryMatcher(expectation))

    def test_dictionary_list_encoding(self):
        params = {"foo": {"0": {"bar": "bat"}}}
        encoded = list(telnyx.api_requestor._api_encode(params))
        key, value = encoded[0]

        assert key == "foo[0][bar]"
        assert value == "bat"

    def test_url_construction(self, requestor, mock_response, check_call):
        CASES = (
            ("%s?foo=bar" % telnyx.api_base, "", {"foo": "bar"}),
            ("%s?foo=bar" % telnyx.api_base, "?", {"foo": "bar"}),
            (telnyx.api_base, "", {}),
            (
                "%s/%%20spaced?foo=bar%%24&baz=5" % telnyx.api_base,
                "/%20spaced?foo=bar%24",
                {"baz": "5"},
            ),
            ("%s?foo=bar&foo=bar" % telnyx.api_base, "?foo=bar", {"foo": "bar"}),
        )

        for expected, url, params in CASES:
            mock_response("{}", 200)

            requestor.request("get", url, params)

            check_call("get", expected)

    def test_empty_methods(self, requestor, mock_response, check_call):
        for meth in VALID_API_METHODS:
            mock_response("{}", 200)

            resp, key = requestor.request(meth, self.valid_path, {})

            if meth == "post":
                post_data = "{}"
            else:
                post_data = None

            check_call(meth, post_data=post_data)
            assert isinstance(resp, TelnyxResponse)

            assert resp.data == {}
            assert resp.data == json.loads(resp.body)

    def test_methods_with_params_and_response(
        self, requestor, mock_response, check_call
    ):
        for method in VALID_API_METHODS:
            mock_response('{"foo": "bar", "baz": 6}', 200)

            params = {
                "alist": [1, 2, 3],
                "adict": {"frobble": "bits"},
                "adatetime": datetime.datetime(2013, 1, 1, tzinfo=GMT1()).isoformat(),
            }
            encoded = (
                "adict[frobble]=bits&adatetime=2013-01-01T00%3A00%3A00%2B01%3A00&"
                "alist[]=1&alist[]=2&alist[]=3"
            )

            resp, key = requestor.request(method, self.valid_path, params)
            assert isinstance(resp, TelnyxResponse)

            assert resp.data == {"foo": "bar", "baz": 6}
            assert resp.data == json.loads(resp.body)

            if method == "post" or method == "patch":
                check_call(method, post_data=json.dumps(params))
            else:
                abs_url = "%s%s?%s" % (telnyx.api_base, self.valid_path, encoded)
                check_call(method, abs_url=UrlMatcher(abs_url))

    def test_uses_headers(self, requestor, mock_response, check_call):
        mock_response("{}", 200)
        requestor.request("get", self.valid_path, {}, {"foo": "bar"})
        check_call("get", headers=APIHeaderMatcher(extra={"foo": "bar"}))

    def test_uses_instance_key(self, http_client, mock_response, check_call):
        key = "fookey"
        requestor = telnyx.api_requestor.APIRequestor(key, client=http_client)

        mock_response("{}", 200)

        resp, used_key = requestor.request("get", self.valid_path, {})

        check_call("get", headers=APIHeaderMatcher(key, request_method="get"))
        assert used_key == key

    def test_uses_app_info(self, requestor, mock_response, check_call):
        try:
            old = telnyx.app_info
            telnyx.set_app_info(
                "MyAwesomePlugin", url="https://myawesomeplugin.info", version="1.2.34"
            )

            mock_response("{}", 200)
            requestor.request("get", self.valid_path, {})

            ua = "Telnyx/v2 PythonBindings/%s" % (telnyx.__version__,)
            ua += " MyAwesomePlugin/1.2.34 (https://myawesomeplugin.info)"
            header_matcher = APIHeaderMatcher(
                user_agent=ua,
                app_info={
                    "name": "MyAwesomePlugin",
                    "url": "https://myawesomeplugin.info",
                    "version": "1.2.34",
                },
            )
            check_call("get", headers=header_matcher)
        finally:
            telnyx.app_info = old

    def test_fails_without_api_key(self, requestor):
        telnyx.api_key = None

        with pytest.raises(telnyx.error.AuthenticationError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_request_error_400(self, requestor, mock_response):
        mock_response('{"errors": []}', 400)

        with pytest.raises(telnyx.error.InvalidRequestError):
            requestor.request("get", self.valid_path, {})

    def test_authentication_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 401)

        with pytest.raises(telnyx.error.AuthenticationError):
            requestor.request("get", self.valid_path, {})

    def test_permissions_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 403)

        with pytest.raises(telnyx.error.PermissionError):
            requestor.request("get", self.valid_path, {})

    def test_resource_not_found_error_404(self, requestor, mock_response):
        mock_response('{"errors": []}', 404)

        with pytest.raises(telnyx.error.ResourceNotFoundError):
            requestor.request("get", self.valid_path, {})

    def test_method_not_supported_error_405(self, requestor, mock_response):
        mock_response('{"errors": []}', 405)

        with pytest.raises(telnyx.error.MethodNotSupportedError):
            requestor.request("get", self.valid_path, {})

    def test_timeout_error_408(self, requestor, mock_response):
        mock_response('{"errors": []}', 408)

        with pytest.raises(telnyx.error.TimeoutError):
            requestor.request("get", self.valid_path, {})

    def test_unsupported_media_type_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 415)

        with pytest.raises(telnyx.error.UnsupportedMediaTypeError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_parameters_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 422)

        with pytest.raises(telnyx.error.InvalidParametersError):
            requestor.request("get", self.valid_path, {})

    def test_rate_limit_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 429)

        with pytest.raises(telnyx.error.RateLimitError):
            requestor.request("get", self.valid_path, {})

    def test_server_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 500)

        with pytest.raises(telnyx.error.APIError):
            requestor.request("get", self.valid_path, {})

    def test_service_unavailable_error(self, requestor, mock_response):
        mock_response('{"errors": []}', 503)

        with pytest.raises(telnyx.error.ServiceUnavailableError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_json(self, requestor, mock_response):
        mock_response("{", 200)

        with pytest.raises(telnyx.error.APIError):
            requestor.request("get", self.valid_path, {})

    def test_invalid_method(self, requestor):
        with pytest.raises(telnyx.error.APIConnectionError):
            requestor.request("foo", "bar")

    def test_raw_request_with_file_param(self, requestor, mock_response):
        test_file = tempfile.NamedTemporaryFile()
        test_file.write("\u263A".encode("utf-16"))
        test_file.seek(0)
        params = {"file": test_file, "purpose": "dispute_evidence"}
        supplied_headers = {"Content-Type": "multipart/form-data"}
        mock_response("{}", 200)
        requestor.request("post", "/v2/files", params, supplied_headers)


class TestDefaultClient(object):
    @pytest.fixture(autouse=True)
    def setup_telnyx(self):
        orig_attrs = {
            "api_key": telnyx.api_key,
            "default_http_client": telnyx.default_http_client,
        }
        telnyx.api_key = "KEY123"
        yield
        telnyx.api_key = orig_attrs["api_key"]
        telnyx.default_http_client = orig_attrs["default_http_client"]

    def test_default_http_client_called(self, mocker):
        hc = mocker.Mock(telnyx.http_client.HTTPClient)
        hc._verify_ssl_certs = True
        hc.name = "mockclient"
        hc.request_with_retries = mocker.Mock(return_value=("{}", 200, {}))

        telnyx.default_http_client = hc
        telnyx.MessagingProfile.list()

        hc.request_with_retries.assert_called_with(
            "get", "https://api.telnyx.com/v2/messaging_profiles", mocker.ANY, None
        )
