# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    partner_campaign_list_params,
    partner_campaign_update_params,
    partner_campaign_list_shared_by_me_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.telnyx_downstream_campaign import TelnyxDownstreamCampaign
from ..types.partner_campaign_list_response import PartnerCampaignListResponse
from ..types.partner_campaign_list_shared_by_me_response import PartnerCampaignListSharedByMeResponse
from ..types.partner_campaign_retrieve_sharing_status_response import PartnerCampaignRetrieveSharingStatusResponse

__all__ = ["PartnerCampaignsResource", "AsyncPartnerCampaignsResource"]


class PartnerCampaignsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PartnerCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PartnerCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartnerCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PartnerCampaignsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxDownstreamCampaign:
        """
        Retrieve campaign details by `campaignId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            f"/partner_campaigns/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxDownstreamCampaign,
        )

    def update(
        self,
        campaign_id: str,
        *,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxDownstreamCampaign:
        """Update campaign details by `campaignId`.

        **Please note:** Only webhook urls are
        editable.

        Args:
          webhook_failover_url: Webhook failover to which campaign status updates are sent.

          webhook_url: Webhook to which campaign status updates are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._patch(
            f"/partner_campaigns/{campaign_id}",
            body=maybe_transform(
                {
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                partner_campaign_update_params.PartnerCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxDownstreamCampaign,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "assignedPhoneNumbersCount",
            "-assignedPhoneNumbersCount",
            "brandDisplayName",
            "-brandDisplayName",
            "tcrBrandId",
            "-tcrBranId",
            "tcrCampaignId",
            "-tcrCampaignId",
            "createdAt",
            "-createdAt",
            "campaignStatus",
            "-campaignStatus",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PartnerCampaignListResponse:
        """
        Retrieve all partner campaigns you have shared to Telnyx in a paginated fashion.

        This endpoint is currently limited to only returning shared campaigns that
        Telnyx has accepted. In other words, shared but pending campaigns are currently
        omitted from the response from this endpoint.

        Args:
          page: The 1-indexed page number to get. The default value is `1`.

          records_per_page: The amount of records per page, limited to between 1 and 500 inclusive. The
              default value is `10`.

          sort: Specifies the sort order for results. If not given, results are sorted by
              createdAt in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/partner_campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                    },
                    partner_campaign_list_params.PartnerCampaignListParams,
                ),
            ),
            cast_to=PartnerCampaignListResponse,
        )

    def list_shared_by_me(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PartnerCampaignListSharedByMeResponse:
        """
        Get all partner campaigns you have shared to Telnyx in a paginated fashion

        This endpoint is currently limited to only returning shared campaigns that
        Telnyx has accepted. In other words, shared but pending campaigns are currently
        omitted from the response from this endpoint.

        Args:
          page: The 1-indexed page number to get. The default value is `1`.

          records_per_page: The amount of records per page, limited to between 1 and 500 inclusive. The
              default value is `10`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/partnerCampaign/sharedByMe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "records_per_page": records_per_page,
                    },
                    partner_campaign_list_shared_by_me_params.PartnerCampaignListSharedByMeParams,
                ),
            ),
            cast_to=PartnerCampaignListSharedByMeResponse,
        )

    def retrieve_sharing_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PartnerCampaignRetrieveSharingStatusResponse:
        """
        Get Sharing Status

        Args:
          campaign_id: ID of the campaign in question

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            f"/partnerCampaign/{campaign_id}/sharing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartnerCampaignRetrieveSharingStatusResponse,
        )


class AsyncPartnerCampaignsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPartnerCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPartnerCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartnerCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPartnerCampaignsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxDownstreamCampaign:
        """
        Retrieve campaign details by `campaignId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            f"/partner_campaigns/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxDownstreamCampaign,
        )

    async def update(
        self,
        campaign_id: str,
        *,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxDownstreamCampaign:
        """Update campaign details by `campaignId`.

        **Please note:** Only webhook urls are
        editable.

        Args:
          webhook_failover_url: Webhook failover to which campaign status updates are sent.

          webhook_url: Webhook to which campaign status updates are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._patch(
            f"/partner_campaigns/{campaign_id}",
            body=await async_maybe_transform(
                {
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                partner_campaign_update_params.PartnerCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxDownstreamCampaign,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "assignedPhoneNumbersCount",
            "-assignedPhoneNumbersCount",
            "brandDisplayName",
            "-brandDisplayName",
            "tcrBrandId",
            "-tcrBranId",
            "tcrCampaignId",
            "-tcrCampaignId",
            "createdAt",
            "-createdAt",
            "campaignStatus",
            "-campaignStatus",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PartnerCampaignListResponse:
        """
        Retrieve all partner campaigns you have shared to Telnyx in a paginated fashion.

        This endpoint is currently limited to only returning shared campaigns that
        Telnyx has accepted. In other words, shared but pending campaigns are currently
        omitted from the response from this endpoint.

        Args:
          page: The 1-indexed page number to get. The default value is `1`.

          records_per_page: The amount of records per page, limited to between 1 and 500 inclusive. The
              default value is `10`.

          sort: Specifies the sort order for results. If not given, results are sorted by
              createdAt in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/partner_campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                    },
                    partner_campaign_list_params.PartnerCampaignListParams,
                ),
            ),
            cast_to=PartnerCampaignListResponse,
        )

    async def list_shared_by_me(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PartnerCampaignListSharedByMeResponse:
        """
        Get all partner campaigns you have shared to Telnyx in a paginated fashion

        This endpoint is currently limited to only returning shared campaigns that
        Telnyx has accepted. In other words, shared but pending campaigns are currently
        omitted from the response from this endpoint.

        Args:
          page: The 1-indexed page number to get. The default value is `1`.

          records_per_page: The amount of records per page, limited to between 1 and 500 inclusive. The
              default value is `10`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/partnerCampaign/sharedByMe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "records_per_page": records_per_page,
                    },
                    partner_campaign_list_shared_by_me_params.PartnerCampaignListSharedByMeParams,
                ),
            ),
            cast_to=PartnerCampaignListSharedByMeResponse,
        )

    async def retrieve_sharing_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PartnerCampaignRetrieveSharingStatusResponse:
        """
        Get Sharing Status

        Args:
          campaign_id: ID of the campaign in question

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            f"/partnerCampaign/{campaign_id}/sharing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartnerCampaignRetrieveSharingStatusResponse,
        )


class PartnerCampaignsResourceWithRawResponse:
    def __init__(self, partner_campaigns: PartnerCampaignsResource) -> None:
        self._partner_campaigns = partner_campaigns

        self.retrieve = to_raw_response_wrapper(
            partner_campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            partner_campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            partner_campaigns.list,
        )
        self.list_shared_by_me = to_raw_response_wrapper(
            partner_campaigns.list_shared_by_me,
        )
        self.retrieve_sharing_status = to_raw_response_wrapper(
            partner_campaigns.retrieve_sharing_status,
        )


class AsyncPartnerCampaignsResourceWithRawResponse:
    def __init__(self, partner_campaigns: AsyncPartnerCampaignsResource) -> None:
        self._partner_campaigns = partner_campaigns

        self.retrieve = async_to_raw_response_wrapper(
            partner_campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            partner_campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            partner_campaigns.list,
        )
        self.list_shared_by_me = async_to_raw_response_wrapper(
            partner_campaigns.list_shared_by_me,
        )
        self.retrieve_sharing_status = async_to_raw_response_wrapper(
            partner_campaigns.retrieve_sharing_status,
        )


class PartnerCampaignsResourceWithStreamingResponse:
    def __init__(self, partner_campaigns: PartnerCampaignsResource) -> None:
        self._partner_campaigns = partner_campaigns

        self.retrieve = to_streamed_response_wrapper(
            partner_campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            partner_campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            partner_campaigns.list,
        )
        self.list_shared_by_me = to_streamed_response_wrapper(
            partner_campaigns.list_shared_by_me,
        )
        self.retrieve_sharing_status = to_streamed_response_wrapper(
            partner_campaigns.retrieve_sharing_status,
        )


class AsyncPartnerCampaignsResourceWithStreamingResponse:
    def __init__(self, partner_campaigns: AsyncPartnerCampaignsResource) -> None:
        self._partner_campaigns = partner_campaigns

        self.retrieve = async_to_streamed_response_wrapper(
            partner_campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            partner_campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            partner_campaigns.list,
        )
        self.list_shared_by_me = async_to_streamed_response_wrapper(
            partner_campaigns.list_shared_by_me,
        )
        self.retrieve_sharing_status = async_to_streamed_response_wrapper(
            partner_campaigns.retrieve_sharing_status,
        )
