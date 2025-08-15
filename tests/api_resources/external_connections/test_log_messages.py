# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.external_connections import (
    LogMessageListResponse,
    LogMessageDismissResponse,
    LogMessageRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        log_message = client.external_connections.log_messages.retrieve(
            "id",
        )
        assert_matches_type(LogMessageRetrieveResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.external_connections.log_messages.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log_message = response.parse()
        assert_matches_type(LogMessageRetrieveResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.external_connections.log_messages.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log_message = response.parse()
            assert_matches_type(LogMessageRetrieveResponse, log_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.log_messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        log_message = client.external_connections.log_messages.list()
        assert_matches_type(LogMessageListResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        log_message = client.external_connections.log_messages.list(
            filter={
                "external_connection_id": "67ea7693-9cd5-4a68-8c76-abb3aa5bf5d2",
                "telephone_number": {
                    "contains": "+123",
                    "eq": "+1234567890",
                },
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(LogMessageListResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.external_connections.log_messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log_message = response.parse()
        assert_matches_type(LogMessageListResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.external_connections.log_messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log_message = response.parse()
            assert_matches_type(LogMessageListResponse, log_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_dismiss(self, client: Telnyx) -> None:
        log_message = client.external_connections.log_messages.dismiss(
            "id",
        )
        assert_matches_type(LogMessageDismissResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_dismiss(self, client: Telnyx) -> None:
        response = client.external_connections.log_messages.with_raw_response.dismiss(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log_message = response.parse()
        assert_matches_type(LogMessageDismissResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_dismiss(self, client: Telnyx) -> None:
        with client.external_connections.log_messages.with_streaming_response.dismiss(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log_message = response.parse()
            assert_matches_type(LogMessageDismissResponse, log_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_dismiss(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.log_messages.with_raw_response.dismiss(
                "",
            )


class TestAsyncLogMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        log_message = await async_client.external_connections.log_messages.retrieve(
            "id",
        )
        assert_matches_type(LogMessageRetrieveResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.log_messages.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log_message = await response.parse()
        assert_matches_type(LogMessageRetrieveResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.log_messages.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log_message = await response.parse()
            assert_matches_type(LogMessageRetrieveResponse, log_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.log_messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        log_message = await async_client.external_connections.log_messages.list()
        assert_matches_type(LogMessageListResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        log_message = await async_client.external_connections.log_messages.list(
            filter={
                "external_connection_id": "67ea7693-9cd5-4a68-8c76-abb3aa5bf5d2",
                "telephone_number": {
                    "contains": "+123",
                    "eq": "+1234567890",
                },
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(LogMessageListResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.log_messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log_message = await response.parse()
        assert_matches_type(LogMessageListResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.log_messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log_message = await response.parse()
            assert_matches_type(LogMessageListResponse, log_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_dismiss(self, async_client: AsyncTelnyx) -> None:
        log_message = await async_client.external_connections.log_messages.dismiss(
            "id",
        )
        assert_matches_type(LogMessageDismissResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_dismiss(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.log_messages.with_raw_response.dismiss(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log_message = await response.parse()
        assert_matches_type(LogMessageDismissResponse, log_message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_dismiss(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.log_messages.with_streaming_response.dismiss(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log_message = await response.parse()
            assert_matches_type(LogMessageDismissResponse, log_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_dismiss(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.log_messages.with_raw_response.dismiss(
                "",
            )
