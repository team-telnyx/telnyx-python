# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.external_connections import (
    PhoneNumberListResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        phone_number = client.external_connections.phone_numbers.retrieve(
            phone_number_id="1234567889",
            id="id",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.external_connections.phone_numbers.with_raw_response.retrieve(
            phone_number_id="1234567889",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.external_connections.phone_numbers.with_streaming_response.retrieve(
            phone_number_id="1234567889",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.phone_numbers.with_raw_response.retrieve(
                phone_number_id="1234567889",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.external_connections.phone_numbers.with_raw_response.retrieve(
                phone_number_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        phone_number = client.external_connections.phone_numbers.update(
            phone_number_id="1234567889",
            id="id",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.external_connections.phone_numbers.update(
            phone_number_id="1234567889",
            id="id",
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.external_connections.phone_numbers.with_raw_response.update(
            phone_number_id="1234567889",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.external_connections.phone_numbers.with_streaming_response.update(
            phone_number_id="1234567889",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.phone_numbers.with_raw_response.update(
                phone_number_id="1234567889",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.external_connections.phone_numbers.with_raw_response.update(
                phone_number_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number = client.external_connections.phone_numbers.list(
            id="id",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.external_connections.phone_numbers.list(
            id="id",
            filter={
                "civic_address_id": {"eq": "19990261512338516954"},
                "location_id": {"eq": "19995665508264022121"},
                "phone_number": {
                    "contains": "+1970",
                    "eq": "+19705555098",
                },
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.external_connections.phone_numbers.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.external_connections.phone_numbers.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.phone_numbers.with_raw_response.list(
                id="",
            )


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.external_connections.phone_numbers.retrieve(
            phone_number_id="1234567889",
            id="id",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.phone_numbers.with_raw_response.retrieve(
            phone_number_id="1234567889",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.phone_numbers.with_streaming_response.retrieve(
            phone_number_id="1234567889",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.phone_numbers.with_raw_response.retrieve(
                phone_number_id="1234567889",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.external_connections.phone_numbers.with_raw_response.retrieve(
                phone_number_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.external_connections.phone_numbers.update(
            phone_number_id="1234567889",
            id="id",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.external_connections.phone_numbers.update(
            phone_number_id="1234567889",
            id="id",
            location_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.phone_numbers.with_raw_response.update(
            phone_number_id="1234567889",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.phone_numbers.with_streaming_response.update(
            phone_number_id="1234567889",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.phone_numbers.with_raw_response.update(
                phone_number_id="1234567889",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.external_connections.phone_numbers.with_raw_response.update(
                phone_number_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.external_connections.phone_numbers.list(
            id="id",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.external_connections.phone_numbers.list(
            id="id",
            filter={
                "civic_address_id": {"eq": "19990261512338516954"},
                "location_id": {"eq": "19995665508264022121"},
                "phone_number": {
                    "contains": "+1970",
                    "eq": "+19705555098",
                },
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.phone_numbers.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.phone_numbers.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.phone_numbers.with_raw_response.list(
                id="",
            )
