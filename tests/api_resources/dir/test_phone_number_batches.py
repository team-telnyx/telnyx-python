# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.dir import (
    PhoneNumberBatch,
    PhoneNumberBatchRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        phone_number_batch = client.dir.phone_number_batches.retrieve(
            batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(PhoneNumberBatchRetrieveResponse, phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.dir.phone_number_batches.with_raw_response.retrieve(
            batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_batch = response.parse()
        assert_matches_type(PhoneNumberBatchRetrieveResponse, phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.dir.phone_number_batches.with_streaming_response.retrieve(
            batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_batch = response.parse()
            assert_matches_type(PhoneNumberBatchRetrieveResponse, phone_number_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.phone_number_batches.with_raw_response.retrieve(
                batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
                dir_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.dir.phone_number_batches.with_raw_response.retrieve(
                batch_id="",
                dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number_batch = client.dir.phone_number_batches.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(SyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number_batch = client.dir.phone_number_batches.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            filter_status="submitted",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(SyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dir.phone_number_batches.with_raw_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_batch = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dir.phone_number_batches.with_streaming_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_batch = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.phone_number_batches.with_raw_response.list(
                dir_id="",
            )


class TestAsyncPhoneNumberBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        phone_number_batch = await async_client.dir.phone_number_batches.retrieve(
            batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(PhoneNumberBatchRetrieveResponse, phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.phone_number_batches.with_raw_response.retrieve(
            batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_batch = await response.parse()
        assert_matches_type(PhoneNumberBatchRetrieveResponse, phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.phone_number_batches.with_streaming_response.retrieve(
            batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_batch = await response.parse()
            assert_matches_type(PhoneNumberBatchRetrieveResponse, phone_number_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.phone_number_batches.with_raw_response.retrieve(
                batch_id="0a4b1f5e-2f12-4c0c-9a98-9b3a7d8b8e62",
                dir_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.dir.phone_number_batches.with_raw_response.retrieve(
                batch_id="",
                dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number_batch = await async_client.dir.phone_number_batches.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_batch = await async_client.dir.phone_number_batches.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            filter_status="submitted",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.phone_number_batches.with_raw_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_batch = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.phone_number_batches.with_streaming_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_batch = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberBatch], phone_number_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.phone_number_batches.with_raw_response.list(
                dir_id="",
            )
