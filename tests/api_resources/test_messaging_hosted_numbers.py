# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MessagingHostedNumberDeleteResponse,
    MessagingHostedNumberUpdateResponse,
    MessagingHostedNumberRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.shared import PhoneNumberWithMessagingSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessagingHostedNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        messaging_hosted_number = client.messaging_hosted_numbers.retrieve(
            "id",
        )
        assert_matches_type(MessagingHostedNumberRetrieveResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messaging_hosted_numbers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = response.parse()
        assert_matches_type(MessagingHostedNumberRetrieveResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messaging_hosted_numbers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = response.parse()
            assert_matches_type(MessagingHostedNumberRetrieveResponse, messaging_hosted_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        messaging_hosted_number = client.messaging_hosted_numbers.update(
            id="id",
        )
        assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        messaging_hosted_number = client.messaging_hosted_numbers.update(
            id="id",
            messaging_product="P2P",
            messaging_profile_id="dd50eba1-a0c0-4563-9925-b25e842a7cb6",
            tags=["string"],
        )
        assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.messaging_hosted_numbers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = response.parse()
        assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.messaging_hosted_numbers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = response.parse()
            assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_numbers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        messaging_hosted_number = client.messaging_hosted_numbers.list()
        assert_matches_type(
            SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        messaging_hosted_number = client.messaging_hosted_numbers.list(
            filter_messaging_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_phone_number="filter[phone_number]",
            filter_phone_number_contains="filter[phone_number][contains]",
            page_number=0,
            page_size=0,
            sort_phone_number="asc",
        )
        assert_matches_type(
            SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_hosted_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_hosted_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        messaging_hosted_number = client.messaging_hosted_numbers.delete(
            "id",
        )
        assert_matches_type(MessagingHostedNumberDeleteResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.messaging_hosted_numbers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = response.parse()
        assert_matches_type(MessagingHostedNumberDeleteResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.messaging_hosted_numbers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = response.parse()
            assert_matches_type(MessagingHostedNumberDeleteResponse, messaging_hosted_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_numbers.with_raw_response.delete(
                "",
            )


class TestAsyncMessagingHostedNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number = await async_client.messaging_hosted_numbers.retrieve(
            "id",
        )
        assert_matches_type(MessagingHostedNumberRetrieveResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_numbers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = await response.parse()
        assert_matches_type(MessagingHostedNumberRetrieveResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_numbers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = await response.parse()
            assert_matches_type(MessagingHostedNumberRetrieveResponse, messaging_hosted_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number = await async_client.messaging_hosted_numbers.update(
            id="id",
        )
        assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number = await async_client.messaging_hosted_numbers.update(
            id="id",
            messaging_product="P2P",
            messaging_profile_id="dd50eba1-a0c0-4563-9925-b25e842a7cb6",
            tags=["string"],
        )
        assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_numbers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = await response.parse()
        assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_numbers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = await response.parse()
            assert_matches_type(MessagingHostedNumberUpdateResponse, messaging_hosted_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_numbers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number = await async_client.messaging_hosted_numbers.list()
        assert_matches_type(
            AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number = await async_client.messaging_hosted_numbers.list(
            filter_messaging_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_phone_number="filter[phone_number]",
            filter_phone_number_contains="filter[phone_number][contains]",
            page_number=0,
            page_size=0,
            sort_phone_number="asc",
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings], messaging_hosted_number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number = await async_client.messaging_hosted_numbers.delete(
            "id",
        )
        assert_matches_type(MessagingHostedNumberDeleteResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_numbers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number = await response.parse()
        assert_matches_type(MessagingHostedNumberDeleteResponse, messaging_hosted_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_numbers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number = await response.parse()
            assert_matches_type(MessagingHostedNumberDeleteResponse, messaging_hosted_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_numbers.with_raw_response.delete(
                "",
            )
