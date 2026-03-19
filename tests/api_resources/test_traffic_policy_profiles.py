# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TrafficPolicyProfileListResponse,
    TrafficPolicyProfileCreateResponse,
    TrafficPolicyProfileDeleteResponse,
    TrafficPolicyProfileUpdateResponse,
    TrafficPolicyProfileRetrieveResponse,
    TrafficPolicyProfileListServicesResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrafficPolicyProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.create(
            type="whitelist",
        )
        assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.create(
            type="whitelist",
            domains=["www.hbomax.com", "netflix.com"],
            ip_ranges=["10.64.0.0/24", "10.64.0.0/25"],
            limit_bw_kbps=512,
            services=["service_123", "service_456"],
        )
        assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.traffic_policy_profiles.with_raw_response.create(
            type="whitelist",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = response.parse()
        assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.traffic_policy_profiles.with_streaming_response.create(
            type="whitelist",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = response.parse()
            assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TrafficPolicyProfileRetrieveResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.traffic_policy_profiles.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = response.parse()
        assert_matches_type(TrafficPolicyProfileRetrieveResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.traffic_policy_profiles.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = response.parse()
            assert_matches_type(TrafficPolicyProfileRetrieveResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.traffic_policy_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            domains=["netflix.com"],
            ip_ranges=["10.64.0.0/24"],
            limit_bw_kbps=1024,
            services=["service_123"],
            type="whitelist",
        )
        assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.traffic_policy_profiles.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = response.parse()
        assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.traffic_policy_profiles.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = response.parse()
            assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.traffic_policy_profiles.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.list()
        assert_matches_type(
            SyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.list(
            filter_service="filter[service]",
            filter_type="whitelist",
            page_number=1,
            page_size=1,
            sort="service",
        )
        assert_matches_type(
            SyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.traffic_policy_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.traffic_policy_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TrafficPolicyProfileDeleteResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.traffic_policy_profiles.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = response.parse()
        assert_matches_type(TrafficPolicyProfileDeleteResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.traffic_policy_profiles.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = response.parse()
            assert_matches_type(TrafficPolicyProfileDeleteResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.traffic_policy_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_services(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.list_services()
        assert_matches_type(
            SyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            traffic_policy_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_services_with_all_params(self, client: Telnyx) -> None:
        traffic_policy_profile = client.traffic_policy_profiles.list_services(
            filter_group="filter[group]",
            filter_name="filter[name]",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            SyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            traffic_policy_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_services(self, client: Telnyx) -> None:
        response = client.traffic_policy_profiles.with_raw_response.list_services()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            traffic_policy_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_services(self, client: Telnyx) -> None:
        with client.traffic_policy_profiles.with_streaming_response.list_services() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
                traffic_policy_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncTrafficPolicyProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.create(
            type="whitelist",
        )
        assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.create(
            type="whitelist",
            domains=["www.hbomax.com", "netflix.com"],
            ip_ranges=["10.64.0.0/24", "10.64.0.0/25"],
            limit_bw_kbps=512,
            services=["service_123", "service_456"],
        )
        assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.traffic_policy_profiles.with_raw_response.create(
            type="whitelist",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = await response.parse()
        assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.traffic_policy_profiles.with_streaming_response.create(
            type="whitelist",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = await response.parse()
            assert_matches_type(TrafficPolicyProfileCreateResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TrafficPolicyProfileRetrieveResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.traffic_policy_profiles.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = await response.parse()
        assert_matches_type(TrafficPolicyProfileRetrieveResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.traffic_policy_profiles.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = await response.parse()
            assert_matches_type(TrafficPolicyProfileRetrieveResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.traffic_policy_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            domains=["netflix.com"],
            ip_ranges=["10.64.0.0/24"],
            limit_bw_kbps=1024,
            services=["service_123"],
            type="whitelist",
        )
        assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.traffic_policy_profiles.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = await response.parse()
        assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.traffic_policy_profiles.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = await response.parse()
            assert_matches_type(TrafficPolicyProfileUpdateResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.traffic_policy_profiles.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.list()
        assert_matches_type(
            AsyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.list(
            filter_service="filter[service]",
            filter_type="whitelist",
            page_number=1,
            page_size=1,
            sort="service",
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.traffic_policy_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.traffic_policy_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[TrafficPolicyProfileListResponse], traffic_policy_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TrafficPolicyProfileDeleteResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.traffic_policy_profiles.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = await response.parse()
        assert_matches_type(TrafficPolicyProfileDeleteResponse, traffic_policy_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.traffic_policy_profiles.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = await response.parse()
            assert_matches_type(TrafficPolicyProfileDeleteResponse, traffic_policy_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.traffic_policy_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_services(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.list_services()
        assert_matches_type(
            AsyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            traffic_policy_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_services_with_all_params(self, async_client: AsyncTelnyx) -> None:
        traffic_policy_profile = await async_client.traffic_policy_profiles.list_services(
            filter_group="filter[group]",
            filter_name="filter[name]",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            traffic_policy_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_services(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.traffic_policy_profiles.with_raw_response.list_services()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_policy_profile = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            traffic_policy_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_services(self, async_client: AsyncTelnyx) -> None:
        async with async_client.traffic_policy_profiles.with_streaming_response.list_services() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_policy_profile = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
                traffic_policy_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
