# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    AdditionalDocumentListResponse,
    AdditionalDocumentCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdditionalDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        additional_document = client.porting_orders.additional_documents.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        additional_document = client.porting_orders.additional_documents.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_documents=[
                {
                    "document_id": "22771a52-c43a-4539-80db-9dd9ec36e237",
                    "document_type": "loa",
                },
                {
                    "document_id": "d91474e6-4ebc-4ec1-b379-c596eeb405d6",
                    "document_type": "invoice",
                },
            ],
        )
        assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting_orders.additional_documents.with_raw_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        additional_document = response.parse()
        assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting_orders.additional_documents.with_streaming_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            additional_document = response.parse()
            assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.additional_documents.with_raw_response.create(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        additional_document = client.porting_orders.additional_documents.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        additional_document = client.porting_orders.additional_documents.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={"document_type": ["loa"]},
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.additional_documents.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        additional_document = response.parse()
        assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.additional_documents.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            additional_document = response.parse()
            assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.additional_documents.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        additional_document = client.porting_orders.additional_documents.delete(
            additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert additional_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.porting_orders.additional_documents.with_raw_response.delete(
            additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        additional_document = response.parse()
        assert additional_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.porting_orders.additional_documents.with_streaming_response.delete(
            additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            additional_document = response.parse()
            assert additional_document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.additional_documents.with_raw_response.delete(
                additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `additional_document_id` but received ''"
        ):
            client.porting_orders.additional_documents.with_raw_response.delete(
                additional_document_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncAdditionalDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        additional_document = await async_client.porting_orders.additional_documents.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        additional_document = await async_client.porting_orders.additional_documents.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_documents=[
                {
                    "document_id": "22771a52-c43a-4539-80db-9dd9ec36e237",
                    "document_type": "loa",
                },
                {
                    "document_id": "d91474e6-4ebc-4ec1-b379-c596eeb405d6",
                    "document_type": "invoice",
                },
            ],
        )
        assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.additional_documents.with_raw_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        additional_document = await response.parse()
        assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.additional_documents.with_streaming_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            additional_document = await response.parse()
            assert_matches_type(AdditionalDocumentCreateResponse, additional_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.additional_documents.with_raw_response.create(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        additional_document = await async_client.porting_orders.additional_documents.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        additional_document = await async_client.porting_orders.additional_documents.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter={"document_type": ["loa"]},
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.additional_documents.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        additional_document = await response.parse()
        assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.additional_documents.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            additional_document = await response.parse()
            assert_matches_type(AdditionalDocumentListResponse, additional_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.additional_documents.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        additional_document = await async_client.porting_orders.additional_documents.delete(
            additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert additional_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.additional_documents.with_raw_response.delete(
            additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        additional_document = await response.parse()
        assert additional_document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.additional_documents.with_streaming_response.delete(
            additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            additional_document = await response.parse()
            assert additional_document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.additional_documents.with_raw_response.delete(
                additional_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `additional_document_id` but received ''"
        ):
            await async_client.porting_orders.additional_documents.with_raw_response.delete(
                additional_document_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
