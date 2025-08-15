# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.bundle_pricing import (
    BillingBundleListResponse,
    BillingBundleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingBundles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        billing_bundle = client.bundle_pricing.billing_bundles.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
        )
        assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        billing_bundle = client.bundle_pricing.billing_bundles.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.bundle_pricing.billing_bundles.with_raw_response.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_bundle = response.parse()
        assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.bundle_pricing.billing_bundles.with_streaming_response.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_bundle = response.parse()
            assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bundle_id` but received ''"):
            client.bundle_pricing.billing_bundles.with_raw_response.retrieve(
                bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        billing_bundle = client.bundle_pricing.billing_bundles.list()
        assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        billing_bundle = client.bundle_pricing.billing_bundles.list(
            filter={
                "country_iso": ["US"],
                "resource": ["+15617819942"],
            },
            page={
                "number": 1,
                "size": 1,
            },
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.bundle_pricing.billing_bundles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_bundle = response.parse()
        assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.bundle_pricing.billing_bundles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_bundle = response.parse()
            assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBillingBundles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        billing_bundle = await async_client.bundle_pricing.billing_bundles.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
        )
        assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        billing_bundle = await async_client.bundle_pricing.billing_bundles.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.billing_bundles.with_raw_response.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_bundle = await response.parse()
        assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.billing_bundles.with_streaming_response.retrieve(
            bundle_id="8661948c-a386-4385-837f-af00f40f111a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_bundle = await response.parse()
            assert_matches_type(BillingBundleRetrieveResponse, billing_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bundle_id` but received ''"):
            await async_client.bundle_pricing.billing_bundles.with_raw_response.retrieve(
                bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        billing_bundle = await async_client.bundle_pricing.billing_bundles.list()
        assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        billing_bundle = await async_client.bundle_pricing.billing_bundles.list(
            filter={
                "country_iso": ["US"],
                "resource": ["+15617819942"],
            },
            page={
                "number": 1,
                "size": 1,
            },
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.billing_bundles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_bundle = await response.parse()
        assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.billing_bundles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_bundle = await response.parse()
            assert_matches_type(BillingBundleListResponse, billing_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True
