# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.storage.sqldbs import ActionQueryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Telnyx) -> None:
        action = client.storage.sqldbs.actions.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
        )
        assert_matches_type(ActionQueryResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Telnyx) -> None:
        action = client.storage.sqldbs.actions.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
            params=["alice"],
        )
        assert_matches_type(ActionQueryResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Telnyx) -> None:
        response = client.storage.sqldbs.actions.with_raw_response.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionQueryResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Telnyx) -> None:
        with client.storage.sqldbs.actions.with_streaming_response.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionQueryResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_query(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.sqldbs.actions.with_raw_response.query(
                id="",
                sql="SELECT * FROM users WHERE name = ?",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.storage.sqldbs.actions.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
        )
        assert_matches_type(ActionQueryResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.storage.sqldbs.actions.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
            params=["alice"],
        )
        assert_matches_type(ActionQueryResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.sqldbs.actions.with_raw_response.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionQueryResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.sqldbs.actions.with_streaming_response.query(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sql="SELECT * FROM users WHERE name = ?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionQueryResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_query(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.sqldbs.actions.with_raw_response.query(
                id="",
                sql="SELECT * FROM users WHERE name = ?",
            )
