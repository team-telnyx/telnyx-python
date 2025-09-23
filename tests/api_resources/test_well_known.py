# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    WellKnownRetrieveProtectedResourceMetadataResponse,
    WellKnownRetrieveAuthorizationServerMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWellKnown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_authorization_server_metadata(self, client: Telnyx) -> None:
        well_known = client.well_known.retrieve_authorization_server_metadata()
        assert_matches_type(WellKnownRetrieveAuthorizationServerMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_authorization_server_metadata(self, client: Telnyx) -> None:
        response = client.well_known.with_raw_response.retrieve_authorization_server_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = response.parse()
        assert_matches_type(WellKnownRetrieveAuthorizationServerMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_authorization_server_metadata(self, client: Telnyx) -> None:
        with client.well_known.with_streaming_response.retrieve_authorization_server_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = response.parse()
            assert_matches_type(WellKnownRetrieveAuthorizationServerMetadataResponse, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_protected_resource_metadata(self, client: Telnyx) -> None:
        well_known = client.well_known.retrieve_protected_resource_metadata()
        assert_matches_type(WellKnownRetrieveProtectedResourceMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_protected_resource_metadata(self, client: Telnyx) -> None:
        response = client.well_known.with_raw_response.retrieve_protected_resource_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = response.parse()
        assert_matches_type(WellKnownRetrieveProtectedResourceMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_protected_resource_metadata(self, client: Telnyx) -> None:
        with client.well_known.with_streaming_response.retrieve_protected_resource_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = response.parse()
            assert_matches_type(WellKnownRetrieveProtectedResourceMetadataResponse, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWellKnown:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_authorization_server_metadata(self, async_client: AsyncTelnyx) -> None:
        well_known = await async_client.well_known.retrieve_authorization_server_metadata()
        assert_matches_type(WellKnownRetrieveAuthorizationServerMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_authorization_server_metadata(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.well_known.with_raw_response.retrieve_authorization_server_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = await response.parse()
        assert_matches_type(WellKnownRetrieveAuthorizationServerMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_authorization_server_metadata(self, async_client: AsyncTelnyx) -> None:
        async with async_client.well_known.with_streaming_response.retrieve_authorization_server_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = await response.parse()
            assert_matches_type(WellKnownRetrieveAuthorizationServerMetadataResponse, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_protected_resource_metadata(self, async_client: AsyncTelnyx) -> None:
        well_known = await async_client.well_known.retrieve_protected_resource_metadata()
        assert_matches_type(WellKnownRetrieveProtectedResourceMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_protected_resource_metadata(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.well_known.with_raw_response.retrieve_protected_resource_metadata()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = await response.parse()
        assert_matches_type(WellKnownRetrieveProtectedResourceMetadataResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_protected_resource_metadata(self, async_client: AsyncTelnyx) -> None:
        async with async_client.well_known.with_streaming_response.retrieve_protected_resource_metadata() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = await response.parse()
            assert_matches_type(WellKnownRetrieveProtectedResourceMetadataResponse, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True
