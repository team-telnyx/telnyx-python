# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.number_10dlc import partner_campaign_get_shared_by_me_params
from ...types.number_10dlc.partner_campaign_get_shared_by_me_response import PartnerCampaignGetSharedByMeResponse
from ...types.number_10dlc.partner_campaign_get_sharing_status_response import PartnerCampaignGetSharingStatusResponse

__all__ = ["PartnerCampaignResource", "AsyncPartnerCampaignResource"]


class PartnerCampaignResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PartnerCampaignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PartnerCampaignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartnerCampaignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PartnerCampaignResourceWithStreamingResponse(self)

    def get_shared_by_me(
        self,
        *,
        page: int | Omit = omit,
        records_per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartnerCampaignGetSharedByMeResponse:
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
            "/10dlc/partnerCampaign/sharedByMe",
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
                    partner_campaign_get_shared_by_me_params.PartnerCampaignGetSharedByMeParams,
                ),
            ),
            cast_to=PartnerCampaignGetSharedByMeResponse,
        )

    def get_sharing_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartnerCampaignGetSharingStatusResponse:
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
            f"/10dlc/partnerCampaign/{campaign_id}/sharing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartnerCampaignGetSharingStatusResponse,
        )


class AsyncPartnerCampaignResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPartnerCampaignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPartnerCampaignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartnerCampaignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPartnerCampaignResourceWithStreamingResponse(self)

    async def get_shared_by_me(
        self,
        *,
        page: int | Omit = omit,
        records_per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartnerCampaignGetSharedByMeResponse:
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
            "/10dlc/partnerCampaign/sharedByMe",
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
                    partner_campaign_get_shared_by_me_params.PartnerCampaignGetSharedByMeParams,
                ),
            ),
            cast_to=PartnerCampaignGetSharedByMeResponse,
        )

    async def get_sharing_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartnerCampaignGetSharingStatusResponse:
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
            f"/10dlc/partnerCampaign/{campaign_id}/sharing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartnerCampaignGetSharingStatusResponse,
        )


class PartnerCampaignResourceWithRawResponse:
    def __init__(self, partner_campaign: PartnerCampaignResource) -> None:
        self._partner_campaign = partner_campaign

        self.get_shared_by_me = to_raw_response_wrapper(
            partner_campaign.get_shared_by_me,
        )
        self.get_sharing_status = to_raw_response_wrapper(
            partner_campaign.get_sharing_status,
        )


class AsyncPartnerCampaignResourceWithRawResponse:
    def __init__(self, partner_campaign: AsyncPartnerCampaignResource) -> None:
        self._partner_campaign = partner_campaign

        self.get_shared_by_me = async_to_raw_response_wrapper(
            partner_campaign.get_shared_by_me,
        )
        self.get_sharing_status = async_to_raw_response_wrapper(
            partner_campaign.get_sharing_status,
        )


class PartnerCampaignResourceWithStreamingResponse:
    def __init__(self, partner_campaign: PartnerCampaignResource) -> None:
        self._partner_campaign = partner_campaign

        self.get_shared_by_me = to_streamed_response_wrapper(
            partner_campaign.get_shared_by_me,
        )
        self.get_sharing_status = to_streamed_response_wrapper(
            partner_campaign.get_sharing_status,
        )


class AsyncPartnerCampaignResourceWithStreamingResponse:
    def __init__(self, partner_campaign: AsyncPartnerCampaignResource) -> None:
        self._partner_campaign = partner_campaign

        self.get_shared_by_me = async_to_streamed_response_wrapper(
            partner_campaign.get_shared_by_me,
        )
        self.get_sharing_status = async_to_streamed_response_wrapper(
            partner_campaign.get_sharing_status,
        )
