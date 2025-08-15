# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .osr import (
    OsrResource,
    AsyncOsrResource,
    OsrResourceWithRawResponse,
    AsyncOsrResourceWithRawResponse,
    OsrResourceWithStreamingResponse,
    AsyncOsrResourceWithStreamingResponse,
)
from ...types import campaign_list_params, campaign_update_params, campaign_submit_appeal_params
from .usecase import (
    UsecaseResource,
    AsyncUsecaseResource,
    UsecaseResourceWithRawResponse,
    AsyncUsecaseResourceWithRawResponse,
    UsecaseResourceWithStreamingResponse,
    AsyncUsecaseResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.telnyx_campaign_csp import TelnyxCampaignCsp
from ...types.campaign_list_response import CampaignListResponse
from ...types.campaign_deactivate_response import CampaignDeactivateResponse
from ...types.campaign_submit_appeal_response import CampaignSubmitAppealResponse
from ...types.campaign_get_mno_metadata_response import CampaignGetMnoMetadataResponse
from ...types.campaign_get_sharing_status_response import CampaignGetSharingStatusResponse

__all__ = ["CampaignResource", "AsyncCampaignResource"]


class CampaignResource(SyncAPIResource):
    @cached_property
    def usecase(self) -> UsecaseResource:
        return UsecaseResource(self._client)

    @cached_property
    def osr(self) -> OsrResource:
        return OsrResource(self._client)

    @cached_property
    def with_raw_response(self) -> CampaignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CampaignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CampaignResourceWithStreamingResponse(self)

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
    ) -> TelnyxCampaignCsp:
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
            f"/campaign/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxCampaignCsp,
        )

    def update(
        self,
        campaign_id: str,
        *,
        auto_renewal: bool | NotGiven = NOT_GIVEN,
        help_message: str | NotGiven = NOT_GIVEN,
        message_flow: str | NotGiven = NOT_GIVEN,
        reseller_id: str | NotGiven = NOT_GIVEN,
        sample1: str | NotGiven = NOT_GIVEN,
        sample2: str | NotGiven = NOT_GIVEN,
        sample3: str | NotGiven = NOT_GIVEN,
        sample4: str | NotGiven = NOT_GIVEN,
        sample5: str | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxCampaignCsp:
        """Update a campaign's properties by `campaignId`.

        **Please note:** only sample
        messages are editable.

        Args:
          auto_renewal: Help message of the campaign.

          help_message: Help message of the campaign.

          message_flow: Message flow description.

          reseller_id: Alphanumeric identifier of the reseller that you want to associate with this
              campaign.

          sample1: Message sample. Some campaign tiers require 1 or more message samples.

          sample2: Message sample. Some campaign tiers require 2 or more message samples.

          sample3: Message sample. Some campaign tiers require 3 or more message samples.

          sample4: Message sample. Some campaign tiers require 4 or more message samples.

          sample5: Message sample. Some campaign tiers require 5 or more message samples.

          webhook_failover_url: Webhook failover to which campaign status updates are sent.

          webhook_url: Webhook to which campaign status updates are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._put(
            f"/campaign/{campaign_id}",
            body=maybe_transform(
                {
                    "auto_renewal": auto_renewal,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "reseller_id": reseller_id,
                    "sample1": sample1,
                    "sample2": sample2,
                    "sample3": sample3,
                    "sample4": sample4,
                    "sample5": sample5,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxCampaignCsp,
        )

    def list(
        self,
        *,
        brand_id: str,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "assignedPhoneNumbersCount",
            "-assignedPhoneNumbersCount",
            "campaignId",
            "-campaignId",
            "createdAt",
            "-createdAt",
            "status",
            "-status",
            "tcrCampaignId",
            "-tcrCampaignId",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignListResponse:
        """
        Retrieve a list of campaigns associated with a supplied `brandId`.

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
            "/campaign",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand_id": brand_id,
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                    },
                    campaign_list_params.CampaignListParams,
                ),
            ),
            cast_to=CampaignListResponse,
        )

    def accept_sharing(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Manually accept a campaign shared with Telnyx

        Args:
          campaign_id: TCR's ID for the campaign to import

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._post(
            f"/campaign/acceptSharing/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def deactivate(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignDeactivateResponse:
        """Terminate a campaign.

        Note that once deactivated, a campaign cannot be restored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._delete(
            f"/campaign/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDeactivateResponse,
        )

    def get_mno_metadata(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignGetMnoMetadataResponse:
        """
        Get the campaign metadata for each MNO it was submitted to.

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
            f"/campaign/{campaign_id}/mnoMetadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignGetMnoMetadataResponse,
        )

    def get_operation_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Retrieve campaign's operation status at MNO level.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._get(
            f"/campaign/{campaign_id}/operationStatus",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignGetSharingStatusResponse:
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
            f"/campaign/{campaign_id}/sharing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignGetSharingStatusResponse,
        )

    def submit_appeal(
        self,
        campaign_id: str,
        *,
        appeal_reason: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignSubmitAppealResponse:
        """
        Submits an appeal for rejected native campaigns in TELNYX_FAILED or MNO_REJECTED
        status. The appeal is recorded for manual compliance team review and the
        campaign status is reset to TCR_ACCEPTED. Note: Appeal forwarding is handled
        manually to allow proper review before incurring upstream charges.

        Args:
          appeal_reason: Detailed explanation of why the campaign should be reconsidered and what changes
              have been made to address the rejection reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return self._post(
            f"/campaign/{campaign_id}/appeal",
            body=maybe_transform(
                {"appeal_reason": appeal_reason}, campaign_submit_appeal_params.CampaignSubmitAppealParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignSubmitAppealResponse,
        )


class AsyncCampaignResource(AsyncAPIResource):
    @cached_property
    def usecase(self) -> AsyncUsecaseResource:
        return AsyncUsecaseResource(self._client)

    @cached_property
    def osr(self) -> AsyncOsrResource:
        return AsyncOsrResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCampaignResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCampaignResourceWithStreamingResponse(self)

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
    ) -> TelnyxCampaignCsp:
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
            f"/campaign/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxCampaignCsp,
        )

    async def update(
        self,
        campaign_id: str,
        *,
        auto_renewal: bool | NotGiven = NOT_GIVEN,
        help_message: str | NotGiven = NOT_GIVEN,
        message_flow: str | NotGiven = NOT_GIVEN,
        reseller_id: str | NotGiven = NOT_GIVEN,
        sample1: str | NotGiven = NOT_GIVEN,
        sample2: str | NotGiven = NOT_GIVEN,
        sample3: str | NotGiven = NOT_GIVEN,
        sample4: str | NotGiven = NOT_GIVEN,
        sample5: str | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxCampaignCsp:
        """Update a campaign's properties by `campaignId`.

        **Please note:** only sample
        messages are editable.

        Args:
          auto_renewal: Help message of the campaign.

          help_message: Help message of the campaign.

          message_flow: Message flow description.

          reseller_id: Alphanumeric identifier of the reseller that you want to associate with this
              campaign.

          sample1: Message sample. Some campaign tiers require 1 or more message samples.

          sample2: Message sample. Some campaign tiers require 2 or more message samples.

          sample3: Message sample. Some campaign tiers require 3 or more message samples.

          sample4: Message sample. Some campaign tiers require 4 or more message samples.

          sample5: Message sample. Some campaign tiers require 5 or more message samples.

          webhook_failover_url: Webhook failover to which campaign status updates are sent.

          webhook_url: Webhook to which campaign status updates are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._put(
            f"/campaign/{campaign_id}",
            body=await async_maybe_transform(
                {
                    "auto_renewal": auto_renewal,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "reseller_id": reseller_id,
                    "sample1": sample1,
                    "sample2": sample2,
                    "sample3": sample3,
                    "sample4": sample4,
                    "sample5": sample5,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxCampaignCsp,
        )

    async def list(
        self,
        *,
        brand_id: str,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "assignedPhoneNumbersCount",
            "-assignedPhoneNumbersCount",
            "campaignId",
            "-campaignId",
            "createdAt",
            "-createdAt",
            "status",
            "-status",
            "tcrCampaignId",
            "-tcrCampaignId",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignListResponse:
        """
        Retrieve a list of campaigns associated with a supplied `brandId`.

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
            "/campaign",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "brand_id": brand_id,
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                    },
                    campaign_list_params.CampaignListParams,
                ),
            ),
            cast_to=CampaignListResponse,
        )

    async def accept_sharing(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Manually accept a campaign shared with Telnyx

        Args:
          campaign_id: TCR's ID for the campaign to import

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._post(
            f"/campaign/acceptSharing/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def deactivate(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignDeactivateResponse:
        """Terminate a campaign.

        Note that once deactivated, a campaign cannot be restored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._delete(
            f"/campaign/{campaign_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDeactivateResponse,
        )

    async def get_mno_metadata(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignGetMnoMetadataResponse:
        """
        Get the campaign metadata for each MNO it was submitted to.

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
            f"/campaign/{campaign_id}/mnoMetadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignGetMnoMetadataResponse,
        )

    async def get_operation_status(
        self,
        campaign_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Retrieve campaign's operation status at MNO level.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._get(
            f"/campaign/{campaign_id}/operationStatus",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignGetSharingStatusResponse:
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
            f"/campaign/{campaign_id}/sharing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignGetSharingStatusResponse,
        )

    async def submit_appeal(
        self,
        campaign_id: str,
        *,
        appeal_reason: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignSubmitAppealResponse:
        """
        Submits an appeal for rejected native campaigns in TELNYX_FAILED or MNO_REJECTED
        status. The appeal is recorded for manual compliance team review and the
        campaign status is reset to TCR_ACCEPTED. Note: Appeal forwarding is handled
        manually to allow proper review before incurring upstream charges.

        Args:
          appeal_reason: Detailed explanation of why the campaign should be reconsidered and what changes
              have been made to address the rejection reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
        return await self._post(
            f"/campaign/{campaign_id}/appeal",
            body=await async_maybe_transform(
                {"appeal_reason": appeal_reason}, campaign_submit_appeal_params.CampaignSubmitAppealParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignSubmitAppealResponse,
        )


class CampaignResourceWithRawResponse:
    def __init__(self, campaign: CampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = to_raw_response_wrapper(
            campaign.retrieve,
        )
        self.update = to_raw_response_wrapper(
            campaign.update,
        )
        self.list = to_raw_response_wrapper(
            campaign.list,
        )
        self.accept_sharing = to_raw_response_wrapper(
            campaign.accept_sharing,
        )
        self.deactivate = to_raw_response_wrapper(
            campaign.deactivate,
        )
        self.get_mno_metadata = to_raw_response_wrapper(
            campaign.get_mno_metadata,
        )
        self.get_operation_status = to_raw_response_wrapper(
            campaign.get_operation_status,
        )
        self.get_sharing_status = to_raw_response_wrapper(
            campaign.get_sharing_status,
        )
        self.submit_appeal = to_raw_response_wrapper(
            campaign.submit_appeal,
        )

    @cached_property
    def usecase(self) -> UsecaseResourceWithRawResponse:
        return UsecaseResourceWithRawResponse(self._campaign.usecase)

    @cached_property
    def osr(self) -> OsrResourceWithRawResponse:
        return OsrResourceWithRawResponse(self._campaign.osr)


class AsyncCampaignResourceWithRawResponse:
    def __init__(self, campaign: AsyncCampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = async_to_raw_response_wrapper(
            campaign.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            campaign.update,
        )
        self.list = async_to_raw_response_wrapper(
            campaign.list,
        )
        self.accept_sharing = async_to_raw_response_wrapper(
            campaign.accept_sharing,
        )
        self.deactivate = async_to_raw_response_wrapper(
            campaign.deactivate,
        )
        self.get_mno_metadata = async_to_raw_response_wrapper(
            campaign.get_mno_metadata,
        )
        self.get_operation_status = async_to_raw_response_wrapper(
            campaign.get_operation_status,
        )
        self.get_sharing_status = async_to_raw_response_wrapper(
            campaign.get_sharing_status,
        )
        self.submit_appeal = async_to_raw_response_wrapper(
            campaign.submit_appeal,
        )

    @cached_property
    def usecase(self) -> AsyncUsecaseResourceWithRawResponse:
        return AsyncUsecaseResourceWithRawResponse(self._campaign.usecase)

    @cached_property
    def osr(self) -> AsyncOsrResourceWithRawResponse:
        return AsyncOsrResourceWithRawResponse(self._campaign.osr)


class CampaignResourceWithStreamingResponse:
    def __init__(self, campaign: CampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = to_streamed_response_wrapper(
            campaign.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            campaign.update,
        )
        self.list = to_streamed_response_wrapper(
            campaign.list,
        )
        self.accept_sharing = to_streamed_response_wrapper(
            campaign.accept_sharing,
        )
        self.deactivate = to_streamed_response_wrapper(
            campaign.deactivate,
        )
        self.get_mno_metadata = to_streamed_response_wrapper(
            campaign.get_mno_metadata,
        )
        self.get_operation_status = to_streamed_response_wrapper(
            campaign.get_operation_status,
        )
        self.get_sharing_status = to_streamed_response_wrapper(
            campaign.get_sharing_status,
        )
        self.submit_appeal = to_streamed_response_wrapper(
            campaign.submit_appeal,
        )

    @cached_property
    def usecase(self) -> UsecaseResourceWithStreamingResponse:
        return UsecaseResourceWithStreamingResponse(self._campaign.usecase)

    @cached_property
    def osr(self) -> OsrResourceWithStreamingResponse:
        return OsrResourceWithStreamingResponse(self._campaign.osr)


class AsyncCampaignResourceWithStreamingResponse:
    def __init__(self, campaign: AsyncCampaignResource) -> None:
        self._campaign = campaign

        self.retrieve = async_to_streamed_response_wrapper(
            campaign.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            campaign.update,
        )
        self.list = async_to_streamed_response_wrapper(
            campaign.list,
        )
        self.accept_sharing = async_to_streamed_response_wrapper(
            campaign.accept_sharing,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            campaign.deactivate,
        )
        self.get_mno_metadata = async_to_streamed_response_wrapper(
            campaign.get_mno_metadata,
        )
        self.get_operation_status = async_to_streamed_response_wrapper(
            campaign.get_operation_status,
        )
        self.get_sharing_status = async_to_streamed_response_wrapper(
            campaign.get_sharing_status,
        )
        self.submit_appeal = async_to_streamed_response_wrapper(
            campaign.submit_appeal,
        )

    @cached_property
    def usecase(self) -> AsyncUsecaseResourceWithStreamingResponse:
        return AsyncUsecaseResourceWithStreamingResponse(self._campaign.usecase)

    @cached_property
    def osr(self) -> AsyncOsrResourceWithStreamingResponse:
        return AsyncOsrResourceWithStreamingResponse(self._campaign.osr)
