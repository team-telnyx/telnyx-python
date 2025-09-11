# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    FqdnListResponse,
    FqdnCreateResponse,
    FqdnDeleteResponse,
    FqdnUpdateResponse,
    FqdnRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFqdns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        fqdn = client.fqdns.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
        )
        assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        fqdn = client.fqdns.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
            port=8080,
        )
        assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.fqdns.with_raw_response.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = response.parse()
        assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.fqdns.with_streaming_response.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = response.parse()
            assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        fqdn = client.fqdns.retrieve(
            "id",
        )
        assert_matches_type(FqdnRetrieveResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.fqdns.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = response.parse()
        assert_matches_type(FqdnRetrieveResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.fqdns.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = response.parse()
            assert_matches_type(FqdnRetrieveResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fqdns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        fqdn = client.fqdns.update(
            id="id",
        )
        assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        fqdn = client.fqdns.update(
            id="id",
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
            port=8080,
        )
        assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.fqdns.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = response.parse()
        assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.fqdns.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = response.parse()
            assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fqdns.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        fqdn = client.fqdns.list()
        assert_matches_type(FqdnListResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        fqdn = client.fqdns.list(
            filter={
                "connection_id": "connection_id",
                "dns_record_type": "a",
                "fqdn": "example.com",
                "port": 5060,
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(FqdnListResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.fqdns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = response.parse()
        assert_matches_type(FqdnListResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.fqdns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = response.parse()
            assert_matches_type(FqdnListResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        fqdn = client.fqdns.delete(
            "id",
        )
        assert_matches_type(FqdnDeleteResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.fqdns.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = response.parse()
        assert_matches_type(FqdnDeleteResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.fqdns.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = response.parse()
            assert_matches_type(FqdnDeleteResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fqdns.with_raw_response.delete(
                "",
            )


class TestAsyncFqdns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
        )
        assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
            port=8080,
        )
        assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdns.with_raw_response.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = await response.parse()
        assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdns.with_streaming_response.create(
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = await response.parse()
            assert_matches_type(FqdnCreateResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.retrieve(
            "id",
        )
        assert_matches_type(FqdnRetrieveResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdns.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = await response.parse()
        assert_matches_type(FqdnRetrieveResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdns.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = await response.parse()
            assert_matches_type(FqdnRetrieveResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fqdns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.update(
            id="id",
        )
        assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.update(
            id="id",
            connection_id="1516447646313612565",
            dns_record_type="a",
            fqdn="example.com",
            port=8080,
        )
        assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdns.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = await response.parse()
        assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdns.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = await response.parse()
            assert_matches_type(FqdnUpdateResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fqdns.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.list()
        assert_matches_type(FqdnListResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.list(
            filter={
                "connection_id": "connection_id",
                "dns_record_type": "a",
                "fqdn": "example.com",
                "port": 5060,
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(FqdnListResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = await response.parse()
        assert_matches_type(FqdnListResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = await response.parse()
            assert_matches_type(FqdnListResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        fqdn = await async_client.fqdns.delete(
            "id",
        )
        assert_matches_type(FqdnDeleteResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fqdns.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fqdn = await response.parse()
        assert_matches_type(FqdnDeleteResponse, fqdn, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fqdns.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fqdn = await response.parse()
            assert_matches_type(FqdnDeleteResponse, fqdn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fqdns.with_raw_response.delete(
                "",
            )
