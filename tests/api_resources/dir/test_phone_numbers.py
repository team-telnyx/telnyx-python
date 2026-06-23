# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.dir import (
    DirPhoneNumber,
    PhoneNumberAddResponse,
    PhoneNumberRemoveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number = client.dir.phone_numbers.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.dir.phone_numbers.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            page_number=1,
            page_size=20,
            status="submitted",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dir.phone_numbers.with_raw_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dir.phone_numbers.with_streaming_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.phone_numbers.with_raw_response.list(
                dir_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Telnyx) -> None:
        phone_number = client.dir.phone_numbers.add(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "letter_of_authorization",
                }
            ],
            phone_numbers=["+19493253498", "+12134445566"],
        )
        assert_matches_type(PhoneNumberAddResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Telnyx) -> None:
        response = client.dir.phone_numbers.with_raw_response.add(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "letter_of_authorization",
                }
            ],
            phone_numbers=["+19493253498", "+12134445566"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberAddResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Telnyx) -> None:
        with client.dir.phone_numbers.with_streaming_response.add(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "letter_of_authorization",
                }
            ],
            phone_numbers=["+19493253498", "+12134445566"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberAddResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.phone_numbers.with_raw_response.add(
                dir_id="",
                documents=[
                    {
                        "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                        "document_type": "letter_of_authorization",
                    }
                ],
                phone_numbers=["+19493253498", "+12134445566"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Telnyx) -> None:
        phone_number = client.dir.phone_numbers.remove(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            phone_numbers=["+19493253498"],
        )
        assert_matches_type(PhoneNumberRemoveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Telnyx) -> None:
        response = client.dir.phone_numbers.with_raw_response.remove(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            phone_numbers=["+19493253498"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberRemoveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Telnyx) -> None:
        with client.dir.phone_numbers.with_streaming_response.remove(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            phone_numbers=["+19493253498"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberRemoveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.phone_numbers.with_raw_response.remove(
                dir_id="",
                phone_numbers=["+19493253498"],
            )


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.dir.phone_numbers.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.dir.phone_numbers.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            page_number=1,
            page_size=20,
            status="submitted",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.phone_numbers.with_raw_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.phone_numbers.with_streaming_response.list(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[DirPhoneNumber], phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.phone_numbers.with_raw_response.list(
                dir_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.dir.phone_numbers.add(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "letter_of_authorization",
                }
            ],
            phone_numbers=["+19493253498", "+12134445566"],
        )
        assert_matches_type(PhoneNumberAddResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.phone_numbers.with_raw_response.add(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "letter_of_authorization",
                }
            ],
            phone_numbers=["+19493253498", "+12134445566"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberAddResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.phone_numbers.with_streaming_response.add(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "letter_of_authorization",
                }
            ],
            phone_numbers=["+19493253498", "+12134445566"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberAddResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.phone_numbers.with_raw_response.add(
                dir_id="",
                documents=[
                    {
                        "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                        "document_type": "letter_of_authorization",
                    }
                ],
                phone_numbers=["+19493253498", "+12134445566"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.dir.phone_numbers.remove(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            phone_numbers=["+19493253498"],
        )
        assert_matches_type(PhoneNumberRemoveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.phone_numbers.with_raw_response.remove(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            phone_numbers=["+19493253498"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberRemoveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.phone_numbers.with_streaming_response.remove(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            phone_numbers=["+19493253498"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberRemoveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.phone_numbers.with_raw_response.remove(
                dir_id="",
                phone_numbers=["+19493253498"],
            )
