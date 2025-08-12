# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.rooms.sessions import (
    ActionEndResponse,
    ActionKickResponse,
    ActionMuteResponse,
    ActionUnmuteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_end(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.end(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionEndResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_end(self, client: Telnyx) -> None:
        response = client.rooms.sessions.actions.with_raw_response.end(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionEndResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_end(self, client: Telnyx) -> None:
        with client.rooms.sessions.actions.with_streaming_response.end(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionEndResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_end(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            client.rooms.sessions.actions.with_raw_response.end(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_kick(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionKickResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_kick_with_all_params(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            exclude=["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
            participants="all",
        )
        assert_matches_type(ActionKickResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_kick(self, client: Telnyx) -> None:
        response = client.rooms.sessions.actions.with_raw_response.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionKickResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_kick(self, client: Telnyx) -> None:
        with client.rooms.sessions.actions.with_streaming_response.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionKickResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_kick(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            client.rooms.sessions.actions.with_raw_response.kick(
                room_session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mute(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mute_with_all_params(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            exclude=["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
            participants="all",
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mute(self, client: Telnyx) -> None:
        response = client.rooms.sessions.actions.with_raw_response.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mute(self, client: Telnyx) -> None:
        with client.rooms.sessions.actions.with_streaming_response.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionMuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_mute(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            client.rooms.sessions.actions.with_raw_response.mute(
                room_session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unmute(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unmute_with_all_params(self, client: Telnyx) -> None:
        action = client.rooms.sessions.actions.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            exclude=["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
            participants="all",
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unmute(self, client: Telnyx) -> None:
        response = client.rooms.sessions.actions.with_raw_response.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unmute(self, client: Telnyx) -> None:
        with client.rooms.sessions.actions.with_streaming_response.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionUnmuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unmute(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            client.rooms.sessions.actions.with_raw_response.unmute(
                room_session_id="",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_end(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.end(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionEndResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_end(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.actions.with_raw_response.end(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionEndResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_end(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.actions.with_streaming_response.end(
            "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionEndResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_end(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            await async_client.rooms.sessions.actions.with_raw_response.end(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_kick(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionKickResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_kick_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            exclude=["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
            participants="all",
        )
        assert_matches_type(ActionKickResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_kick(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.actions.with_raw_response.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionKickResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_kick(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.actions.with_streaming_response.kick(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionKickResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_kick(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            await async_client.rooms.sessions.actions.with_raw_response.kick(
                room_session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mute(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mute_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            exclude=["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
            participants="all",
        )
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mute(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.actions.with_raw_response.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionMuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mute(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.actions.with_streaming_response.mute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionMuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_mute(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            await async_client.rooms.sessions.actions.with_raw_response.mute(
                room_session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unmute(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unmute_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.rooms.sessions.actions.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
            exclude=["7b61621f-62e0-4aad-ab11-9fd19e272e73"],
            participants="all",
        )
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unmute(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rooms.sessions.actions.with_raw_response.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionUnmuteResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unmute(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rooms.sessions.actions.with_streaming_response.unmute(
            room_session_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionUnmuteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unmute(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_session_id` but received ''"):
            await async_client.rooms.sessions.actions.with_raw_response.unmute(
                room_session_id="",
            )
