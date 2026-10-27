# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PayConnector,
    PayConnectorResponse,
)
from telnyx.pagination import SyncEmailBracketCursorPagination, AsyncEmailBracketCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.create(
            config={"auth_type": "none"},
            name="my-payment-connector",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.create(
            config={
                "auth_type": "none",
                "token": {},
                "endpoint_url": "https://processor.example.com/pay",
                "password": {},
                "timeout": 1,
                "username": {},
            },
            name="my-payment-connector",
            mode="test",
            type="generic",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.pay_connectors.with_raw_response.create(
            config={"auth_type": "none"},
            name="my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = response.parse()
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.pay_connectors.with_streaming_response.create(
            config={"auth_type": "none"},
            name="my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = response.parse()
            assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.retrieve(
            "my-payment-connector",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.pay_connectors.with_raw_response.retrieve(
            "my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = response.parse()
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.pay_connectors.with_streaming_response.retrieve(
            "my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = response.parse()
            assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.pay_connectors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.update(
            name="my-payment-connector",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.update(
            name="my-payment-connector",
            config={
                "password": "P",
                "username": "P",
                "token": {},
                "auth_type": "basic",
                "endpoint_url": "https://processor.example.com/pay",
                "timeout": 1,
            },
            mode="live",
            type="generic",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.pay_connectors.with_raw_response.update(
            name="my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = response.parse()
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.pay_connectors.with_streaming_response.update(
            name="my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = response.parse()
            assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.pay_connectors.with_raw_response.update(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.list()
        assert_matches_type(SyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.list(
            filter_created_at_eq="2026-10-01T00:00:00Z",
            filter_created_at_gt="2026-10-01T00:00:00Z",
            filter_created_at_gte="2026-10-01T00:00:00Z",
            filter_created_at_lt="2026-10-01T00:00:00Z",
            filter_created_at_lte="2026-10-01T00:00:00Z",
            filter_mode="test",
            filter_name="my-payment-connector",
            filter_type="generic",
            filter_updated_at_eq="2026-10-01T00:00:00Z",
            filter_updated_at_gt="2026-10-01T00:00:00Z",
            filter_updated_at_gte="2026-10-01T00:00:00Z",
            filter_updated_at_lt="2026-10-01T00:00:00Z",
            filter_updated_at_lte="2026-10-01T00:00:00Z",
            page_after="page[after]",
            page_before="page[before]",
            page_size=1,
            sort="-created_at",
        )
        assert_matches_type(SyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.pay_connectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = response.parse()
        assert_matches_type(SyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.pay_connectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = response.parse()
            assert_matches_type(SyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        pay_connector = client.pay_connectors.delete(
            "my-payment-connector",
        )
        assert pay_connector is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.pay_connectors.with_raw_response.delete(
            "my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = response.parse()
        assert pay_connector is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.pay_connectors.with_streaming_response.delete(
            "my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = response.parse()
            assert pay_connector is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.pay_connectors.with_raw_response.delete(
                "",
            )


class TestAsyncPayConnectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.create(
            config={"auth_type": "none"},
            name="my-payment-connector",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.create(
            config={
                "auth_type": "none",
                "token": {},
                "endpoint_url": "https://processor.example.com/pay",
                "password": {},
                "timeout": 1,
                "username": {},
            },
            name="my-payment-connector",
            mode="test",
            type="generic",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pay_connectors.with_raw_response.create(
            config={"auth_type": "none"},
            name="my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = await response.parse()
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pay_connectors.with_streaming_response.create(
            config={"auth_type": "none"},
            name="my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = await response.parse()
            assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.retrieve(
            "my-payment-connector",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pay_connectors.with_raw_response.retrieve(
            "my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = await response.parse()
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pay_connectors.with_streaming_response.retrieve(
            "my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = await response.parse()
            assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.pay_connectors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.update(
            name="my-payment-connector",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.update(
            name="my-payment-connector",
            config={
                "password": "P",
                "username": "P",
                "token": {},
                "auth_type": "basic",
                "endpoint_url": "https://processor.example.com/pay",
                "timeout": 1,
            },
            mode="live",
            type="generic",
        )
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pay_connectors.with_raw_response.update(
            name="my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = await response.parse()
        assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pay_connectors.with_streaming_response.update(
            name="my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = await response.parse()
            assert_matches_type(PayConnectorResponse, pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.pay_connectors.with_raw_response.update(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.list()
        assert_matches_type(AsyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.list(
            filter_created_at_eq="2026-10-01T00:00:00Z",
            filter_created_at_gt="2026-10-01T00:00:00Z",
            filter_created_at_gte="2026-10-01T00:00:00Z",
            filter_created_at_lt="2026-10-01T00:00:00Z",
            filter_created_at_lte="2026-10-01T00:00:00Z",
            filter_mode="test",
            filter_name="my-payment-connector",
            filter_type="generic",
            filter_updated_at_eq="2026-10-01T00:00:00Z",
            filter_updated_at_gt="2026-10-01T00:00:00Z",
            filter_updated_at_gte="2026-10-01T00:00:00Z",
            filter_updated_at_lt="2026-10-01T00:00:00Z",
            filter_updated_at_lte="2026-10-01T00:00:00Z",
            page_after="page[after]",
            page_before="page[before]",
            page_size=1,
            sort="-created_at",
        )
        assert_matches_type(AsyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pay_connectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = await response.parse()
        assert_matches_type(AsyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pay_connectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = await response.parse()
            assert_matches_type(AsyncEmailBracketCursorPagination[PayConnector], pay_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        pay_connector = await async_client.pay_connectors.delete(
            "my-payment-connector",
        )
        assert pay_connector is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pay_connectors.with_raw_response.delete(
            "my-payment-connector",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_connector = await response.parse()
        assert pay_connector is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pay_connectors.with_streaming_response.delete(
            "my-payment-connector",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_connector = await response.parse()
            assert pay_connector is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.pay_connectors.with_raw_response.delete(
                "",
            )
