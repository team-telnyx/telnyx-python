# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ManagedAccountListResponse,
    ManagedAccountCreateResponse,
    ManagedAccountUpdateResponse,
    ManagedAccountRetrieveResponse,
    ManagedAccountUpdateGlobalChannelLimitResponse,
    ManagedAccountGetAllocatableGlobalOutboundChannelsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManagedAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.create(
            business_name="Larry's Cat Food Inc",
        )
        assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.create(
            business_name="Larry's Cat Food Inc",
            email="larry_cat_food@customer.org",
            managed_account_allow_custom_pricing=False,
            password="3jVjLq!tMuWKyWx4NN*CvhnB",
            rollup_billing=False,
        )
        assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.managed_accounts.with_raw_response.create(
            business_name="Larry's Cat Food Inc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = response.parse()
        assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.managed_accounts.with_streaming_response.create(
            business_name="Larry's Cat Food Inc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = response.parse()
            assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.retrieve(
            "id",
        )
        assert_matches_type(ManagedAccountRetrieveResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.managed_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = response.parse()
        assert_matches_type(ManagedAccountRetrieveResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.managed_accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = response.parse()
            assert_matches_type(ManagedAccountRetrieveResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.managed_accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.update(
            id="id",
        )
        assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.update(
            id="id",
            managed_account_allow_custom_pricing=True,
        )
        assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.managed_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = response.parse()
        assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.managed_accounts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = response.parse()
            assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.managed_accounts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.list()
        assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.list(
            filter={
                "email": {
                    "contains": "john",
                    "eq": "eq",
                },
                "organization_name": {
                    "contains": "contains",
                    "eq": "Example Company LLC",
                },
            },
            include_cancelled_accounts=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort="email",
        )
        assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.managed_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = response.parse()
        assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.managed_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = response.parse()
            assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_allocatable_global_outbound_channels(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.get_allocatable_global_outbound_channels()
        assert_matches_type(
            ManagedAccountGetAllocatableGlobalOutboundChannelsResponse, managed_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_allocatable_global_outbound_channels(self, client: Telnyx) -> None:
        response = client.managed_accounts.with_raw_response.get_allocatable_global_outbound_channels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = response.parse()
        assert_matches_type(
            ManagedAccountGetAllocatableGlobalOutboundChannelsResponse, managed_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_allocatable_global_outbound_channels(self, client: Telnyx) -> None:
        with client.managed_accounts.with_streaming_response.get_allocatable_global_outbound_channels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = response.parse()
            assert_matches_type(
                ManagedAccountGetAllocatableGlobalOutboundChannelsResponse, managed_account, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_global_channel_limit(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.update_global_channel_limit(
            id="id",
        )
        assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_global_channel_limit_with_all_params(self, client: Telnyx) -> None:
        managed_account = client.managed_accounts.update_global_channel_limit(
            id="id",
            channel_limit=30,
        )
        assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_global_channel_limit(self, client: Telnyx) -> None:
        response = client.managed_accounts.with_raw_response.update_global_channel_limit(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = response.parse()
        assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_global_channel_limit(self, client: Telnyx) -> None:
        with client.managed_accounts.with_streaming_response.update_global_channel_limit(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = response.parse()
            assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_global_channel_limit(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.managed_accounts.with_raw_response.update_global_channel_limit(
                id="",
            )


class TestAsyncManagedAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.create(
            business_name="Larry's Cat Food Inc",
        )
        assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.create(
            business_name="Larry's Cat Food Inc",
            email="larry_cat_food@customer.org",
            managed_account_allow_custom_pricing=False,
            password="3jVjLq!tMuWKyWx4NN*CvhnB",
            rollup_billing=False,
        )
        assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.with_raw_response.create(
            business_name="Larry's Cat Food Inc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = await response.parse()
        assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.with_streaming_response.create(
            business_name="Larry's Cat Food Inc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = await response.parse()
            assert_matches_type(ManagedAccountCreateResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.retrieve(
            "id",
        )
        assert_matches_type(ManagedAccountRetrieveResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = await response.parse()
        assert_matches_type(ManagedAccountRetrieveResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = await response.parse()
            assert_matches_type(ManagedAccountRetrieveResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.managed_accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.update(
            id="id",
        )
        assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.update(
            id="id",
            managed_account_allow_custom_pricing=True,
        )
        assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = await response.parse()
        assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = await response.parse()
            assert_matches_type(ManagedAccountUpdateResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.managed_accounts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.list()
        assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.list(
            filter={
                "email": {
                    "contains": "john",
                    "eq": "eq",
                },
                "organization_name": {
                    "contains": "contains",
                    "eq": "Example Company LLC",
                },
            },
            include_cancelled_accounts=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort="email",
        )
        assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = await response.parse()
        assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = await response.parse()
            assert_matches_type(ManagedAccountListResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_allocatable_global_outbound_channels(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.get_allocatable_global_outbound_channels()
        assert_matches_type(
            ManagedAccountGetAllocatableGlobalOutboundChannelsResponse, managed_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_allocatable_global_outbound_channels(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.with_raw_response.get_allocatable_global_outbound_channels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = await response.parse()
        assert_matches_type(
            ManagedAccountGetAllocatableGlobalOutboundChannelsResponse, managed_account, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_allocatable_global_outbound_channels(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.managed_accounts.with_streaming_response.get_allocatable_global_outbound_channels()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = await response.parse()
            assert_matches_type(
                ManagedAccountGetAllocatableGlobalOutboundChannelsResponse, managed_account, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_global_channel_limit(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.update_global_channel_limit(
            id="id",
        )
        assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_global_channel_limit_with_all_params(self, async_client: AsyncTelnyx) -> None:
        managed_account = await async_client.managed_accounts.update_global_channel_limit(
            id="id",
            channel_limit=30,
        )
        assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_global_channel_limit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.with_raw_response.update_global_channel_limit(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_account = await response.parse()
        assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_global_channel_limit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.with_streaming_response.update_global_channel_limit(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_account = await response.parse()
            assert_matches_type(ManagedAccountUpdateGlobalChannelLimitResponse, managed_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_global_channel_limit(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.managed_accounts.with_raw_response.update_global_channel_limit(
                id="",
            )
