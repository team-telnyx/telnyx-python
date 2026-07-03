# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from telnyx.types.storage.kvs import KeyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/storage/kvs/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/keys/key").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        key = client.storage.kvs.keys.retrieve(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert key.is_closed
        assert key.json() == {"foo": "bar"}
        assert cast(Any, key.is_closed) is True
        assert isinstance(key, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/storage/kvs/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/keys/key").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        key = client.storage.kvs.keys.with_raw_response.retrieve(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert key.is_closed is True
        assert key.http_request.headers.get("X-Stainless-Lang") == "python"
        assert key.json() == {"foo": "bar"}
        assert isinstance(key, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/storage/kvs/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/keys/key").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.storage.kvs.keys.with_streaming_response.retrieve(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as key:
            assert not key.is_closed
            assert key.http_request.headers.get("X-Stainless-Lang") == "python"

            assert key.json() == {"foo": "bar"}
            assert cast(Any, key.is_closed) is True
            assert isinstance(key, StreamedBinaryAPIResponse)

        assert cast(Any, key.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.kvs.keys.with_raw_response.retrieve(
                key="key",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.storage.kvs.keys.with_raw_response.retrieve(
                key="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        key = client.storage.kvs.keys.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        key = client.storage.kvs.keys.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ttl_secs=1,
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.storage.kvs.keys.with_raw_response.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.storage.kvs.keys.with_streaming_response.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.kvs.keys.with_raw_response.update(
                key="key",
                body=b"Example data",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.storage.kvs.keys.with_raw_response.update(
                key="",
                body=b"Example data",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        key = client.storage.kvs.keys.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        key = client.storage.kvs.keys.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
            prefix="prefix",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.storage.kvs.keys.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.storage.kvs.keys.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.kvs.keys.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        key = client.storage.kvs.keys.delete(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.storage.kvs.keys.with_raw_response.delete(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.storage.kvs.keys.with_streaming_response.delete(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.kvs.keys.with_raw_response.delete(
                key="key",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.storage.kvs.keys.with_raw_response.delete(
                key="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/storage/kvs/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/keys/key").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        key = await async_client.storage.kvs.keys.retrieve(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert key.is_closed
        assert await key.json() == {"foo": "bar"}
        assert cast(Any, key.is_closed) is True
        assert isinstance(key, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/storage/kvs/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/keys/key").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        key = await async_client.storage.kvs.keys.with_raw_response.retrieve(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert key.is_closed is True
        assert key.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await key.json() == {"foo": "bar"}
        assert isinstance(key, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/storage/kvs/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/keys/key").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.storage.kvs.keys.with_streaming_response.retrieve(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as key:
            assert not key.is_closed
            assert key.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await key.json() == {"foo": "bar"}
            assert cast(Any, key.is_closed) is True
            assert isinstance(key, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, key.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.retrieve(
                key="key",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.retrieve(
                key="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.storage.kvs.keys.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.storage.kvs.keys.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ttl_secs=1,
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.kvs.keys.with_raw_response.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.kvs.keys.with_streaming_response.update(
            key="key",
            body=b"Example data",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.update(
                key="key",
                body=b"Example data",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.update(
                key="",
                body=b"Example data",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.storage.kvs.keys.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.storage.kvs.keys.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=1,
            prefix="prefix",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.kvs.keys.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.kvs.keys.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        key = await async_client.storage.kvs.keys.delete(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.kvs.keys.with_raw_response.delete(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.kvs.keys.with_streaming_response.delete(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.delete(
                key="key",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.storage.kvs.keys.with_raw_response.delete(
                key="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
