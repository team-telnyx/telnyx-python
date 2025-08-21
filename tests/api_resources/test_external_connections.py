# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ExternalConnectionListResponse,
    ExternalConnectionCreateResponse,
    ExternalConnectionDeleteResponse,
    ExternalConnectionUpdateResponse,
    ExternalConnectionRetrieveResponse,
    ExternalConnectionUpdateLocationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        external_connection = client.external_connections.create(
            external_sip_connection="zoom",
            outbound={},
        )
        assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        external_connection = client.external_connections.create(
            external_sip_connection="zoom",
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            active=False,
            inbound={"channel_limit": 10},
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.external_connections.with_raw_response.create(
            external_sip_connection="zoom",
            outbound={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = response.parse()
        assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.external_connections.with_streaming_response.create(
            external_sip_connection="zoom",
            outbound={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = response.parse()
            assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        external_connection = client.external_connections.retrieve(
            "id",
        )
        assert_matches_type(ExternalConnectionRetrieveResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.external_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = response.parse()
        assert_matches_type(ExternalConnectionRetrieveResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.external_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = response.parse()
            assert_matches_type(ExternalConnectionRetrieveResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        external_connection = client.external_connections.update(
            id="id",
            outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
        )
        assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        external_connection = client.external_connections.update(
            id="id",
            outbound={
                "outbound_voice_profile_id": "outbound_voice_profile_id",
                "channel_limit": 10,
            },
            active=False,
            inbound={"channel_limit": 10},
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.external_connections.with_raw_response.update(
            id="id",
            outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = response.parse()
        assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.external_connections.with_streaming_response.update(
            id="id",
            outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = response.parse()
            assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.with_raw_response.update(
                id="",
                outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        external_connection = client.external_connections.list()
        assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        external_connection = client.external_connections.list(
            filter={
                "id": "1930241863466354012",
                "connection_name": {"contains": "My Connection"},
                "created_at": "2022-12-31",
                "external_sip_connection": "zoom",
                "phone_number": {"contains": "+15555555555"},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.external_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = response.parse()
        assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.external_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = response.parse()
            assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        external_connection = client.external_connections.delete(
            "id",
        )
        assert_matches_type(ExternalConnectionDeleteResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.external_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = response.parse()
        assert_matches_type(ExternalConnectionDeleteResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.external_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = response.parse()
            assert_matches_type(ExternalConnectionDeleteResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_location(self, client: Telnyx) -> None:
        external_connection = client.external_connections.update_location(
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalConnectionUpdateLocationResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_location(self, client: Telnyx) -> None:
        response = client.external_connections.with_raw_response.update_location(
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = response.parse()
        assert_matches_type(ExternalConnectionUpdateLocationResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_location(self, client: Telnyx) -> None:
        with client.external_connections.with_streaming_response.update_location(
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = response.parse()
            assert_matches_type(ExternalConnectionUpdateLocationResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_location(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.with_raw_response.update_location(
                location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            client.external_connections.with_raw_response.update_location(
                location_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncExternalConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.create(
            external_sip_connection="zoom",
            outbound={},
        )
        assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.create(
            external_sip_connection="zoom",
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            active=False,
            inbound={"channel_limit": 10},
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.with_raw_response.create(
            external_sip_connection="zoom",
            outbound={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = await response.parse()
        assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.with_streaming_response.create(
            external_sip_connection="zoom",
            outbound={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = await response.parse()
            assert_matches_type(ExternalConnectionCreateResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.retrieve(
            "id",
        )
        assert_matches_type(ExternalConnectionRetrieveResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = await response.parse()
        assert_matches_type(ExternalConnectionRetrieveResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = await response.parse()
            assert_matches_type(ExternalConnectionRetrieveResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.update(
            id="id",
            outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
        )
        assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.update(
            id="id",
            outbound={
                "outbound_voice_profile_id": "outbound_voice_profile_id",
                "channel_limit": 10,
            },
            active=False,
            inbound={"channel_limit": 10},
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_event_url="https://example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.with_raw_response.update(
            id="id",
            outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = await response.parse()
        assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.with_streaming_response.update(
            id="id",
            outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = await response.parse()
            assert_matches_type(ExternalConnectionUpdateResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.with_raw_response.update(
                id="",
                outbound={"outbound_voice_profile_id": "outbound_voice_profile_id"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.list()
        assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.list(
            filter={
                "id": "1930241863466354012",
                "connection_name": {"contains": "My Connection"},
                "created_at": "2022-12-31",
                "external_sip_connection": "zoom",
                "phone_number": {"contains": "+15555555555"},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = await response.parse()
        assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = await response.parse()
            assert_matches_type(ExternalConnectionListResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.delete(
            "id",
        )
        assert_matches_type(ExternalConnectionDeleteResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = await response.parse()
        assert_matches_type(ExternalConnectionDeleteResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = await response.parse()
            assert_matches_type(ExternalConnectionDeleteResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_location(self, async_client: AsyncTelnyx) -> None:
        external_connection = await async_client.external_connections.update_location(
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalConnectionUpdateLocationResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_location(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.with_raw_response.update_location(
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_connection = await response.parse()
        assert_matches_type(ExternalConnectionUpdateLocationResponse, external_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_location(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.with_streaming_response.update_location(
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_connection = await response.parse()
            assert_matches_type(ExternalConnectionUpdateLocationResponse, external_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_location(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.with_raw_response.update_location(
                location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
                static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            await async_client.external_connections.with_raw_response.update_location(
                location_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                static_emergency_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
