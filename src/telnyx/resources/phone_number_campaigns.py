# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    phone_number_campaign_list_params,
    phone_number_campaign_create_params,
    phone_number_campaign_update_params,
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
from ..types.phone_number_campaign import PhoneNumberCampaign
from ..types.phone_number_campaign_list_response import PhoneNumberCampaignListResponse

__all__ = ["PhoneNumberCampaignsResource", "AsyncPhoneNumberCampaignsResource"]


class PhoneNumberCampaignsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumberCampaignsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        campaign_id: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        Create New Phone Number Campaign

        Args:
          campaign_id: The ID of the campaign you want to link to the specified phone number.

          phone_number: The phone number you want to link to a specified campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_number_campaigns",
            body=maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "phone_number": phone_number,
                },
                phone_number_campaign_create_params.PhoneNumberCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        Retrieve an individual phone number/campaign assignment by `phoneNumber`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/phone_number_campaigns/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )

    def update(
        self,
        path_phone_number: str,
        *,
        campaign_id: str,
        body_phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        Create New Phone Number Campaign

        Args:
          campaign_id: The ID of the campaign you want to link to the specified phone number.

          body_phone_number: The phone number you want to link to a specified campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_phone_number:
            raise ValueError(f"Expected a non-empty value for `path_phone_number` but received {path_phone_number!r}")
        return self._put(
            f"/phone_number_campaigns/{path_phone_number}",
            body=maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "body_phone_number": body_phone_number,
                },
                phone_number_campaign_update_params.PhoneNumberCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )

    def list(
        self,
        *,
        filter: phone_number_campaign_list_params.Filter | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["assignmentStatus", "-assignmentStatus", "createdAt", "-createdAt", "phoneNumber", "-phoneNumber"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaignListResponse:
        """
        Retrieve All Phone Number Campaigns

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[telnyx_campaign_id], filter[telnyx_brand_id], filter[tcr_campaign_id],
              filter[tcr_brand_id]

          sort: Specifies the sort order for results. If not given, results are sorted by
              createdAt in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_number_campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                    },
                    phone_number_campaign_list_params.PhoneNumberCampaignListParams,
                ),
            ),
            cast_to=PhoneNumberCampaignListResponse,
        )

    def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        This endpoint allows you to remove a campaign assignment from the supplied
        `phoneNumber`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._delete(
            f"/phone_number_campaigns/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )


class AsyncPhoneNumberCampaignsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumberCampaignsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        campaign_id: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        Create New Phone Number Campaign

        Args:
          campaign_id: The ID of the campaign you want to link to the specified phone number.

          phone_number: The phone number you want to link to a specified campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_number_campaigns",
            body=await async_maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "phone_number": phone_number,
                },
                phone_number_campaign_create_params.PhoneNumberCampaignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        Retrieve an individual phone number/campaign assignment by `phoneNumber`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/phone_number_campaigns/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )

    async def update(
        self,
        path_phone_number: str,
        *,
        campaign_id: str,
        body_phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        Create New Phone Number Campaign

        Args:
          campaign_id: The ID of the campaign you want to link to the specified phone number.

          body_phone_number: The phone number you want to link to a specified campaign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_phone_number:
            raise ValueError(f"Expected a non-empty value for `path_phone_number` but received {path_phone_number!r}")
        return await self._put(
            f"/phone_number_campaigns/{path_phone_number}",
            body=await async_maybe_transform(
                {
                    "campaign_id": campaign_id,
                    "body_phone_number": body_phone_number,
                },
                phone_number_campaign_update_params.PhoneNumberCampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )

    async def list(
        self,
        *,
        filter: phone_number_campaign_list_params.Filter | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["assignmentStatus", "-assignmentStatus", "createdAt", "-createdAt", "phoneNumber", "-phoneNumber"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaignListResponse:
        """
        Retrieve All Phone Number Campaigns

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[telnyx_campaign_id], filter[telnyx_brand_id], filter[tcr_campaign_id],
              filter[tcr_brand_id]

          sort: Specifies the sort order for results. If not given, results are sorted by
              createdAt in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_number_campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                    },
                    phone_number_campaign_list_params.PhoneNumberCampaignListParams,
                ),
            ),
            cast_to=PhoneNumberCampaignListResponse,
        )

    async def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberCampaign:
        """
        This endpoint allows you to remove a campaign assignment from the supplied
        `phoneNumber`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._delete(
            f"/phone_number_campaigns/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCampaign,
        )


class PhoneNumberCampaignsResourceWithRawResponse:
    def __init__(self, phone_number_campaigns: PhoneNumberCampaignsResource) -> None:
        self._phone_number_campaigns = phone_number_campaigns

        self.create = to_raw_response_wrapper(
            phone_number_campaigns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            phone_number_campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            phone_number_campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            phone_number_campaigns.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_number_campaigns.delete,
        )


class AsyncPhoneNumberCampaignsResourceWithRawResponse:
    def __init__(self, phone_number_campaigns: AsyncPhoneNumberCampaignsResource) -> None:
        self._phone_number_campaigns = phone_number_campaigns

        self.create = async_to_raw_response_wrapper(
            phone_number_campaigns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            phone_number_campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            phone_number_campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_number_campaigns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_number_campaigns.delete,
        )


class PhoneNumberCampaignsResourceWithStreamingResponse:
    def __init__(self, phone_number_campaigns: PhoneNumberCampaignsResource) -> None:
        self._phone_number_campaigns = phone_number_campaigns

        self.create = to_streamed_response_wrapper(
            phone_number_campaigns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            phone_number_campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            phone_number_campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_number_campaigns.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_number_campaigns.delete,
        )


class AsyncPhoneNumberCampaignsResourceWithStreamingResponse:
    def __init__(self, phone_number_campaigns: AsyncPhoneNumberCampaignsResource) -> None:
        self._phone_number_campaigns = phone_number_campaigns

        self.create = async_to_streamed_response_wrapper(
            phone_number_campaigns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            phone_number_campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_number_campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_number_campaigns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_number_campaigns.delete,
        )
