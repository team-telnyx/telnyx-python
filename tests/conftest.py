from __future__ import absolute_import, division, print_function

import atexit
import os
import sys
from distutils.version import StrictVersion

import pytest

import telnyx
from telnyx.six.moves.urllib.request import urlopen
from telnyx.six.moves.urllib.error import HTTPError

from tests.request_mock import RequestMock
from tests.telnyx_mock import TelnyxMock


# When changing this number, don't forget to change it in `.travis.yml` too.
MOCK_MINIMUM_VERSION = "0.4.0"

# Starts telnyx-mock if an OpenAPI spec override is found in `openapi/`, and
# otherwise fall back to `TELNYX_MOCK_PORT` or 12111.
if TelnyxMock.start():
    MOCK_PORT = TelnyxMock.port()
else:
    MOCK_PORT = os.environ.get("TELNYX_MOCK_PORT", 12111)


@atexit.register
def stop_telnyx_mock():
    TelnyxMock.stop()


try:
    resp = urlopen("http://localhost:%s/" % MOCK_PORT)
    info = resp.info()
except HTTPError as e:
    info = e.info()
except Exception:
    sys.exit(
        "Couldn't reach telnyx-mock at `localhost:%s`. Is "
        "it running? Please see README for setup instructions." % MOCK_PORT
    )

version = info.get("Telnyx-Mock-Version")
if version != "master" and StrictVersion(version) < StrictVersion(MOCK_MINIMUM_VERSION):
    sys.exit(
        "Your version of telnyx-mock (%s) is too old. The minimum "
        "version to run this test suite is %s. Please "
        "see its repository for upgrade instructions." % (version, MOCK_MINIMUM_VERSION)
    )


@pytest.fixture(autouse=True)
def setup_telnyx():
    orig_attrs = {
        "api_base": telnyx.api_base,
        "api_key": telnyx.api_key,
        "default_http_client": telnyx.default_http_client,
    }
    http_client = telnyx.http_client.new_default_http_client()
    telnyx.api_base = "http://localhost:%s" % MOCK_PORT
    telnyx.api_key = "KEY123"
    telnyx.default_http_client = http_client
    yield
    http_client.close()
    telnyx.api_base = orig_attrs["api_base"]
    telnyx.api_key = orig_attrs["api_key"]
    telnyx.default_http_client = orig_attrs["default_http_client"]


@pytest.fixture
def request_mock(mocker):
    return RequestMock(mocker)
