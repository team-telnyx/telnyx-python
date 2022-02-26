from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_FAX_CONNECTION_ID = "0239852093"
TEST_SRC_LONG_CODE = "+13125550100"
TEST_DST = "+17735550100"
TEST_MEDIA_URL = "http://www.africau.edu/images/default/sample.pdf"
TEST_RESOURCE_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestFax(object):
    def test_can_create_standard_fax(self, request_mock):
        resource = telnyx.Fax.create(
            from_=TEST_SRC_LONG_CODE,
            to=TEST_DST,
            media_url=TEST_MEDIA_URL,
            connection_id=TEST_FAX_CONNECTION_ID,
        )
        request_mock.assert_requested("post", "/v2/faxes")
        print(resource)
        print(type(resource))
        assert isinstance(resource, telnyx.Fax)

    @pytest.mark.skip(reason="Fax needs correct input")
    def test_can_fax_refresh(self, request_mock):
        resource = telnyx.Fax.retrieve(TEST_RESOURCE_ID)
        resource.create_refresh(id=TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v2/faxes/%s/actions/refresh" % TEST_RESOURCE_ID
        )
