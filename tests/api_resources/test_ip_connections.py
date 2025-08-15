# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    IPConnectionListResponse,
    IPConnectionCreateResponse,
    IPConnectionDeleteResponse,
    IPConnectionUpdateResponse,
    IPConnectionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.create()
        assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.create(
            active=True,
            anchorsite_override="Latency",
            android_push_credential_id="06b09dfd-7154-4980-8b75-cebf7a9d4f8e",
            connection_name="string",
            default_on_hold_comfort_noise_enabled=True,
            dtmf_type="RFC 2833",
            encode_contact_header_enabled=True,
            encrypted_media="SRTP",
            inbound={
                "ani_number_format": "+E.164",
                "channel_limit": 10,
                "codecs": ["string"],
                "default_routing_method": "sequential",
                "dnis_number_format": "+e164",
                "generate_ringback_tone": True,
                "isup_headers_enabled": True,
                "prack_enabled": True,
                "shaken_stir_enabled": True,
                "sip_compact_headers_enabled": True,
                "sip_region": "US",
                "sip_subdomain": "test",
                "sip_subdomain_receive_settings": "only_my_connections",
                "timeout_1xx_secs": 10,
                "timeout_2xx_secs": 20,
            },
            ios_push_credential_id="ec0c8e5d-439e-4620-a0c1-9d9c8d02a836",
            onnet_t38_passthrough_enabled=False,
            outbound={
                "ani_override": "string",
                "ani_override_type": "always",
                "call_parking_enabled": True,
                "channel_limit": 10,
                "generate_ringback_tone": True,
                "instant_ringback_enabled": True,
                "ip_authentication_method": "token",
                "ip_authentication_token": "string",
                "localization": "string",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
                "t38_reinvite_source": "customer",
                "tech_prefix": "string",
            },
            rtcp_settings={
                "capture_enabled": True,
                "port": "rtcp-mux",
                "report_frequency_secs": 10,
            },
            tags=["tag1", "tag2"],
            transport_protocol="UDP",
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ip_connections.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = response.parse()
        assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ip_connections.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = response.parse()
            assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.retrieve(
            "id",
        )
        assert_matches_type(IPConnectionRetrieveResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ip_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = response.parse()
        assert_matches_type(IPConnectionRetrieveResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ip_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = response.parse()
            assert_matches_type(IPConnectionRetrieveResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ip_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.update(
            id="id",
        )
        assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.update(
            id="id",
            active=True,
            anchorsite_override="Latency",
            android_push_credential_id="06b09dfd-7154-4980-8b75-cebf7a9d4f8e",
            connection_name="string",
            default_on_hold_comfort_noise_enabled=True,
            dtmf_type="RFC 2833",
            encode_contact_header_enabled=True,
            encrypted_media="SRTP",
            inbound={
                "ani_number_format": "+E.164",
                "channel_limit": 10,
                "codecs": ["string"],
                "default_primary_ip_id": "192.168.0.0",
                "default_routing_method": "sequential",
                "default_secondary_ip_id": "192.168.0.0",
                "default_tertiary_ip_id": "192.168.0.0",
                "dnis_number_format": "+e164",
                "generate_ringback_tone": True,
                "isup_headers_enabled": True,
                "prack_enabled": True,
                "shaken_stir_enabled": True,
                "sip_compact_headers_enabled": True,
                "sip_region": "US",
                "sip_subdomain": "test",
                "sip_subdomain_receive_settings": "only_my_connections",
                "timeout_1xx_secs": 10,
                "timeout_2xx_secs": 20,
            },
            ios_push_credential_id="ec0c8e5d-439e-4620-a0c1-9d9c8d02a836",
            onnet_t38_passthrough_enabled=False,
            outbound={
                "ani_override": "string",
                "ani_override_type": "always",
                "call_parking_enabled": True,
                "channel_limit": 10,
                "generate_ringback_tone": True,
                "instant_ringback_enabled": True,
                "ip_authentication_method": "token",
                "ip_authentication_token": "string",
                "localization": "string",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
                "t38_reinvite_source": "customer",
                "tech_prefix": "string",
            },
            rtcp_settings={
                "capture_enabled": True,
                "port": "rtcp-mux",
                "report_frequency_secs": 10,
            },
            tags=["tag1", "tag2"],
            transport_protocol="UDP",
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ip_connections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = response.parse()
        assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ip_connections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = response.parse()
            assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ip_connections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.list()
        assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.list(
            filter={
                "connection_name": {"contains": "contains"},
                "fqdn": "fqdn",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ip_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = response.parse()
        assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ip_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = response.parse()
            assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        ip_connection = client.ip_connections.delete(
            "id",
        )
        assert_matches_type(IPConnectionDeleteResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ip_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = response.parse()
        assert_matches_type(IPConnectionDeleteResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ip_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = response.parse()
            assert_matches_type(IPConnectionDeleteResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ip_connections.with_raw_response.delete(
                "",
            )


class TestAsyncIPConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.create()
        assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.create(
            active=True,
            anchorsite_override="Latency",
            android_push_credential_id="06b09dfd-7154-4980-8b75-cebf7a9d4f8e",
            connection_name="string",
            default_on_hold_comfort_noise_enabled=True,
            dtmf_type="RFC 2833",
            encode_contact_header_enabled=True,
            encrypted_media="SRTP",
            inbound={
                "ani_number_format": "+E.164",
                "channel_limit": 10,
                "codecs": ["string"],
                "default_routing_method": "sequential",
                "dnis_number_format": "+e164",
                "generate_ringback_tone": True,
                "isup_headers_enabled": True,
                "prack_enabled": True,
                "shaken_stir_enabled": True,
                "sip_compact_headers_enabled": True,
                "sip_region": "US",
                "sip_subdomain": "test",
                "sip_subdomain_receive_settings": "only_my_connections",
                "timeout_1xx_secs": 10,
                "timeout_2xx_secs": 20,
            },
            ios_push_credential_id="ec0c8e5d-439e-4620-a0c1-9d9c8d02a836",
            onnet_t38_passthrough_enabled=False,
            outbound={
                "ani_override": "string",
                "ani_override_type": "always",
                "call_parking_enabled": True,
                "channel_limit": 10,
                "generate_ringback_tone": True,
                "instant_ringback_enabled": True,
                "ip_authentication_method": "token",
                "ip_authentication_token": "string",
                "localization": "string",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
                "t38_reinvite_source": "customer",
                "tech_prefix": "string",
            },
            rtcp_settings={
                "capture_enabled": True,
                "port": "rtcp-mux",
                "report_frequency_secs": 10,
            },
            tags=["tag1", "tag2"],
            transport_protocol="UDP",
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ip_connections.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = await response.parse()
        assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ip_connections.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = await response.parse()
            assert_matches_type(IPConnectionCreateResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.retrieve(
            "id",
        )
        assert_matches_type(IPConnectionRetrieveResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ip_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = await response.parse()
        assert_matches_type(IPConnectionRetrieveResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ip_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = await response.parse()
            assert_matches_type(IPConnectionRetrieveResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ip_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.update(
            id="id",
        )
        assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.update(
            id="id",
            active=True,
            anchorsite_override="Latency",
            android_push_credential_id="06b09dfd-7154-4980-8b75-cebf7a9d4f8e",
            connection_name="string",
            default_on_hold_comfort_noise_enabled=True,
            dtmf_type="RFC 2833",
            encode_contact_header_enabled=True,
            encrypted_media="SRTP",
            inbound={
                "ani_number_format": "+E.164",
                "channel_limit": 10,
                "codecs": ["string"],
                "default_primary_ip_id": "192.168.0.0",
                "default_routing_method": "sequential",
                "default_secondary_ip_id": "192.168.0.0",
                "default_tertiary_ip_id": "192.168.0.0",
                "dnis_number_format": "+e164",
                "generate_ringback_tone": True,
                "isup_headers_enabled": True,
                "prack_enabled": True,
                "shaken_stir_enabled": True,
                "sip_compact_headers_enabled": True,
                "sip_region": "US",
                "sip_subdomain": "test",
                "sip_subdomain_receive_settings": "only_my_connections",
                "timeout_1xx_secs": 10,
                "timeout_2xx_secs": 20,
            },
            ios_push_credential_id="ec0c8e5d-439e-4620-a0c1-9d9c8d02a836",
            onnet_t38_passthrough_enabled=False,
            outbound={
                "ani_override": "string",
                "ani_override_type": "always",
                "call_parking_enabled": True,
                "channel_limit": 10,
                "generate_ringback_tone": True,
                "instant_ringback_enabled": True,
                "ip_authentication_method": "token",
                "ip_authentication_token": "string",
                "localization": "string",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
                "t38_reinvite_source": "customer",
                "tech_prefix": "string",
            },
            rtcp_settings={
                "capture_enabled": True,
                "port": "rtcp-mux",
                "report_frequency_secs": 10,
            },
            tags=["tag1", "tag2"],
            transport_protocol="UDP",
            webhook_api_version="1",
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ip_connections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = await response.parse()
        assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ip_connections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = await response.parse()
            assert_matches_type(IPConnectionUpdateResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ip_connections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.list()
        assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.list(
            filter={
                "connection_name": {"contains": "contains"},
                "fqdn": "fqdn",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ip_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = await response.parse()
        assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ip_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = await response.parse()
            assert_matches_type(IPConnectionListResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        ip_connection = await async_client.ip_connections.delete(
            "id",
        )
        assert_matches_type(IPConnectionDeleteResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ip_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_connection = await response.parse()
        assert_matches_type(IPConnectionDeleteResponse, ip_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ip_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_connection = await response.parse()
            assert_matches_type(IPConnectionDeleteResponse, ip_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ip_connections.with_raw_response.delete(
                "",
            )
