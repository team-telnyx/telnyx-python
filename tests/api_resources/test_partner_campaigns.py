# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TelnyxDownstreamCampaign,
    PartnerCampaignListResponse,
    PartnerCampaignListSharedByMeResponse,
    PartnerCampaignRetrieveSharingStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPartnerCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.retrieve(
            "campaignId",
        )
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.partner_campaigns.with_raw_response.retrieve(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.partner_campaigns.with_streaming_response.retrieve(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.partner_campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.update(
            campaign_id="campaignId",
        )
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.update(
            campaign_id="campaignId",
            webhook_failover_url="https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
        )
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.partner_campaigns.with_raw_response.update(
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.partner_campaigns.with_streaming_response.update(
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.partner_campaigns.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.list()
        assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.list(
            page=0,
            records_per_page=0,
            sort="assignedPhoneNumbersCount",
        )
        assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.partner_campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.partner_campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_shared_by_me(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.list_shared_by_me()
        assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_shared_by_me_with_all_params(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.list_shared_by_me(
            page=0,
            records_per_page=0,
        )
        assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_shared_by_me(self, client: Telnyx) -> None:
        response = client.partner_campaigns.with_raw_response.list_shared_by_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_shared_by_me(self, client: Telnyx) -> None:
        with client.partner_campaigns.with_streaming_response.list_shared_by_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_sharing_status(self, client: Telnyx) -> None:
        partner_campaign = client.partner_campaigns.retrieve_sharing_status(
            "campaignId",
        )
        assert_matches_type(PartnerCampaignRetrieveSharingStatusResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sharing_status(self, client: Telnyx) -> None:
        response = client.partner_campaigns.with_raw_response.retrieve_sharing_status(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = response.parse()
        assert_matches_type(PartnerCampaignRetrieveSharingStatusResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sharing_status(self, client: Telnyx) -> None:
        with client.partner_campaigns.with_streaming_response.retrieve_sharing_status(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = response.parse()
            assert_matches_type(PartnerCampaignRetrieveSharingStatusResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_sharing_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.partner_campaigns.with_raw_response.retrieve_sharing_status(
                "",
            )


class TestAsyncPartnerCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.retrieve(
            "campaignId",
        )
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.partner_campaigns.with_raw_response.retrieve(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.partner_campaigns.with_streaming_response.retrieve(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.partner_campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.update(
            campaign_id="campaignId",
        )
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.update(
            campaign_id="campaignId",
            webhook_failover_url="https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
        )
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.partner_campaigns.with_raw_response.update(
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.partner_campaigns.with_streaming_response.update(
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(TelnyxDownstreamCampaign, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.partner_campaigns.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.list()
        assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.list(
            page=0,
            records_per_page=0,
            sort="assignedPhoneNumbersCount",
        )
        assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.partner_campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.partner_campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(PartnerCampaignListResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_shared_by_me(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.list_shared_by_me()
        assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_shared_by_me_with_all_params(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.list_shared_by_me(
            page=0,
            records_per_page=0,
        )
        assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_shared_by_me(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.partner_campaigns.with_raw_response.list_shared_by_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_shared_by_me(self, async_client: AsyncTelnyx) -> None:
        async with async_client.partner_campaigns.with_streaming_response.list_shared_by_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(PartnerCampaignListSharedByMeResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_sharing_status(self, async_client: AsyncTelnyx) -> None:
        partner_campaign = await async_client.partner_campaigns.retrieve_sharing_status(
            "campaignId",
        )
        assert_matches_type(PartnerCampaignRetrieveSharingStatusResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sharing_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.partner_campaigns.with_raw_response.retrieve_sharing_status(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        partner_campaign = await response.parse()
        assert_matches_type(PartnerCampaignRetrieveSharingStatusResponse, partner_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sharing_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.partner_campaigns.with_streaming_response.retrieve_sharing_status(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            partner_campaign = await response.parse()
            assert_matches_type(PartnerCampaignRetrieveSharingStatusResponse, partner_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_sharing_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.partner_campaigns.with_raw_response.retrieve_sharing_status(
                "",
            )
