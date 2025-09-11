# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.addresses import (
    ActionValidateResponse,
    ActionAcceptSuggestionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_accept_suggestions(self, client: Telnyx) -> None:
        action = client.addresses.actions.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_accept_suggestions_with_all_params(self, client: Telnyx) -> None:
        action = client.addresses.actions.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="id",
        )
        assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_accept_suggestions(self, client: Telnyx) -> None:
        response = client.addresses.actions.with_raw_response.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_accept_suggestions(self, client: Telnyx) -> None:
        with client.addresses.actions.with_streaming_response.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_accept_suggestions(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.addresses.actions.with_raw_response.accept_suggestions(
                path_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate(self, client: Telnyx) -> None:
        action = client.addresses.actions.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
        )
        assert_matches_type(ActionValidateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: Telnyx) -> None:
        action = client.addresses.actions.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
            administrative_area="TX",
            extended_address="14th Floor",
            locality="Austin",
        )
        assert_matches_type(ActionValidateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Telnyx) -> None:
        response = client.addresses.actions.with_raw_response.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionValidateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: Telnyx) -> None:
        with client.addresses.actions.with_streaming_response.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionValidateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_accept_suggestions(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.addresses.actions.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_accept_suggestions_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.addresses.actions.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_id="id",
        )
        assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_accept_suggestions(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.addresses.actions.with_raw_response.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_accept_suggestions(self, async_client: AsyncTelnyx) -> None:
        async with async_client.addresses.actions.with_streaming_response.accept_suggestions(
            path_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionAcceptSuggestionsResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_accept_suggestions(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.addresses.actions.with_raw_response.accept_suggestions(
                path_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.addresses.actions.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
        )
        assert_matches_type(ActionValidateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.addresses.actions.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
            administrative_area="TX",
            extended_address="14th Floor",
            locality="Austin",
        )
        assert_matches_type(ActionValidateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.addresses.actions.with_raw_response.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionValidateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.addresses.actions.with_streaming_response.validate(
            country_code="US",
            postal_code="78701",
            street_address="600 Congress Avenue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionValidateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True
