# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.meeting_sessions import ActionAcceptedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_chat(self, client: Telnyx) -> None:
        action = client.meeting_sessions.actions.send_chat(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="I will send the summary after this call.",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_chat(self, client: Telnyx) -> None:
        response = client.meeting_sessions.actions.with_raw_response.send_chat(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="I will send the summary after this call.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_chat(self, client: Telnyx) -> None:
        with client.meeting_sessions.actions.with_streaming_response.send_chat(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="I will send the summary after this call.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionAcceptedResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_chat(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.actions.with_raw_response.send_chat(
                id="",
                text="I will send the summary after this call.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_speak(self, client: Telnyx) -> None:
        action = client.meeting_sessions.actions.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_speak_with_all_params(self, client: Telnyx) -> None:
        action = client.meeting_sessions.actions.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
            interrupt=False,
            voice="x",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_speak(self, client: Telnyx) -> None:
        response = client.meeting_sessions.actions.with_raw_response.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_speak(self, client: Telnyx) -> None:
        with client.meeting_sessions.actions.with_streaming_response.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionAcceptedResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_speak(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.actions.with_raw_response.speak(
                id="",
                text="Here are the three decisions from this call.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop_speaking(self, client: Telnyx) -> None:
        action = client.meeting_sessions.actions.stop_speaking(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop_speaking(self, client: Telnyx) -> None:
        response = client.meeting_sessions.actions.with_raw_response.stop_speaking(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop_speaking(self, client: Telnyx) -> None:
        with client.meeting_sessions.actions.with_streaming_response.stop_speaking(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionAcceptedResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop_speaking(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.meeting_sessions.actions.with_raw_response.stop_speaking(
                "",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_chat(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.meeting_sessions.actions.send_chat(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="I will send the summary after this call.",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_chat(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.actions.with_raw_response.send_chat(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="I will send the summary after this call.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_chat(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.actions.with_streaming_response.send_chat(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="I will send the summary after this call.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionAcceptedResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_chat(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.actions.with_raw_response.send_chat(
                id="",
                text="I will send the summary after this call.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_speak(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.meeting_sessions.actions.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_speak_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.meeting_sessions.actions.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
            interrupt=False,
            voice="x",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_speak(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.actions.with_raw_response.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_speak(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.actions.with_streaming_response.speak(
            id="mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            text="Here are the three decisions from this call.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionAcceptedResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_speak(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.actions.with_raw_response.speak(
                id="",
                text="Here are the three decisions from this call.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop_speaking(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.meeting_sessions.actions.stop_speaking(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop_speaking(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_sessions.actions.with_raw_response.stop_speaking(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionAcceptedResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop_speaking(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_sessions.actions.with_streaming_response.stop_speaking(
            "mtgsess_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionAcceptedResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop_speaking(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.meeting_sessions.actions.with_raw_response.stop_speaking(
                "",
            )
