# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    WirelessBlocklistListResponse,
    WirelessBlocklistCreateResponse,
    WirelessBlocklistDeleteResponse,
    WirelessBlocklistUpdateResponse,
    WirelessBlocklistRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWirelessBlocklists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.create(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        )
        assert_matches_type(WirelessBlocklistCreateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.wireless_blocklists.with_raw_response.create(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = response.parse()
        assert_matches_type(WirelessBlocklistCreateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.wireless_blocklists.with_streaming_response.create(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = response.parse()
            assert_matches_type(WirelessBlocklistCreateResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WirelessBlocklistRetrieveResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.wireless_blocklists.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = response.parse()
        assert_matches_type(WirelessBlocklistRetrieveResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.wireless_blocklists.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = response.parse()
            assert_matches_type(WirelessBlocklistRetrieveResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wireless_blocklists.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.update()
        assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.update(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        )
        assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.wireless_blocklists.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = response.parse()
        assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.wireless_blocklists.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = response.parse()
            assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.list()
        assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.list(
            filter_name="filter[name]",
            filter_type="filter[type]",
            filter_values="filter[values]",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.wireless_blocklists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = response.parse()
        assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.wireless_blocklists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = response.parse()
            assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        wireless_blocklist = client.wireless_blocklists.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WirelessBlocklistDeleteResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.wireless_blocklists.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = response.parse()
        assert_matches_type(WirelessBlocklistDeleteResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.wireless_blocklists.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = response.parse()
            assert_matches_type(WirelessBlocklistDeleteResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wireless_blocklists.with_raw_response.delete(
                "",
            )


class TestAsyncWirelessBlocklists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.create(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        )
        assert_matches_type(WirelessBlocklistCreateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireless_blocklists.with_raw_response.create(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = await response.parse()
        assert_matches_type(WirelessBlocklistCreateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireless_blocklists.with_streaming_response.create(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = await response.parse()
            assert_matches_type(WirelessBlocklistCreateResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WirelessBlocklistRetrieveResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireless_blocklists.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = await response.parse()
        assert_matches_type(WirelessBlocklistRetrieveResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireless_blocklists.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = await response.parse()
            assert_matches_type(WirelessBlocklistRetrieveResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wireless_blocklists.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.update()
        assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.update(
            name="My Wireless Blocklist",
            type="country",
            values=["CA", "US"],
        )
        assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireless_blocklists.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = await response.parse()
        assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireless_blocklists.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = await response.parse()
            assert_matches_type(WirelessBlocklistUpdateResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.list()
        assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.list(
            filter_name="filter[name]",
            filter_type="filter[type]",
            filter_values="filter[values]",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireless_blocklists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = await response.parse()
        assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireless_blocklists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = await response.parse()
            assert_matches_type(WirelessBlocklistListResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        wireless_blocklist = await async_client.wireless_blocklists.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WirelessBlocklistDeleteResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireless_blocklists.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless_blocklist = await response.parse()
        assert_matches_type(WirelessBlocklistDeleteResponse, wireless_blocklist, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireless_blocklists.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless_blocklist = await response.parse()
            assert_matches_type(WirelessBlocklistDeleteResponse, wireless_blocklist, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wireless_blocklists.with_raw_response.delete(
                "",
            )
