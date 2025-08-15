# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.texml.accounts import (
    CallCallsResponse,
    CallUpdateResponse,
    CallRetrieveResponse,
    CallSiprecJsonResponse,
    CallStreamsJsonResponse,
    CallRetrieveCallsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.retrieve(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallRetrieveResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.with_raw_response.retrieve(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallRetrieveResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.with_streaming_response.retrieve(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallRetrieveResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.retrieve(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.retrieve(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.update(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallUpdateResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.update(
            call_sid="call_sid",
            account_sid="account_sid",
            fallback_method="GET",
            fallback_url="https://www.example.com/intruction-c.xml",
            method="GET",
            status="completed",
            status_callback="https://www.example.com/callback",
            status_callback_method="GET",
            texml='<?xml version="1.0" encoding="UTF-8"?><Response><Say>Hello</Say></Response>',
            url="https://www.example.com/intruction-b.xml",
        )
        assert_matches_type(CallUpdateResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.with_raw_response.update(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallUpdateResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.with_streaming_response.update(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallUpdateResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.update(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.update(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_calls(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
        )
        assert_matches_type(CallCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_calls_with_all_params(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
            async_amd=True,
            async_amd_status_callback="https://www.example.com/callback",
            async_amd_status_callback_method="GET",
            caller_id="Info",
            cancel_playback_on_detect_message_end=False,
            cancel_playback_on_machine_detection=False,
            detection_mode="Premium",
            fallback_url="https://www.example.com/instructions-fallback.xml",
            machine_detection="Enable",
            machine_detection_silence_timeout=2000,
            machine_detection_speech_end_threshold=2000,
            machine_detection_speech_threshold=2000,
            machine_detection_timeout=5000,
            preferred_codecs="PCMA,PCMU",
            record=False,
            recording_channels="dual",
            recording_status_callback="https://example.com/recording_status_callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_timeout=5,
            recording_track="inbound",
            send_recording_url=False,
            sip_auth_password="1234",
            sip_auth_username="user",
            status_callback="https://www.example.com/statuscallback-listener",
            status_callback_event="initiated",
            status_callback_method="GET",
            trim="trim-silence",
            url="https://www.example.com/texml.xml",
            url_method="GET",
        )
        assert_matches_type(CallCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_calls(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.with_raw_response.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_calls(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.with_streaming_response.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallCallsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_calls(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.calls(
                account_sid="",
                application_sid="ApplicationSid",
                from_="+13120001234",
                to="+13121230000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_calls(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.retrieve_calls(
            account_sid="account_sid",
        )
        assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_calls_with_all_params(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.retrieve_calls(
            account_sid="account_sid",
            end_time="EndTime",
            end_time_gt="EndTime_gt",
            end_time_lt="EndTime_lt",
            from_="From",
            page=0,
            page_size=0,
            page_token="PageToken",
            start_time="StartTime",
            start_time_gt="StartTime_gt",
            start_time_lt="StartTime_lt",
            status="canceled",
            to="To",
        )
        assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_calls(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.with_raw_response.retrieve_calls(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_calls(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.with_streaming_response.retrieve_calls(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_calls(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.retrieve_calls(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_siprec_json(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_siprec_json_with_all_params(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
            connector_name="my_connector",
            include_metadata_custom_headers=True,
            name="my_siprec_session",
            secure=True,
            session_timeout_secs=900,
            sip_transport="tcp",
            status_callback="https://www.example.com/callback",
            status_callback_method="GET",
            track="both_tracks",
        )
        assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_siprec_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.with_raw_response.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_siprec_json(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.with_streaming_response.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_siprec_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.siprec_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.siprec_json(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_streams_json(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_streams_json_with_all_params(self, client: Telnyx) -> None:
        call = client.texml.accounts.calls.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
            bidirectional_codec="G722",
            bidirectional_mode="rtp",
            name="My stream",
            status_callback="http://webhook.com/callback",
            status_callback_method="GET",
            track="both_tracks",
            url="wss://www.example.com/websocket",
        )
        assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_streams_json(self, client: Telnyx) -> None:
        response = client.texml.accounts.calls.with_raw_response.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_streams_json(self, client: Telnyx) -> None:
        with client.texml.accounts.calls.with_streaming_response.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_streams_json(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.streams_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            client.texml.accounts.calls.with_raw_response.streams_json(
                call_sid="",
                account_sid="account_sid",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.retrieve(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallRetrieveResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.with_raw_response.retrieve(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallRetrieveResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.with_streaming_response.retrieve(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallRetrieveResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.retrieve(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.retrieve(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.update(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallUpdateResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.update(
            call_sid="call_sid",
            account_sid="account_sid",
            fallback_method="GET",
            fallback_url="https://www.example.com/intruction-c.xml",
            method="GET",
            status="completed",
            status_callback="https://www.example.com/callback",
            status_callback_method="GET",
            texml='<?xml version="1.0" encoding="UTF-8"?><Response><Say>Hello</Say></Response>',
            url="https://www.example.com/intruction-b.xml",
        )
        assert_matches_type(CallUpdateResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.with_raw_response.update(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallUpdateResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.with_streaming_response.update(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallUpdateResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.update(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.update(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_calls(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
        )
        assert_matches_type(CallCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_calls_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
            async_amd=True,
            async_amd_status_callback="https://www.example.com/callback",
            async_amd_status_callback_method="GET",
            caller_id="Info",
            cancel_playback_on_detect_message_end=False,
            cancel_playback_on_machine_detection=False,
            detection_mode="Premium",
            fallback_url="https://www.example.com/instructions-fallback.xml",
            machine_detection="Enable",
            machine_detection_silence_timeout=2000,
            machine_detection_speech_end_threshold=2000,
            machine_detection_speech_threshold=2000,
            machine_detection_timeout=5000,
            preferred_codecs="PCMA,PCMU",
            record=False,
            recording_channels="dual",
            recording_status_callback="https://example.com/recording_status_callback",
            recording_status_callback_event="in-progress completed absent",
            recording_status_callback_method="GET",
            recording_timeout=5,
            recording_track="inbound",
            send_recording_url=False,
            sip_auth_password="1234",
            sip_auth_username="user",
            status_callback="https://www.example.com/statuscallback-listener",
            status_callback_event="initiated",
            status_callback_method="GET",
            trim="trim-silence",
            url="https://www.example.com/texml.xml",
            url_method="GET",
        )
        assert_matches_type(CallCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_calls(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.with_raw_response.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_calls(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.with_streaming_response.calls(
            account_sid="account_sid",
            application_sid="ApplicationSid",
            from_="+13120001234",
            to="+13121230000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallCallsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_calls(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.calls(
                account_sid="",
                application_sid="ApplicationSid",
                from_="+13120001234",
                to="+13121230000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_calls(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.retrieve_calls(
            account_sid="account_sid",
        )
        assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_calls_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.retrieve_calls(
            account_sid="account_sid",
            end_time="EndTime",
            end_time_gt="EndTime_gt",
            end_time_lt="EndTime_lt",
            from_="From",
            page=0,
            page_size=0,
            page_token="PageToken",
            start_time="StartTime",
            start_time_gt="StartTime_gt",
            start_time_lt="StartTime_lt",
            status="canceled",
            to="To",
        )
        assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_calls(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.with_raw_response.retrieve_calls(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_calls(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.with_streaming_response.retrieve_calls(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallRetrieveCallsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_calls(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.retrieve_calls(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_siprec_json(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_siprec_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
            connector_name="my_connector",
            include_metadata_custom_headers=True,
            name="my_siprec_session",
            secure=True,
            session_timeout_secs=900,
            sip_transport="tcp",
            status_callback="https://www.example.com/callback",
            status_callback_method="GET",
            track="both_tracks",
        )
        assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_siprec_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.with_raw_response.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_siprec_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.with_streaming_response.siprec_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallSiprecJsonResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_siprec_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.siprec_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.siprec_json(
                call_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_streams_json(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )
        assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_streams_json_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call = await async_client.texml.accounts.calls.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
            bidirectional_codec="G722",
            bidirectional_mode="rtp",
            name="My stream",
            status_callback="http://webhook.com/callback",
            status_callback_method="GET",
            track="both_tracks",
            url="wss://www.example.com/websocket",
        )
        assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_streams_json(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.calls.with_raw_response.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_streams_json(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.calls.with_streaming_response.streams_json(
            call_sid="call_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallStreamsJsonResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_streams_json(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.streams_json(
                call_sid="call_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_sid` but received ''"):
            await async_client.texml.accounts.calls.with_raw_response.streams_json(
                call_sid="",
                account_sid="account_sid",
            )
