# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.enterprises.reputation import ExternalVerificationWrapped

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        external_verification = client.enterprises.reputation.external_verification.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
        )
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        external_verification = client.enterprises.reputation.external_verification.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
            phone_numbers=["+13125550142"],
        )
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.external_verification.with_raw_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_verification = response.parse()
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.enterprises.reputation.external_verification.with_streaming_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_verification = response.parse()
            assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.external_verification.with_raw_response.create(
                enterprise_id="",
                document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        external_verification = client.enterprises.reputation.external_verification.list(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.external_verification.with_raw_response.list(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_verification = response.parse()
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.enterprises.reputation.external_verification.with_streaming_response.list(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_verification = response.parse()
            assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.external_verification.with_raw_response.list(
                "",
            )


class TestAsyncExternalVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        external_verification = await async_client.enterprises.reputation.external_verification.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
        )
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        external_verification = await async_client.enterprises.reputation.external_verification.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
            phone_numbers=["+13125550142"],
        )
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.external_verification.with_raw_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_verification = await response.parse()
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.external_verification.with_streaming_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_verification = await response.parse()
            assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.external_verification.with_raw_response.create(
                enterprise_id="",
                document_ids=["2a7e8337-e803-4057-a4ae-26c40eb0bc6c"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        external_verification = await async_client.enterprises.reputation.external_verification.list(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.external_verification.with_raw_response.list(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_verification = await response.parse()
        assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.external_verification.with_streaming_response.list(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_verification = await response.parse()
            assert_matches_type(ExternalVerificationWrapped, external_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.external_verification.with_raw_response.list(
                "",
            )
