# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    DynamicEmergencyEndpointListResponse,
    DynamicEmergencyEndpointCreateResponse,
    DynamicEmergencyEndpointDeleteResponse,
    DynamicEmergencyEndpointRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDynamicEmergencyEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        dynamic_emergency_endpoint = client.dynamic_emergency_endpoints.create(
            callback_number="+13125550000",
            caller_name="Jane Doe Desk Phone",
            dynamic_emergency_address_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(DynamicEmergencyEndpointCreateResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_endpoints.with_raw_response.create(
            callback_number="+13125550000",
            caller_name="Jane Doe Desk Phone",
            dynamic_emergency_address_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = response.parse()
        assert_matches_type(DynamicEmergencyEndpointCreateResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.dynamic_emergency_endpoints.with_streaming_response.create(
            callback_number="+13125550000",
            caller_name="Jane Doe Desk Phone",
            dynamic_emergency_address_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = response.parse()
            assert_matches_type(DynamicEmergencyEndpointCreateResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        dynamic_emergency_endpoint = client.dynamic_emergency_endpoints.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyEndpointRetrieveResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_endpoints.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = response.parse()
        assert_matches_type(DynamicEmergencyEndpointRetrieveResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.dynamic_emergency_endpoints.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = response.parse()
            assert_matches_type(DynamicEmergencyEndpointRetrieveResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dynamic_emergency_endpoints.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        dynamic_emergency_endpoint = client.dynamic_emergency_endpoints.list()
        assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        dynamic_emergency_endpoint = client.dynamic_emergency_endpoints.list(
            filter={
                "country_code": "country_code",
                "status": "pending",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = response.parse()
        assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dynamic_emergency_endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = response.parse()
            assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        dynamic_emergency_endpoint = client.dynamic_emergency_endpoints.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyEndpointDeleteResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_endpoints.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = response.parse()
        assert_matches_type(DynamicEmergencyEndpointDeleteResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.dynamic_emergency_endpoints.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = response.parse()
            assert_matches_type(DynamicEmergencyEndpointDeleteResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dynamic_emergency_endpoints.with_raw_response.delete(
                "",
            )


class TestAsyncDynamicEmergencyEndpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_endpoint = await async_client.dynamic_emergency_endpoints.create(
            callback_number="+13125550000",
            caller_name="Jane Doe Desk Phone",
            dynamic_emergency_address_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )
        assert_matches_type(DynamicEmergencyEndpointCreateResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_endpoints.with_raw_response.create(
            callback_number="+13125550000",
            caller_name="Jane Doe Desk Phone",
            dynamic_emergency_address_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = await response.parse()
        assert_matches_type(DynamicEmergencyEndpointCreateResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_endpoints.with_streaming_response.create(
            callback_number="+13125550000",
            caller_name="Jane Doe Desk Phone",
            dynamic_emergency_address_id="0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = await response.parse()
            assert_matches_type(DynamicEmergencyEndpointCreateResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_endpoint = await async_client.dynamic_emergency_endpoints.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyEndpointRetrieveResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_endpoints.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = await response.parse()
        assert_matches_type(DynamicEmergencyEndpointRetrieveResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_endpoints.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = await response.parse()
            assert_matches_type(DynamicEmergencyEndpointRetrieveResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dynamic_emergency_endpoints.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_endpoint = await async_client.dynamic_emergency_endpoints.list()
        assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_endpoint = await async_client.dynamic_emergency_endpoints.list(
            filter={
                "country_code": "country_code",
                "status": "pending",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = await response.parse()
        assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = await response.parse()
            assert_matches_type(DynamicEmergencyEndpointListResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_endpoint = await async_client.dynamic_emergency_endpoints.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyEndpointDeleteResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_endpoints.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_endpoint = await response.parse()
        assert_matches_type(DynamicEmergencyEndpointDeleteResponse, dynamic_emergency_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_endpoints.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_endpoint = await response.parse()
            assert_matches_type(DynamicEmergencyEndpointDeleteResponse, dynamic_emergency_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dynamic_emergency_endpoints.with_raw_response.delete(
                "",
            )
