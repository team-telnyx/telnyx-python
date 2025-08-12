# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    NumberReservationListResponse,
    NumberReservationCreateResponse,
    NumberReservationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberReservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        number_reservation = client.number_reservations.create()
        assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        number_reservation = client.number_reservations.create(
            customer_reference="MY REF 001",
            phone_numbers=[{"phone_number": "+19705555098"}],
        )
        assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.number_reservations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reservation = response.parse()
        assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.number_reservations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reservation = response.parse()
            assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number_reservation = client.number_reservations.retrieve(
            "number_reservation_id",
        )
        assert_matches_type(NumberReservationRetrieveResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_reservations.with_raw_response.retrieve(
            "number_reservation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reservation = response.parse()
        assert_matches_type(NumberReservationRetrieveResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_reservations.with_streaming_response.retrieve(
            "number_reservation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reservation = response.parse()
            assert_matches_type(NumberReservationRetrieveResponse, number_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_reservation_id` but received ''"):
            client.number_reservations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        number_reservation = client.number_reservations.list()
        assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        number_reservation = client.number_reservations.list(
            filter={
                "created_at": {
                    "gt": "gt",
                    "lt": "lt",
                },
                "customer_reference": "customer_reference",
                "phone_numbers_phone_number": "phone_numbers.phone_number",
                "status": "status",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.number_reservations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reservation = response.parse()
        assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.number_reservations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reservation = response.parse()
            assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNumberReservations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        number_reservation = await async_client.number_reservations.create()
        assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_reservation = await async_client.number_reservations.create(
            customer_reference="MY REF 001",
            phone_numbers=[{"phone_number": "+19705555098"}],
        )
        assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_reservations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reservation = await response.parse()
        assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_reservations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reservation = await response.parse()
            assert_matches_type(NumberReservationCreateResponse, number_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number_reservation = await async_client.number_reservations.retrieve(
            "number_reservation_id",
        )
        assert_matches_type(NumberReservationRetrieveResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_reservations.with_raw_response.retrieve(
            "number_reservation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reservation = await response.parse()
        assert_matches_type(NumberReservationRetrieveResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_reservations.with_streaming_response.retrieve(
            "number_reservation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reservation = await response.parse()
            assert_matches_type(NumberReservationRetrieveResponse, number_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number_reservation_id` but received ''"):
            await async_client.number_reservations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        number_reservation = await async_client.number_reservations.list()
        assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_reservation = await async_client.number_reservations.list(
            filter={
                "created_at": {
                    "gt": "gt",
                    "lt": "lt",
                },
                "customer_reference": "customer_reference",
                "phone_numbers_phone_number": "phone_numbers.phone_number",
                "status": "status",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_reservations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reservation = await response.parse()
        assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_reservations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reservation = await response.parse()
            assert_matches_type(NumberReservationListResponse, number_reservation, path=["response"])

        assert cast(Any, response.is_closed) is True
