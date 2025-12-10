# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.bundle_pricing import (
    UserBundleListResponse,
    UserBundleCreateResponse,
    UserBundleRetrieveResponse,
    UserBundleDeactivateResponse,
    UserBundleListUnusedResponse,
    UserBundleListResourcesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserBundles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.create()
        assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.create(
            idempotency_key="12ade33a-21c0-473b-b055-b3c836e1c292",
            items=[
                {
                    "billing_bundle_id": "12ade33a-21c0-473b-b055-b3c836e1c292",
                    "quantity": 0,
                }
            ],
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.bundle_pricing.user_bundles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = response.parse()
        assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.bundle_pricing.user_bundles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = response.parse()
            assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )
        assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.bundle_pricing.user_bundles.with_raw_response.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = response.parse()
        assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.bundle_pricing.user_bundles.with_streaming_response.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = response.parse()
            assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_bundle_id` but received ''"):
            client.bundle_pricing.user_bundles.with_raw_response.retrieve(
                user_bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.list()
        assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.list(
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
        assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.bundle_pricing.user_bundles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = response.parse()
        assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.bundle_pricing.user_bundles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = response.parse()
            assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )
        assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deactivate_with_all_params(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: Telnyx) -> None:
        response = client.bundle_pricing.user_bundles.with_raw_response.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = response.parse()
        assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: Telnyx) -> None:
        with client.bundle_pricing.user_bundles.with_streaming_response.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = response.parse()
            assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_bundle_id` but received ''"):
            client.bundle_pricing.user_bundles.with_raw_response.deactivate(
                user_bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_resources(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )
        assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_resources_with_all_params(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_resources(self, client: Telnyx) -> None:
        response = client.bundle_pricing.user_bundles.with_raw_response.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = response.parse()
        assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_resources(self, client: Telnyx) -> None:
        with client.bundle_pricing.user_bundles.with_streaming_response.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = response.parse()
            assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_resources(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_bundle_id` but received ''"):
            client.bundle_pricing.user_bundles.with_raw_response.list_resources(
                user_bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_unused(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.list_unused()
        assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_unused_with_all_params(self, client: Telnyx) -> None:
        user_bundle = client.bundle_pricing.user_bundles.list_unused(
            filter={
                "country_iso": ["US"],
                "resource": ["+15617819942"],
            },
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_unused(self, client: Telnyx) -> None:
        response = client.bundle_pricing.user_bundles.with_raw_response.list_unused()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = response.parse()
        assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_unused(self, client: Telnyx) -> None:
        with client.bundle_pricing.user_bundles.with_streaming_response.list_unused() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = response.parse()
            assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserBundles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.create()
        assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.create(
            idempotency_key="12ade33a-21c0-473b-b055-b3c836e1c292",
            items=[
                {
                    "billing_bundle_id": "12ade33a-21c0-473b-b055-b3c836e1c292",
                    "quantity": 0,
                }
            ],
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.user_bundles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = await response.parse()
        assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.user_bundles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = await response.parse()
            assert_matches_type(UserBundleCreateResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )
        assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.user_bundles.with_raw_response.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = await response.parse()
        assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.user_bundles.with_streaming_response.retrieve(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = await response.parse()
            assert_matches_type(UserBundleRetrieveResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_bundle_id` but received ''"):
            await async_client.bundle_pricing.user_bundles.with_raw_response.retrieve(
                user_bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.list()
        assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.list(
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
        assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.user_bundles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = await response.parse()
        assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.user_bundles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = await response.parse()
            assert_matches_type(UserBundleListResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )
        assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deactivate_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.user_bundles.with_raw_response.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = await response.parse()
        assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.user_bundles.with_streaming_response.deactivate(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = await response.parse()
            assert_matches_type(UserBundleDeactivateResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_bundle_id` but received ''"):
            await async_client.bundle_pricing.user_bundles.with_raw_response.deactivate(
                user_bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_resources(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )
        assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_resources_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_resources(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.user_bundles.with_raw_response.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = await response.parse()
        assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_resources(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.user_bundles.with_streaming_response.list_resources(
            user_bundle_id="ca1d2263-d1f1-43ac-ba53-248e7a4bb26a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = await response.parse()
            assert_matches_type(UserBundleListResourcesResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_resources(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_bundle_id` but received ''"):
            await async_client.bundle_pricing.user_bundles.with_raw_response.list_resources(
                user_bundle_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_unused(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.list_unused()
        assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_unused_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_bundle = await async_client.bundle_pricing.user_bundles.list_unused(
            filter={
                "country_iso": ["US"],
                "resource": ["+15617819942"],
            },
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_unused(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bundle_pricing.user_bundles.with_raw_response.list_unused()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_bundle = await response.parse()
        assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_unused(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bundle_pricing.user_bundles.with_streaming_response.list_unused() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_bundle = await response.parse()
            assert_matches_type(UserBundleListUnusedResponse, user_bundle, path=["response"])

        assert cast(Any, response.is_closed) is True
