# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PronunciationDictListResponse,
    PronunciationDictCreateResponse,
    PronunciationDictUpdateResponse,
    PronunciationDictRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPronunciationDicts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.create(
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Brand Names",
        )
        assert_matches_type(PronunciationDictCreateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.pronunciation_dicts.with_raw_response.create(
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Brand Names",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = response.parse()
        assert_matches_type(PronunciationDictCreateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.pronunciation_dicts.with_streaming_response.create(
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Brand Names",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = response.parse()
            assert_matches_type(PronunciationDictCreateResponse, pronunciation_dict, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.retrieve(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )
        assert_matches_type(PronunciationDictRetrieveResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.pronunciation_dicts.with_raw_response.retrieve(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = response.parse()
        assert_matches_type(PronunciationDictRetrieveResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.pronunciation_dicts.with_streaming_response.retrieve(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = response.parse()
            assert_matches_type(PronunciationDictRetrieveResponse, pronunciation_dict, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pronunciation_dicts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )
        assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Updated Brand Names",
        )
        assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.pronunciation_dicts.with_raw_response.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = response.parse()
        assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.pronunciation_dicts.with_streaming_response.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = response.parse()
            assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pronunciation_dicts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.list()
        assert_matches_type(
            SyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            SyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.pronunciation_dicts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.pronunciation_dicts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        pronunciation_dict = client.pronunciation_dicts.delete(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )
        assert pronunciation_dict is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.pronunciation_dicts.with_raw_response.delete(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = response.parse()
        assert pronunciation_dict is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.pronunciation_dicts.with_streaming_response.delete(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = response.parse()
            assert pronunciation_dict is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.pronunciation_dicts.with_raw_response.delete(
                "",
            )


class TestAsyncPronunciationDicts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.create(
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Brand Names",
        )
        assert_matches_type(PronunciationDictCreateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pronunciation_dicts.with_raw_response.create(
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Brand Names",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = await response.parse()
        assert_matches_type(PronunciationDictCreateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pronunciation_dicts.with_streaming_response.create(
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Brand Names",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = await response.parse()
            assert_matches_type(PronunciationDictCreateResponse, pronunciation_dict, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.retrieve(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )
        assert_matches_type(PronunciationDictRetrieveResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pronunciation_dicts.with_raw_response.retrieve(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = await response.parse()
        assert_matches_type(PronunciationDictRetrieveResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pronunciation_dicts.with_streaming_response.retrieve(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = await response.parse()
            assert_matches_type(PronunciationDictRetrieveResponse, pronunciation_dict, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pronunciation_dicts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )
        assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
            items=[
                {
                    "alias": "tel-nicks",
                    "text": "Telnyx",
                    "type": "alias",
                }
            ],
            name="Updated Brand Names",
        )
        assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pronunciation_dicts.with_raw_response.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = await response.parse()
        assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pronunciation_dicts.with_streaming_response.update(
            id="c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = await response.parse()
            assert_matches_type(PronunciationDictUpdateResponse, pronunciation_dict, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pronunciation_dicts.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.list()
        assert_matches_type(
            AsyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pronunciation_dicts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pronunciation_dicts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[PronunciationDictListResponse], pronunciation_dict, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        pronunciation_dict = await async_client.pronunciation_dicts.delete(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )
        assert pronunciation_dict is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.pronunciation_dicts.with_raw_response.delete(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pronunciation_dict = await response.parse()
        assert pronunciation_dict is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.pronunciation_dicts.with_streaming_response.delete(
            "c215a3e1-be41-4701-97e8-1d3c22f9a5b7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pronunciation_dict = await response.parse()
            assert pronunciation_dict is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.pronunciation_dicts.with_raw_response.delete(
                "",
            )
