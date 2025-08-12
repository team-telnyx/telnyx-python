# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.messaging_hosted_number_orders import ActionUploadFileResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file(self, client: Telnyx) -> None:
        action = client.messaging_hosted_number_orders.actions.upload_file(
            id="id",
        )
        assert_matches_type(ActionUploadFileResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_file_with_all_params(self, client: Telnyx) -> None:
        action = client.messaging_hosted_number_orders.actions.upload_file(
            id="id",
            bill=b"raw file contents",
            loa=b"raw file contents",
        )
        assert_matches_type(ActionUploadFileResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_file(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.actions.with_raw_response.upload_file(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionUploadFileResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_file(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.actions.with_streaming_response.upload_file(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionUploadFileResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upload_file(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_number_orders.actions.with_raw_response.upload_file(
                id="",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.messaging_hosted_number_orders.actions.upload_file(
            id="id",
        )
        assert_matches_type(ActionUploadFileResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_file_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.messaging_hosted_number_orders.actions.upload_file(
            id="id",
            bill=b"raw file contents",
            loa=b"raw file contents",
        )
        assert_matches_type(ActionUploadFileResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_file(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.actions.with_raw_response.upload_file(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionUploadFileResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_file(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.actions.with_streaming_response.upload_file(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionUploadFileResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upload_file(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_number_orders.actions.with_raw_response.upload_file(
                id="",
            )
