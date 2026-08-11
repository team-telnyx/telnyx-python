# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.fqdn_connections import (
    FqdnAuthenticationListResponse,
    FqdnAuthenticationPatchAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFqdnAuthentication:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        fqdn_authentication = client.fqdn_connections.fqdn_authentication.list(
            "fqdn_connection_id",
        )
        assert_matches_type(FqdnAuthenticationListResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.fqdn_connections.fqdn_authentication.with_raw_response.list(
            "fqdn_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn_authentication = response.parse()
        assert_matches_type(FqdnAuthenticationListResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.fqdn_connections.fqdn_authentication.with_streaming_response.list(
            "fqdn_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn_authentication = response.parse()
            assert_matches_type(FqdnAuthenticationListResponse, fqdn_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fqdn_connection_id` but received ''"):
            client.fqdn_connections.fqdn_authentication.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: Telnyx) -> None:
        fqdn_authentication = client.fqdn_connections.fqdn_authentication.patch_all(
            fqdn_connection_id="fqdn_connection_id",
        )
        assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all_with_all_params(self, client: Telnyx) -> None:
        fqdn_authentication = client.fqdn_connections.fqdn_authentication.patch_all(
            fqdn_connection_id="fqdn_connection_id",
            failover_url="https://failover.example.com",
            fqdn_outbound_authentication="ip-authentication",
            ip_authentication_method="p-charge-info",
            password="new_password",
            txt_name="new_txt_name",
            txt_ttl=300,
            txt_value="new_txt_value",
            user_name="newusername",
            webhook_url="https://example.com",
        )
        assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: Telnyx) -> None:
        response = client.fqdn_connections.fqdn_authentication.with_raw_response.patch_all(
            fqdn_connection_id="fqdn_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn_authentication = response.parse()
        assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: Telnyx) -> None:
        with client.fqdn_connections.fqdn_authentication.with_streaming_response.patch_all(
            fqdn_connection_id="fqdn_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn_authentication = response.parse()
            assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fqdn_connection_id` but received ''"):
            client.fqdn_connections.fqdn_authentication.with_raw_response.patch_all(
                fqdn_connection_id="",
            )


class TestAsyncFqdnAuthentication:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        fqdn_authentication = await async_client.fqdn_connections.fqdn_authentication.list(
            "fqdn_connection_id",
        )
        assert_matches_type(FqdnAuthenticationListResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdn_connections.fqdn_authentication.with_raw_response.list(
            "fqdn_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn_authentication = await response.parse()
        assert_matches_type(FqdnAuthenticationListResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdn_connections.fqdn_authentication.with_streaming_response.list(
            "fqdn_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn_authentication = await response.parse()
            assert_matches_type(FqdnAuthenticationListResponse, fqdn_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fqdn_connection_id` but received ''"):
            await async_client.fqdn_connections.fqdn_authentication.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncTelnyx) -> None:
        fqdn_authentication = await async_client.fqdn_connections.fqdn_authentication.patch_all(
            fqdn_connection_id="fqdn_connection_id",
        )
        assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fqdn_authentication = await async_client.fqdn_connections.fqdn_authentication.patch_all(
            fqdn_connection_id="fqdn_connection_id",
            failover_url="https://failover.example.com",
            fqdn_outbound_authentication="ip-authentication",
            ip_authentication_method="p-charge-info",
            password="new_password",
            txt_name="new_txt_name",
            txt_ttl=300,
            txt_value="new_txt_value",
            user_name="newusername",
            webhook_url="https://example.com",
        )
        assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdn_connections.fqdn_authentication.with_raw_response.patch_all(
            fqdn_connection_id="fqdn_connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn_authentication = await response.parse()
        assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdn_connections.fqdn_authentication.with_streaming_response.patch_all(
            fqdn_connection_id="fqdn_connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn_authentication = await response.parse()
            assert_matches_type(FqdnAuthenticationPatchAllResponse, fqdn_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fqdn_connection_id` but received ''"):
            await async_client.fqdn_connections.fqdn_authentication.with_raw_response.patch_all(
                fqdn_connection_id="",
            )
