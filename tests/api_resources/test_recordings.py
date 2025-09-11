# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    RecordingListResponse,
    RecordingDeleteResponse,
    RecordingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        recording = client.recordings.retrieve(
            "recording_id",
        )
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.recordings.with_raw_response.retrieve(
            "recording_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.recordings.with_streaming_response.retrieve(
            "recording_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.recordings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        recording = client.recordings.list()
        assert_matches_type(RecordingListResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        recording = client.recordings.list(
            filter={
                "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                "call_session_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                "conference_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                "connection_id": "175237942907135762",
                "created_at": {
                    "gte": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "from": "1234567890",
                "to": "1234567890",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RecordingListResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.recordings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingListResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.recordings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingListResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        recording = client.recordings.delete(
            "recording_id",
        )
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.recordings.with_raw_response.delete(
            "recording_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.recordings.with_streaming_response.delete(
            "recording_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.recordings.with_raw_response.delete(
                "",
            )


class TestAsyncRecordings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        recording = await async_client.recordings.retrieve(
            "recording_id",
        )
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.recordings.with_raw_response.retrieve(
            "recording_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.recordings.with_streaming_response.retrieve(
            "recording_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingRetrieveResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.recordings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        recording = await async_client.recordings.list()
        assert_matches_type(RecordingListResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        recording = await async_client.recordings.list(
            filter={
                "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                "call_session_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                "conference_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
                "connection_id": "175237942907135762",
                "created_at": {
                    "gte": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "from": "1234567890",
                "to": "1234567890",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RecordingListResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.recordings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingListResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.recordings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingListResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        recording = await async_client.recordings.delete(
            "recording_id",
        )
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.recordings.with_raw_response.delete(
            "recording_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.recordings.with_streaming_response.delete(
            "recording_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingDeleteResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.recordings.with_raw_response.delete(
                "",
            )
