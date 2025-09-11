# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import CampaignBuilderCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCampaignBuilder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        campaign_builder = client.campaign_builder.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
        )
        assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        campaign_builder = client.campaign_builder.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
            age_gated=True,
            auto_renewal=True,
            direct_lending=True,
            embedded_link=True,
            embedded_link_sample="embeddedLinkSample",
            embedded_phone=True,
            help_keywords="helpKeywords",
            help_message="helpMessage",
            message_flow="messageFlow",
            mno_ids=[0],
            number_pool=True,
            optin_keywords="optinKeywords",
            optin_message="optinMessage",
            optout_keywords="optoutKeywords",
            optout_message="optoutMessage",
            privacy_policy_link="privacyPolicyLink",
            reference_id="referenceId",
            reseller_id="resellerId",
            sample1="sample1",
            sample2="sample2",
            sample3="sample3",
            sample4="sample4",
            sample5="sample5",
            subscriber_help=True,
            subscriber_optin=True,
            subscriber_optout=True,
            sub_usecases=["string"],
            tag=["string"],
            terms_and_conditions=True,
            terms_and_conditions_link="termsAndConditionsLink",
            webhook_failover_url="https://webhook.com/93711262-23e5-4048-a966-c0b2a16d5963",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
        )
        assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.campaign_builder.with_raw_response.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign_builder = response.parse()
        assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.campaign_builder.with_streaming_response.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign_builder = response.parse()
            assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCampaignBuilder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        campaign_builder = await async_client.campaign_builder.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
        )
        assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        campaign_builder = await async_client.campaign_builder.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
            age_gated=True,
            auto_renewal=True,
            direct_lending=True,
            embedded_link=True,
            embedded_link_sample="embeddedLinkSample",
            embedded_phone=True,
            help_keywords="helpKeywords",
            help_message="helpMessage",
            message_flow="messageFlow",
            mno_ids=[0],
            number_pool=True,
            optin_keywords="optinKeywords",
            optin_message="optinMessage",
            optout_keywords="optoutKeywords",
            optout_message="optoutMessage",
            privacy_policy_link="privacyPolicyLink",
            reference_id="referenceId",
            reseller_id="resellerId",
            sample1="sample1",
            sample2="sample2",
            sample3="sample3",
            sample4="sample4",
            sample5="sample5",
            subscriber_help=True,
            subscriber_optin=True,
            subscriber_optout=True,
            sub_usecases=["string"],
            tag=["string"],
            terms_and_conditions=True,
            terms_and_conditions_link="termsAndConditionsLink",
            webhook_failover_url="https://webhook.com/93711262-23e5-4048-a966-c0b2a16d5963",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
        )
        assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.campaign_builder.with_raw_response.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign_builder = await response.parse()
        assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.campaign_builder.with_streaming_response.create(
            brand_id="brandId",
            description="description",
            usecase="usecase",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign_builder = await response.parse()
            assert_matches_type(CampaignBuilderCreateResponse, campaign_builder, path=["response"])

        assert cast(Any, response.is_closed) is True
