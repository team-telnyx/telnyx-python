# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MobileVoiceConnection,
    MobileVoiceConnectionCreateResponse,
    MobileVoiceConnectionDeleteResponse,
    MobileVoiceConnectionUpdateResponse,
    MobileVoiceConnectionRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMobileVoiceConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.create()
        assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.create(
            active=True,
            connection_name="connection_name",
            inbound={"channel_limit": 0},
            outbound={
                "channel_limit": 0,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            tags=["string"],
            webhook_api_version="1",
            webhook_event_failover_url="webhook_event_failover_url",
            webhook_event_url="webhook_event_url",
            webhook_timeout_secs=0,
        )
        assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.mobile_voice_connections.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = response.parse()
        assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.mobile_voice_connections.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = response.parse()
            assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.retrieve(
            "id",
        )
        assert_matches_type(MobileVoiceConnectionRetrieveResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.mobile_voice_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = response.parse()
        assert_matches_type(MobileVoiceConnectionRetrieveResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.mobile_voice_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = response.parse()
            assert_matches_type(MobileVoiceConnectionRetrieveResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mobile_voice_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.update(
            id="id",
        )
        assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.update(
            id="id",
            active=True,
            connection_name="connection_name",
            inbound={"channel_limit": 0},
            outbound={
                "channel_limit": 0,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            tags=["string"],
            webhook_api_version="1",
            webhook_event_failover_url="webhook_event_failover_url",
            webhook_event_url="webhook_event_url",
            webhook_timeout_secs=0,
        )
        assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.mobile_voice_connections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = response.parse()
        assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.mobile_voice_connections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = response.parse()
            assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mobile_voice_connections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.list()
        assert_matches_type(
            SyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.list(
            filter_connection_name_contains="filter[connection_name][contains]",
            page_number=0,
            page_size=0,
            sort="sort",
        )
        assert_matches_type(
            SyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.mobile_voice_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.mobile_voice_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        mobile_voice_connection = client.mobile_voice_connections.delete(
            "id",
        )
        assert_matches_type(MobileVoiceConnectionDeleteResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.mobile_voice_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = response.parse()
        assert_matches_type(MobileVoiceConnectionDeleteResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.mobile_voice_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = response.parse()
            assert_matches_type(MobileVoiceConnectionDeleteResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mobile_voice_connections.with_raw_response.delete(
                "",
            )


class TestAsyncMobileVoiceConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.create()
        assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.create(
            active=True,
            connection_name="connection_name",
            inbound={"channel_limit": 0},
            outbound={
                "channel_limit": 0,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            tags=["string"],
            webhook_api_version="1",
            webhook_event_failover_url="webhook_event_failover_url",
            webhook_event_url="webhook_event_url",
            webhook_timeout_secs=0,
        )
        assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_voice_connections.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = await response.parse()
        assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_voice_connections.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = await response.parse()
            assert_matches_type(MobileVoiceConnectionCreateResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.retrieve(
            "id",
        )
        assert_matches_type(MobileVoiceConnectionRetrieveResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_voice_connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = await response.parse()
        assert_matches_type(MobileVoiceConnectionRetrieveResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_voice_connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = await response.parse()
            assert_matches_type(MobileVoiceConnectionRetrieveResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mobile_voice_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.update(
            id="id",
        )
        assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.update(
            id="id",
            active=True,
            connection_name="connection_name",
            inbound={"channel_limit": 0},
            outbound={
                "channel_limit": 0,
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            tags=["string"],
            webhook_api_version="1",
            webhook_event_failover_url="webhook_event_failover_url",
            webhook_event_url="webhook_event_url",
            webhook_timeout_secs=0,
        )
        assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_voice_connections.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = await response.parse()
        assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_voice_connections.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = await response.parse()
            assert_matches_type(MobileVoiceConnectionUpdateResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mobile_voice_connections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.list()
        assert_matches_type(
            AsyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.list(
            filter_connection_name_contains="filter[connection_name][contains]",
            page_number=0,
            page_size=0,
            sort="sort",
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_voice_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_voice_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[MobileVoiceConnection], mobile_voice_connection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        mobile_voice_connection = await async_client.mobile_voice_connections.delete(
            "id",
        )
        assert_matches_type(MobileVoiceConnectionDeleteResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_voice_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_voice_connection = await response.parse()
        assert_matches_type(MobileVoiceConnectionDeleteResponse, mobile_voice_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_voice_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_voice_connection = await response.parse()
            assert_matches_type(MobileVoiceConnectionDeleteResponse, mobile_voice_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mobile_voice_connections.with_raw_response.delete(
                "",
            )
