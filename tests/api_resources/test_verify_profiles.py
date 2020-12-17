import telnyx

TEST_RESOURCE_ID = "123"


class TestVerifyProfile(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.VerifyProfile.list()
        request_mock.assert_requested("get", "/v2/verify_profiles")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.VerifyProfile)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.VerifyProfile.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/verify_profiles/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.VerifyProfile)

    def test_is_saveable(self, request_mock):
        resource = telnyx.VerifyProfile.create(name="Hi there")
        request_mock.assert_requested("post", "/v2/verify_profiles")
        assert isinstance(resource, telnyx.VerifyProfile)
        assert resource is resource

    def test_is_modifiable(self, request_mock):
        _ = telnyx.VerifyProfile.modify(TEST_RESOURCE_ID, name="hi there")
        request_mock.assert_requested(
            "patch", "/v2/verify_profiles/%s" % TEST_RESOURCE_ID
        )
