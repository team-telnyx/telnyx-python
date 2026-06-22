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
from telnyx.types.enterprises import EnterpriseReputationPublicWrapped

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoa:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        loa = client.enterprises.reputation.loa.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        )
        assert_matches_type(EnterpriseReputationPublicWrapped, loa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.loa.with_raw_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa = response.parse()
        assert_matches_type(EnterpriseReputationPublicWrapped, loa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.enterprises.reputation.loa.with_streaming_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa = response.parse()
            assert_matches_type(EnterpriseReputationPublicWrapped, loa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.loa.with_raw_response.update(
                enterprise_id="",
                loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_render(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa = client.enterprises.reputation.loa.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert loa.is_closed
        assert loa.json() == {"foo": "bar"}
        assert cast(Any, loa.is_closed) is True
        assert isinstance(loa, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_render_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa = client.enterprises.reputation.loa.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            agent={
                "administrative_area": "administrative_area",
                "city": "city",
                "contact_email": "dev@stainless.com",
                "contact_name": "contact_name",
                "contact_phone": "+13125550000",
                "contact_title": "contact_title",
                "country": "US",
                "legal_name": "legal_name",
                "postal_code": "postal_code",
                "street_address": "street_address",
                "dba": "dba",
                "extended_address": "extended_address",
            },
            signature={
                "image_base64": "image_base64",
                "signer_name": "signer_name",
            },
        )
        assert loa.is_closed
        assert loa.json() == {"foo": "bar"}
        assert cast(Any, loa.is_closed) is True
        assert isinstance(loa, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_render(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        loa = client.enterprises.reputation.loa.with_raw_response.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert loa.is_closed is True
        assert loa.http_request.headers.get("X-Stainless-Lang") == "python"
        assert loa.json() == {"foo": "bar"}
        assert isinstance(loa, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_render(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.enterprises.reputation.loa.with_streaming_response.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as loa:
            assert not loa.is_closed
            assert loa.http_request.headers.get("X-Stainless-Lang") == "python"

            assert loa.json() == {"foo": "bar"}
            assert cast(Any, loa.is_closed) is True
            assert isinstance(loa, StreamedBinaryAPIResponse)

        assert cast(Any, loa.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_render(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.loa.with_raw_response.render(
                enterprise_id="",
            )


class TestAsyncLoa:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        loa = await async_client.enterprises.reputation.loa.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        )
        assert_matches_type(EnterpriseReputationPublicWrapped, loa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.loa.with_raw_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa = await response.parse()
        assert_matches_type(EnterpriseReputationPublicWrapped, loa, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.loa.with_streaming_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa = await response.parse()
            assert_matches_type(EnterpriseReputationPublicWrapped, loa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.loa.with_raw_response.update(
                enterprise_id="",
                loa_document_id="2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_render(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa = await async_client.enterprises.reputation.loa.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert loa.is_closed
        assert await loa.json() == {"foo": "bar"}
        assert cast(Any, loa.is_closed) is True
        assert isinstance(loa, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_render_with_all_params(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa = await async_client.enterprises.reputation.loa.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            agent={
                "administrative_area": "administrative_area",
                "city": "city",
                "contact_email": "dev@stainless.com",
                "contact_name": "contact_name",
                "contact_phone": "+13125550000",
                "contact_title": "contact_title",
                "country": "US",
                "legal_name": "legal_name",
                "postal_code": "postal_code",
                "street_address": "street_address",
                "dba": "dba",
                "extended_address": "extended_address",
            },
            signature={
                "image_base64": "image_base64",
                "signer_name": "signer_name",
            },
        )
        assert loa.is_closed
        assert await loa.json() == {"foo": "bar"}
        assert cast(Any, loa.is_closed) is True
        assert isinstance(loa, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_render(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        loa = await async_client.enterprises.reputation.loa.with_raw_response.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert loa.is_closed is True
        assert loa.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await loa.json() == {"foo": "bar"}
        assert isinstance(loa, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_render(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/enterprises/4a6192a4-573d-446d-b3ce-aff9117272a6/reputation/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.enterprises.reputation.loa.with_streaming_response.render(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as loa:
            assert not loa.is_closed
            assert loa.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await loa.json() == {"foo": "bar"}
            assert cast(Any, loa.is_closed) is True
            assert isinstance(loa, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, loa.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_render(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.loa.with_raw_response.render(
                enterprise_id="",
            )
