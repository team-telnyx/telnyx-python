# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.meeting_sessions import ArtifactListResponse, MeetingSessionArtifactResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        artifact = client.meeting_sessions.artifacts.create(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            type="summary",
        )
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.meeting_sessions.artifacts.with_raw_response.create(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            type="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.meeting_sessions.artifacts.with_streaming_response.create(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            type="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.artifacts.with_raw_response.create(
                id="",
                type="summary",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        artifact = client.meeting_sessions.artifacts.retrieve(
            artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.meeting_sessions.artifacts.with_raw_response.retrieve(
            artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.meeting_sessions.artifacts.with_streaming_response.retrieve(
            artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.artifacts.with_raw_response.retrieve(
                artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.meeting_sessions.artifacts.with_raw_response.retrieve(
                artifact_id="",
                id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        artifact = client.meeting_sessions.artifacts.list(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.meeting_sessions.artifacts.with_raw_response.list(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.meeting_sessions.artifacts.with_streaming_response.list(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(ArtifactListResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.artifacts.with_raw_response.list(
                "",
            )


class TestAsyncArtifacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        artifact = await async_client.meeting_sessions.artifacts.create(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            type="summary",
        )
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.artifacts.with_raw_response.create(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            type="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.artifacts.with_streaming_response.create(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            type="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.artifacts.with_raw_response.create(
                id="",
                type="summary",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        artifact = await async_client.meeting_sessions.artifacts.retrieve(
            artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.artifacts.with_raw_response.retrieve(
            artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.artifacts.with_streaming_response.retrieve(
            artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(MeetingSessionArtifactResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.artifacts.with_raw_response.retrieve(
                artifact_id="mtgart_b2c3d4e5-f6a7-8901-bcde-f23456789012",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.meeting_sessions.artifacts.with_raw_response.retrieve(
                artifact_id="",
                id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        artifact = await async_client.meeting_sessions.artifacts.list(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.artifacts.with_raw_response.list(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(ArtifactListResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.artifacts.with_streaming_response.list(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(ArtifactListResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.artifacts.with_raw_response.list(
                "",
            )
