from __future__ import absolute_import, division, print_function

import telnyx

TEST_RECORDING_ID = "5e820ca7-a7c9-4724-b7f0-6ac5ac54e5c6"


class TestRecording(object):
    def test_is_listable(self, request_mock):
        """Test that recordings can be listed"""
        request_mock.stub_request(
            "get",
            "/v2/recordings",
            {
                "data": [
                    {
                        "record_type": "recording",
                        "id": TEST_RECORDING_ID,
                        "call_control_id": "v3:MjM0ODE4OC01YzUxLTQ4N2YtOGM3MC0yNzQ2OWFhNzg2YjU",
                        "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                        "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1", 
                        "status": "completed",
                        "channels": "single",
                        "source": "conference",
                        "download_url": "https://example.com/recording.mp3",
                        "duration_millis": 5000,
                        "created_at": "2018-02-02T22:25:27.521992Z",
                        "updated_at": "2018-02-02T22:25:27.521992Z"
                    }
                ]
            },
            rheaders={"request-id": "req_id"},
        )

        recordings = telnyx.Recording.list()
        request_mock.assert_requested("get", "/v2/recordings", {})
        assert len(recordings.data) == 1
        assert isinstance(recordings.data[0], telnyx.Recording)
        assert recordings.data[0].id == TEST_RECORDING_ID
        assert recordings.data[0].record_type == "recording"
        assert recordings.data[0].status == "completed"

    def test_is_listable_with_params(self, request_mock):
        """Test that recordings can be listed with filter parameters"""
        request_mock.stub_request(
            "get",
            "/v2/recordings",
            {
                "data": [],
                "meta": {
                    "total_pages": 1,
                    "total_results": 0,
                    "page_number": 1,
                    "page_size": 20
                }
            }
        )

        telnyx.Recording.list(
            filter={
                "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
                "status": "completed"
            },
            page={"size": 10}
        )
        
        request_mock.assert_requested(
            "get", 
            "/v2/recordings", 
            {
                "filter[call_session_id]": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
                "filter[status]": "completed",
                "page[size]": 10
            }
        )

    def test_is_retrievable(self, request_mock):
        """Test that individual recordings can be retrieved"""
        request_mock.stub_request(
            "get",
            "/v2/recordings/%s" % TEST_RECORDING_ID,
            {
                "data": {
                    "record_type": "recording",
                    "id": TEST_RECORDING_ID,
                    "call_control_id": "v3:MjM0ODE4OC01YzUxLTQ4N2YtOGM3MC0yNzQ2OWFhNzg2YjU",
                    "status": "completed",
                    "channels": "single",
                    "source": "conference",
                    "download_url": "https://example.com/recording.mp3",
                    "duration_millis": 5000,
                    "created_at": "2018-02-02T22:25:27.521992Z",
                    "updated_at": "2018-02-02T22:25:27.521992Z"
                }
            }
        )

        recording = telnyx.Recording.retrieve(TEST_RECORDING_ID)
        request_mock.assert_requested("get", "/v2/recordings/%s" % TEST_RECORDING_ID)
        assert isinstance(recording, telnyx.Recording)
        assert recording.id == TEST_RECORDING_ID

    def test_is_deletable(self, request_mock):
        """Test that recordings can be deleted"""
        recording = telnyx.Recording.construct_from(
            {
                "id": TEST_RECORDING_ID,
                "record_type": "recording",
                "status": "completed"
            },
            None
        )

        request_mock.stub_request(
            "delete",
            "/v2/recordings/%s/actions/delete" % TEST_RECORDING_ID,
            {
                "data": {
                    "record_type": "recording",
                    "id": TEST_RECORDING_ID,
                    "status": "deleted"
                }
            }
        )

        recording.delete()
        request_mock.assert_requested(
            "delete", "/v2/recordings/%s/actions/delete" % TEST_RECORDING_ID
        )

    def test_can_delete_class_method(self, request_mock):
        """Test that recordings can be deleted using class method"""
        request_mock.stub_request(
            "delete",
            "/v2/recordings/%s/actions/delete" % TEST_RECORDING_ID,
            {
                "data": {
                    "record_type": "recording", 
                    "id": TEST_RECORDING_ID,
                    "status": "deleted"
                }
            }
        )

        # The nested_resource_class_methods decorator requires both id and nested_id
        result = telnyx.Recording.delete_delete(TEST_RECORDING_ID, nested_id=None)
        request_mock.assert_requested(
            "delete", "/v2/recordings/%s/actions/delete" % TEST_RECORDING_ID
        )
        assert isinstance(result, telnyx.Recording)

    def test_does_not_have_create_method(self):
        """Test that create method is not available (not supported by API)"""
        assert not hasattr(telnyx.Recording, 'create'), "Recording should not have create method"

    def test_does_not_have_save_method(self):
        """Test that save method is not available (not supported by API)"""
        recording = telnyx.Recording.construct_from(
            {"id": TEST_RECORDING_ID, "record_type": "recording"},
            None
        )
        assert not hasattr(recording, 'save'), "Recording should not have save method"

    def test_class_url(self):
        """Test that the class generates the correct URL"""
        assert telnyx.Recording.class_url() == "/v2/recordings"

    def test_object_name(self):
        """Test that the OBJECT_NAME is correct"""
        assert telnyx.Recording.OBJECT_NAME == "recording"