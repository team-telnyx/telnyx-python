# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.number_10dlc import (
    PartnerCampaignRetrieveSharingResponse,
    PartnerCampaignRetrieveSharedByMeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPartnerCampaign:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_shared_by_me(self, client: Telnyx) -> None:
        partner_campaign = client.number_10dlc.partner_campaign.retrieve_shared_by_me()
        assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_shared_by_me_with_all_params(self, client: Telnyx) -> None:
        partner_campaign = client.number_10dlc.partner_campaign.retrieve_shared_by_me(
            page=0,
            records_per_page=0,
        )
        assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_shared_by_me(self, client: Telnyx) -> None:
        response = client.number_10dlc.partner_campaign.with_raw_response.retrieve_shared_by_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_shared_by_me(self, client: Telnyx) -> None:
        with client.number_10dlc.partner_campaign.with_streaming_response.retrieve_shared_by_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_sharing(self, client: Telnyx) -> None:
        partner_campaign = client.number_10dlc.partner_campaign.retrieve_sharing(
            "campaignId",
        )
        assert_matches_type(PartnerCampaignRetrieveSharingResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sharing(self, client: Telnyx) -> None:
        response = client.number_10dlc.partner_campaign.with_raw_response.retrieve_sharing(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(PartnerCampaignRetrieveSharingResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sharing(self, client: Telnyx) -> None:
        with client.number_10dlc.partner_campaign.with_streaming_response.retrieve_sharing(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(PartnerCampaignRetrieveSharingResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_sharing(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.partner_campaign.with_raw_response.retrieve_sharing(
                "",
            )


class TestAsyncPartnerCampaign:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_shared_by_me(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.number_10dlc.partner_campaign.retrieve_shared_by_me()
        assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_shared_by_me_with_all_params(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.number_10dlc.partner_campaign.retrieve_shared_by_me(
            page=0,
            records_per_page=0,
        )
        assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_shared_by_me(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.partner_campaign.with_raw_response.retrieve_shared_by_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_shared_by_me(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.number_10dlc.partner_campaign.with_streaming_response.retrieve_shared_by_me()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(PartnerCampaignRetrieveSharedByMeResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.number_10dlc.partner_campaign.retrieve_sharing(
            "campaignId",
        )
        assert_matches_type(PartnerCampaignRetrieveSharingResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.partner_campaign.with_raw_response.retrieve_sharing(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(PartnerCampaignRetrieveSharingResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.partner_campaign.with_streaming_response.retrieve_sharing(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(PartnerCampaignRetrieveSharingResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.partner_campaign.with_raw_response.retrieve_sharing(
                "",
            )
