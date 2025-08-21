# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CallControlApplicationListResponse,
    CallControlApplicationCreateResponse,
    CallControlApplicationDeleteResponse,
    CallControlApplicationUpdateResponse,
    CallControlApplicationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallControlApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override='"Latency"',
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            redact_dtmf_debug_logging=True,
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.call_control_applications.with_raw_response.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = response.parse()
        assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.call_control_applications.with_streaming_response.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = response.parse()
            assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.retrieve(
            "id",
        )
        assert_matches_type(CallControlApplicationRetrieveResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.call_control_applications.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = response.parse()
        assert_matches_type(CallControlApplicationRetrieveResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.call_control_applications.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = response.parse()
            assert_matches_type(CallControlApplicationRetrieveResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.call_control_applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override='"Latency"',
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            redact_dtmf_debug_logging=True,
            tags=["tag1", "tag2"],
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.call_control_applications.with_raw_response.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = response.parse()
        assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.call_control_applications.with_streaming_response.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = response.parse()
            assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.call_control_applications.with_raw_response.update(
                id="",
                application_name="call-router",
                webhook_event_url="https://example.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.list()
        assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.list(
            filter={
                "application_name": {"contains": "contains"},
                "application_session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "connection_id": "connection_id",
                "failed": False,
                "from": "+12025550142",
                "leg_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "occurred_at": {
                    "eq": "2019-03-29T11:10:00Z",
                    "gt": "2019-03-29T11:10:00Z",
                    "gte": "2019-03-29T11:10:00Z",
                    "lt": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "outbound_outbound_voice_profile_id": "outbound.outbound_voice_profile_id",
                "product": "texml",
                "status": "init",
                "to": "+12025550142",
                "type": "webhook",
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.call_control_applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = response.parse()
        assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.call_control_applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = response.parse()
            assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        call_control_application = client.call_control_applications.delete(
            "id",
        )
        assert_matches_type(CallControlApplicationDeleteResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.call_control_applications.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = response.parse()
        assert_matches_type(CallControlApplicationDeleteResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.call_control_applications.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = response.parse()
            assert_matches_type(CallControlApplicationDeleteResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.call_control_applications.with_raw_response.delete(
                "",
            )


class TestAsyncCallControlApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override='"Latency"',
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            redact_dtmf_debug_logging=True,
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_control_applications.with_raw_response.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = await response.parse()
        assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_control_applications.with_streaming_response.create(
            application_name="call-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = await response.parse()
            assert_matches_type(CallControlApplicationCreateResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.retrieve(
            "id",
        )
        assert_matches_type(CallControlApplicationRetrieveResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_control_applications.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = await response.parse()
        assert_matches_type(CallControlApplicationRetrieveResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_control_applications.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = await response.parse()
            assert_matches_type(CallControlApplicationRetrieveResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.call_control_applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override='"Latency"',
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            redact_dtmf_debug_logging=True,
            tags=["tag1", "tag2"],
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_control_applications.with_raw_response.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = await response.parse()
        assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_control_applications.with_streaming_response.update(
            id="id",
            application_name="call-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = await response.parse()
            assert_matches_type(CallControlApplicationUpdateResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.call_control_applications.with_raw_response.update(
                id="",
                application_name="call-router",
                webhook_event_url="https://example.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.list()
        assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.list(
            filter={
                "application_name": {"contains": "contains"},
                "application_session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "connection_id": "connection_id",
                "failed": False,
                "from": "+12025550142",
                "leg_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "occurred_at": {
                    "eq": "2019-03-29T11:10:00Z",
                    "gt": "2019-03-29T11:10:00Z",
                    "gte": "2019-03-29T11:10:00Z",
                    "lt": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "outbound_outbound_voice_profile_id": "outbound.outbound_voice_profile_id",
                "product": "texml",
                "status": "init",
                "to": "+12025550142",
                "type": "webhook",
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_control_applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = await response.parse()
        assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_control_applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = await response.parse()
            assert_matches_type(CallControlApplicationListResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        call_control_application = await async_client.call_control_applications.delete(
            "id",
        )
        assert_matches_type(CallControlApplicationDeleteResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_control_applications.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_control_application = await response.parse()
        assert_matches_type(CallControlApplicationDeleteResponse, call_control_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_control_applications.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_control_application = await response.parse()
            assert_matches_type(CallControlApplicationDeleteResponse, call_control_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.call_control_applications.with_raw_response.delete(
                "",
            )
