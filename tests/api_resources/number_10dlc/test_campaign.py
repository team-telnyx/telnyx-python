# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import TelnyxCampaignCsp
from telnyx.types.number_10dlc import (
    CampaignListResponse,
    CampaignAppealResponse,
    CampaignDeleteResponse,
    CampaignRetrieveSharingResponse,
    CampaignRetrieveMnoMetadataResponse,
    CampaignRetrieveOperationStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCampaign:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.retrieve(
            "campaignId",
        )
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.retrieve(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.retrieve(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.update(
            campaign_id="campaignId",
        )
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.update(
            campaign_id="campaignId",
            auto_renewal=True,
            help_message="helpMessage",
            message_flow="messageFlow",
            reseller_id="resellerId",
            sample1="sample1",
            sample2="sample2",
            sample3="sample3",
            sample4="sample4",
            sample5="sample5",
            webhook_failover_url="webhookFailoverURL",
            webhook_url="webhookURL",
        )
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.update(
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.update(
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.list(
            brand_id="brandId",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.list(
            brand_id="brandId",
            page=0,
            records_per_page=0,
            sort="assignedPhoneNumbersCount",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.list(
            brand_id="brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.list(
            brand_id="brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.delete(
            "campaignId",
        )
        assert_matches_type(CampaignDeleteResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.delete(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignDeleteResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.delete(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignDeleteResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_appeal(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.appeal(
            campaign_id="5eb13888-32b7-4cab-95e6-d834dde21d64",
            appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
        )
        assert_matches_type(CampaignAppealResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_appeal(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.appeal(
            campaign_id="5eb13888-32b7-4cab-95e6-d834dde21d64",
            appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignAppealResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_appeal(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.appeal(
            campaign_id="5eb13888-32b7-4cab-95e6-d834dde21d64",
            appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignAppealResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_appeal(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.appeal(
                campaign_id="",
                appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_mno_metadata(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.retrieve_mno_metadata(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveMnoMetadataResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_mno_metadata(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.retrieve_mno_metadata(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignRetrieveMnoMetadataResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_mno_metadata(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.retrieve_mno_metadata(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignRetrieveMnoMetadataResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_mno_metadata(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.retrieve_mno_metadata(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_operation_status(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.retrieve_operation_status(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveOperationStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_operation_status(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.retrieve_operation_status(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignRetrieveOperationStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_operation_status(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.retrieve_operation_status(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignRetrieveOperationStatusResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_operation_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.retrieve_operation_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_sharing(self, client: Telnyx) -> None:
        campaign = client.number_10dlc.campaign.retrieve_sharing(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveSharingResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sharing(self, client: Telnyx) -> None:
        response = client.number_10dlc.campaign.with_raw_response.retrieve_sharing(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignRetrieveSharingResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sharing(self, client: Telnyx) -> None:
        with client.number_10dlc.campaign.with_streaming_response.retrieve_sharing(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignRetrieveSharingResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_sharing(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.number_10dlc.campaign.with_raw_response.retrieve_sharing(
                "",
            )


class TestAsyncCampaign:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.retrieve(
            "campaignId",
        )
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.retrieve(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.retrieve(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.update(
            campaign_id="campaignId",
        )
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.update(
            campaign_id="campaignId",
            auto_renewal=True,
            help_message="helpMessage",
            message_flow="messageFlow",
            reseller_id="resellerId",
            sample1="sample1",
            sample2="sample2",
            sample3="sample3",
            sample4="sample4",
            sample5="sample5",
            webhook_failover_url="webhookFailoverURL",
            webhook_url="webhookURL",
        )
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.update(
            campaign_id="campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.update(
            campaign_id="campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(TelnyxCampaignCsp, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.update(
                campaign_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.list(
            brand_id="brandId",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.list(
            brand_id="brandId",
            page=0,
            records_per_page=0,
            sort="assignedPhoneNumbersCount",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.list(
            brand_id="brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.list(
            brand_id="brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.delete(
            "campaignId",
        )
        assert_matches_type(CampaignDeleteResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.delete(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignDeleteResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.delete(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignDeleteResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_appeal(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.appeal(
            campaign_id="5eb13888-32b7-4cab-95e6-d834dde21d64",
            appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
        )
        assert_matches_type(CampaignAppealResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_appeal(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.appeal(
            campaign_id="5eb13888-32b7-4cab-95e6-d834dde21d64",
            appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignAppealResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_appeal(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.appeal(
            campaign_id="5eb13888-32b7-4cab-95e6-d834dde21d64",
            appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignAppealResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_appeal(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.appeal(
                campaign_id="",
                appeal_reason="The website has been updated to include the required privacy policy and terms of service.",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_mno_metadata(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.retrieve_mno_metadata(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveMnoMetadataResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_mno_metadata(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.retrieve_mno_metadata(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignRetrieveMnoMetadataResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_mno_metadata(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.retrieve_mno_metadata(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignRetrieveMnoMetadataResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_mno_metadata(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.retrieve_mno_metadata(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_operation_status(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.retrieve_operation_status(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveOperationStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_operation_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.retrieve_operation_status(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignRetrieveOperationStatusResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_operation_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.retrieve_operation_status(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignRetrieveOperationStatusResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_operation_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.retrieve_operation_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        campaign = await async_client.number_10dlc.campaign.retrieve_sharing(
            "campaignId",
        )
        assert_matches_type(CampaignRetrieveSharingResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.campaign.with_raw_response.retrieve_sharing(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignRetrieveSharingResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.campaign.with_streaming_response.retrieve_sharing(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignRetrieveSharingResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_sharing(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.number_10dlc.campaign.with_raw_response.retrieve_sharing(
                "",
            )
