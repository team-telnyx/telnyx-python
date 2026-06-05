# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    InfringementClaimContestResponse,
    InfringementClaimRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInfringementClaims:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        infringement_claim = client.infringement_claims.retrieve(
            "e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
        )
        assert_matches_type(InfringementClaimRetrieveResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.infringement_claims.with_raw_response.retrieve(
            "e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infringement_claim = response.parse()
        assert_matches_type(InfringementClaimRetrieveResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.infringement_claims.with_streaming_response.retrieve(
            "e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infringement_claim = response.parse()
            assert_matches_type(InfringementClaimRetrieveResponse, infringement_claim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `claim_id` but received ''"):
            client.infringement_claims.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_contest(self, client: Telnyx) -> None:
        infringement_claim = client.infringement_claims.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
        )
        assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_contest_with_all_params(self, client: Telnyx) -> None:
        infringement_claim = client.infringement_claims.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "trademark_registration",
                    "description": "USPTO trademark certificate.",
                }
            ],
        )
        assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_contest(self, client: Telnyx) -> None:
        response = client.infringement_claims.with_raw_response.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infringement_claim = response.parse()
        assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_contest(self, client: Telnyx) -> None:
        with client.infringement_claims.with_streaming_response.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infringement_claim = response.parse()
            assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_contest(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `claim_id` but received ''"):
            client.infringement_claims.with_raw_response.contest(
                claim_id="",
                contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
            )


class TestAsyncInfringementClaims:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        infringement_claim = await async_client.infringement_claims.retrieve(
            "e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
        )
        assert_matches_type(InfringementClaimRetrieveResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.infringement_claims.with_raw_response.retrieve(
            "e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infringement_claim = await response.parse()
        assert_matches_type(InfringementClaimRetrieveResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.infringement_claims.with_streaming_response.retrieve(
            "e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infringement_claim = await response.parse()
            assert_matches_type(InfringementClaimRetrieveResponse, infringement_claim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `claim_id` but received ''"):
            await async_client.infringement_claims.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_contest(self, async_client: AsyncTelnyx) -> None:
        infringement_claim = await async_client.infringement_claims.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
        )
        assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_contest_with_all_params(self, async_client: AsyncTelnyx) -> None:
        infringement_claim = await async_client.infringement_claims.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "trademark_registration",
                    "description": "USPTO trademark certificate.",
                }
            ],
        )
        assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_contest(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.infringement_claims.with_raw_response.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infringement_claim = await response.parse()
        assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_contest(self, async_client: AsyncTelnyx) -> None:
        async with async_client.infringement_claims.with_streaming_response.contest(
            claim_id="e379fbc8-cd83-4bef-a280-a0ac9d00dcf8",
            contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infringement_claim = await response.parse()
            assert_matches_type(InfringementClaimContestResponse, infringement_claim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_contest(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `claim_id` but received ''"):
            await async_client.infringement_claims.with_raw_response.contest(
                claim_id="",
                contest_notes="We own the trademark outright; our registration precedes the claimant by three years. See attached certificate.",
            )
