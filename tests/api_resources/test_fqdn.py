from __future__ import absolute_import, division, print_function

import pytest
import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


class TestFQDN(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.FQDN.list()
        request_mock.assert_requested("get", "/v2/fqdns")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.FQDN)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.FQDN.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/fqdns/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.FQDN)

    def test_is_creatable(self, request_mock):
        resource = telnyx.FQDN.create(
            fqdn="example.com", dns_record_type="a", connection_id="1123"
        )
        request_mock.assert_requested("post", "/v2/fqdns")
        assert isinstance(resource, telnyx.FQDN)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_saveable(self, request_mock):
        fqdn = telnyx.FQDN.retrieve(TEST_RESOURCE_ID)
        fqdn.fqdn = "new-example.com"
        resource = fqdn.save()
        request_mock.assert_requested("patch", "/v2/fqdns/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.FQDN)
        assert resource is fqdn

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.FQDN.modify(TEST_RESOURCE_ID, fqdn="new-example.com")
        request_mock.assert_requested("patch", "/v2/fqdns/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.FQDN)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_deletable(self, request_mock):
        resource = telnyx.FQDN.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested("delete", "/v2/fqdns/%s" % TEST_RESOURCE_ID)
