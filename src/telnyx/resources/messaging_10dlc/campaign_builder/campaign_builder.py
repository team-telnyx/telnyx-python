# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .brand import (
    BrandResource,
    AsyncBrandResource,
    BrandResourceWithRawResponse,
    AsyncBrandResourceWithRawResponse,
    BrandResourceWithStreamingResponse,
    AsyncBrandResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.messaging_10dlc import campaign_builder_submit_params
from ....types.messaging_10dlc.telnyx_campaign_csp import TelnyxCampaignCsp

__all__ = ["CampaignBuilderResource", "AsyncCampaignBuilderResource"]


class CampaignBuilderResource(SyncAPIResource):
    @cached_property
    def brand(self) -> BrandResource:
        return BrandResource(self._client)

    @cached_property
    def with_raw_response(self) -> CampaignBuilderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CampaignBuilderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignBuilderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CampaignBuilderResourceWithStreamingResponse(self)

    def submit(
        self,
        *,
        brand_id: str,
        description: str,
        usecase: str,
        age_gated: bool | Omit = omit,
        auto_renewal: bool | Omit = omit,
        direct_lending: bool | Omit = omit,
        embedded_link: bool | Omit = omit,
        embedded_link_sample: str | Omit = omit,
        embedded_phone: bool | Omit = omit,
        help_keywords: str | Omit = omit,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        mno_ids: Iterable[int] | Omit = omit,
        number_pool: bool | Omit = omit,
        optin_keywords: str | Omit = omit,
        optin_message: str | Omit = omit,
        optout_keywords: str | Omit = omit,
        optout_message: str | Omit = omit,
        privacy_policy_link: str | Omit = omit,
        reference_id: str | Omit = omit,
        reseller_id: str | Omit = omit,
        sample1: str | Omit = omit,
        sample2: str | Omit = omit,
        sample3: str | Omit = omit,
        sample4: str | Omit = omit,
        sample5: str | Omit = omit,
        subscriber_help: bool | Omit = omit,
        subscriber_optin: bool | Omit = omit,
        subscriber_optout: bool | Omit = omit,
        sub_usecases: SequenceNotStr[str] | Omit = omit,
        tag: SequenceNotStr[str] | Omit = omit,
        terms_and_conditions: bool | Omit = omit,
        terms_and_conditions_link: str | Omit = omit,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelnyxCampaignCsp:
        """
        Before creating a campaign, use the
        [Qualify By Usecase endpoint](https://developers.telnyx.com/api-reference/campaign/qualify-by-usecase)
        to ensure that the brand you want to assign a new campaign to is qualified for
        the desired use case of that campaign. **Please note:** After campaign creation,
        you'll only be able to edit the campaign's sample messages. Creating a campaign
        will entail an upfront, non-refundable three month's cost that will depend on
        the campaign's use case
        ([see 10DLC Costs section for details](https://developers.telnyx.com/api-reference/campaign/get-campaign-cost)).

        Args:
          brand_id: Alphanumeric identifier of the brand associated with this campaign.

          description: Summary description of this campaign.

          usecase: Campaign usecase. Must be of defined valid types. Use `/10dlc/enum/usecase`
              operation to retrieve usecases available for given brand.

          age_gated: Age gated message content in campaign.

          auto_renewal: Campaign subscription auto-renewal option. If set to true, then campaign will
              automatically renewal at end of billing cycle.

          direct_lending: Direct lending or loan arrangement

          embedded_link: Does message generated by the campaign include URL link in SMS?

          embedded_link_sample: Sample of an embedded link that will be sent to subscribers.

          embedded_phone: Does message generated by the campaign include phone number in SMS?

          help_keywords: Subscriber help keywords. Multiple keywords are comma separated without space.

          help_message: Help message of the campaign.

          message_flow: Message flow description.

          mno_ids: Submit campaign to given list of MNOs by MNO's network ID. Default is all MNOs
              if no value provided.

          number_pool: Does campaign utilize pool of phone numbers?

          optin_keywords: Subscriber opt-in keywords. Multiple keywords are comma separated without space.

          optin_message: Subscriber opt-in message.

          optout_keywords: Subscriber opt-out keywords. Multiple keywords are comma separated without
              space.

          optout_message: Subscriber opt-out message.

          privacy_policy_link: Link to the campaign's privacy policy.

          reference_id: Caller supplied campaign reference ID. If supplied, the value must be unique
              across all submitted campaigns. Can be used to prevent duplicate campaign
              registrations.

          reseller_id: Alphanumeric identifier of the reseller that you want to associate with this
              campaign.

          sample1: Message sample. Some campaign tiers require 1 or more message samples.

          sample2: Message sample. Some campaign tiers require 2 or more message samples.

          sample3: Message sample. Some campaign tiers require 3 or more message samples.

          sample4: Message sample. Some campaign tiers require 4 or more message samples.

          sample5: Message sample. Some campaign tiers require 5 or more message samples.

          subscriber_help: Does campaign responds to help keyword(s)?

          subscriber_optin: Does campaign require subscriber to opt-in before SMS is sent to subscriber?

          subscriber_optout: Does campaign support subscriber opt-out keyword(s)?

          sub_usecases: Campaign sub-usecases. Must be of defined valid sub-usecase types. Use
              `/10dlc/enum/usecase` operation to retrieve list of valid sub-usecases

          tag: Tags to be set on the Campaign.

          terms_and_conditions: Is terms and conditions accepted?

          terms_and_conditions_link: Link to the campaign's terms and conditions.

          webhook_failover_url: Failover webhook to which campaign status updates are sent.

          webhook_url: Webhook to which campaign status updates are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/10dlc/campaignBuilder",
            body=maybe_transform(
                {
                    "brand_id": brand_id,
                    "description": description,
                    "usecase": usecase,
                    "age_gated": age_gated,
                    "auto_renewal": auto_renewal,
                    "direct_lending": direct_lending,
                    "embedded_link": embedded_link,
                    "embedded_link_sample": embedded_link_sample,
                    "embedded_phone": embedded_phone,
                    "help_keywords": help_keywords,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "mno_ids": mno_ids,
                    "number_pool": number_pool,
                    "optin_keywords": optin_keywords,
                    "optin_message": optin_message,
                    "optout_keywords": optout_keywords,
                    "optout_message": optout_message,
                    "privacy_policy_link": privacy_policy_link,
                    "reference_id": reference_id,
                    "reseller_id": reseller_id,
                    "sample1": sample1,
                    "sample2": sample2,
                    "sample3": sample3,
                    "sample4": sample4,
                    "sample5": sample5,
                    "subscriber_help": subscriber_help,
                    "subscriber_optin": subscriber_optin,
                    "subscriber_optout": subscriber_optout,
                    "sub_usecases": sub_usecases,
                    "tag": tag,
                    "terms_and_conditions": terms_and_conditions,
                    "terms_and_conditions_link": terms_and_conditions_link,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                campaign_builder_submit_params.CampaignBuilderSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxCampaignCsp,
        )


class AsyncCampaignBuilderResource(AsyncAPIResource):
    @cached_property
    def brand(self) -> AsyncBrandResource:
        return AsyncBrandResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCampaignBuilderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignBuilderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignBuilderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCampaignBuilderResourceWithStreamingResponse(self)

    async def submit(
        self,
        *,
        brand_id: str,
        description: str,
        usecase: str,
        age_gated: bool | Omit = omit,
        auto_renewal: bool | Omit = omit,
        direct_lending: bool | Omit = omit,
        embedded_link: bool | Omit = omit,
        embedded_link_sample: str | Omit = omit,
        embedded_phone: bool | Omit = omit,
        help_keywords: str | Omit = omit,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        mno_ids: Iterable[int] | Omit = omit,
        number_pool: bool | Omit = omit,
        optin_keywords: str | Omit = omit,
        optin_message: str | Omit = omit,
        optout_keywords: str | Omit = omit,
        optout_message: str | Omit = omit,
        privacy_policy_link: str | Omit = omit,
        reference_id: str | Omit = omit,
        reseller_id: str | Omit = omit,
        sample1: str | Omit = omit,
        sample2: str | Omit = omit,
        sample3: str | Omit = omit,
        sample4: str | Omit = omit,
        sample5: str | Omit = omit,
        subscriber_help: bool | Omit = omit,
        subscriber_optin: bool | Omit = omit,
        subscriber_optout: bool | Omit = omit,
        sub_usecases: SequenceNotStr[str] | Omit = omit,
        tag: SequenceNotStr[str] | Omit = omit,
        terms_and_conditions: bool | Omit = omit,
        terms_and_conditions_link: str | Omit = omit,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelnyxCampaignCsp:
        """
        Before creating a campaign, use the
        [Qualify By Usecase endpoint](https://developers.telnyx.com/api-reference/campaign/qualify-by-usecase)
        to ensure that the brand you want to assign a new campaign to is qualified for
        the desired use case of that campaign. **Please note:** After campaign creation,
        you'll only be able to edit the campaign's sample messages. Creating a campaign
        will entail an upfront, non-refundable three month's cost that will depend on
        the campaign's use case
        ([see 10DLC Costs section for details](https://developers.telnyx.com/api-reference/campaign/get-campaign-cost)).

        Args:
          brand_id: Alphanumeric identifier of the brand associated with this campaign.

          description: Summary description of this campaign.

          usecase: Campaign usecase. Must be of defined valid types. Use `/10dlc/enum/usecase`
              operation to retrieve usecases available for given brand.

          age_gated: Age gated message content in campaign.

          auto_renewal: Campaign subscription auto-renewal option. If set to true, then campaign will
              automatically renewal at end of billing cycle.

          direct_lending: Direct lending or loan arrangement

          embedded_link: Does message generated by the campaign include URL link in SMS?

          embedded_link_sample: Sample of an embedded link that will be sent to subscribers.

          embedded_phone: Does message generated by the campaign include phone number in SMS?

          help_keywords: Subscriber help keywords. Multiple keywords are comma separated without space.

          help_message: Help message of the campaign.

          message_flow: Message flow description.

          mno_ids: Submit campaign to given list of MNOs by MNO's network ID. Default is all MNOs
              if no value provided.

          number_pool: Does campaign utilize pool of phone numbers?

          optin_keywords: Subscriber opt-in keywords. Multiple keywords are comma separated without space.

          optin_message: Subscriber opt-in message.

          optout_keywords: Subscriber opt-out keywords. Multiple keywords are comma separated without
              space.

          optout_message: Subscriber opt-out message.

          privacy_policy_link: Link to the campaign's privacy policy.

          reference_id: Caller supplied campaign reference ID. If supplied, the value must be unique
              across all submitted campaigns. Can be used to prevent duplicate campaign
              registrations.

          reseller_id: Alphanumeric identifier of the reseller that you want to associate with this
              campaign.

          sample1: Message sample. Some campaign tiers require 1 or more message samples.

          sample2: Message sample. Some campaign tiers require 2 or more message samples.

          sample3: Message sample. Some campaign tiers require 3 or more message samples.

          sample4: Message sample. Some campaign tiers require 4 or more message samples.

          sample5: Message sample. Some campaign tiers require 5 or more message samples.

          subscriber_help: Does campaign responds to help keyword(s)?

          subscriber_optin: Does campaign require subscriber to opt-in before SMS is sent to subscriber?

          subscriber_optout: Does campaign support subscriber opt-out keyword(s)?

          sub_usecases: Campaign sub-usecases. Must be of defined valid sub-usecase types. Use
              `/10dlc/enum/usecase` operation to retrieve list of valid sub-usecases

          tag: Tags to be set on the Campaign.

          terms_and_conditions: Is terms and conditions accepted?

          terms_and_conditions_link: Link to the campaign's terms and conditions.

          webhook_failover_url: Failover webhook to which campaign status updates are sent.

          webhook_url: Webhook to which campaign status updates are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/10dlc/campaignBuilder",
            body=await async_maybe_transform(
                {
                    "brand_id": brand_id,
                    "description": description,
                    "usecase": usecase,
                    "age_gated": age_gated,
                    "auto_renewal": auto_renewal,
                    "direct_lending": direct_lending,
                    "embedded_link": embedded_link,
                    "embedded_link_sample": embedded_link_sample,
                    "embedded_phone": embedded_phone,
                    "help_keywords": help_keywords,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "mno_ids": mno_ids,
                    "number_pool": number_pool,
                    "optin_keywords": optin_keywords,
                    "optin_message": optin_message,
                    "optout_keywords": optout_keywords,
                    "optout_message": optout_message,
                    "privacy_policy_link": privacy_policy_link,
                    "reference_id": reference_id,
                    "reseller_id": reseller_id,
                    "sample1": sample1,
                    "sample2": sample2,
                    "sample3": sample3,
                    "sample4": sample4,
                    "sample5": sample5,
                    "subscriber_help": subscriber_help,
                    "subscriber_optin": subscriber_optin,
                    "subscriber_optout": subscriber_optout,
                    "sub_usecases": sub_usecases,
                    "tag": tag,
                    "terms_and_conditions": terms_and_conditions,
                    "terms_and_conditions_link": terms_and_conditions_link,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                campaign_builder_submit_params.CampaignBuilderSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxCampaignCsp,
        )


class CampaignBuilderResourceWithRawResponse:
    def __init__(self, campaign_builder: CampaignBuilderResource) -> None:
        self._campaign_builder = campaign_builder

        self.submit = to_raw_response_wrapper(
            campaign_builder.submit,
        )

    @cached_property
    def brand(self) -> BrandResourceWithRawResponse:
        return BrandResourceWithRawResponse(self._campaign_builder.brand)


class AsyncCampaignBuilderResourceWithRawResponse:
    def __init__(self, campaign_builder: AsyncCampaignBuilderResource) -> None:
        self._campaign_builder = campaign_builder

        self.submit = async_to_raw_response_wrapper(
            campaign_builder.submit,
        )

    @cached_property
    def brand(self) -> AsyncBrandResourceWithRawResponse:
        return AsyncBrandResourceWithRawResponse(self._campaign_builder.brand)


class CampaignBuilderResourceWithStreamingResponse:
    def __init__(self, campaign_builder: CampaignBuilderResource) -> None:
        self._campaign_builder = campaign_builder

        self.submit = to_streamed_response_wrapper(
            campaign_builder.submit,
        )

    @cached_property
    def brand(self) -> BrandResourceWithStreamingResponse:
        return BrandResourceWithStreamingResponse(self._campaign_builder.brand)


class AsyncCampaignBuilderResourceWithStreamingResponse:
    def __init__(self, campaign_builder: AsyncCampaignBuilderResource) -> None:
        self._campaign_builder = campaign_builder

        self.submit = async_to_streamed_response_wrapper(
            campaign_builder.submit,
        )

    @cached_property
    def brand(self) -> AsyncBrandResourceWithStreamingResponse:
        return AsyncBrandResourceWithStreamingResponse(self._campaign_builder.brand)
