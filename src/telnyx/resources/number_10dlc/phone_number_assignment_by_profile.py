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
from ...types.number_10dlc import (
    phone_number_assignment_by_profile_assign_params,
    phone_number_assignment_by_profile_get_phone_number_status_params,
)
from ...types.number_10dlc.phone_number_assignment_by_profile_assign_response import (
    PhoneNumberAssignmentByProfileAssignResponse,
)
from ...types.number_10dlc.phone_number_assignment_by_profile_get_task_status_response import (
    PhoneNumberAssignmentByProfileGetTaskStatusResponse,
)
from ...types.number_10dlc.phone_number_assignment_by_profile_get_phone_number_status_response import (
    PhoneNumberAssignmentByProfileGetPhoneNumberStatusResponse,
)

__all__ = ["PhoneNumberAssignmentByProfileResource", "AsyncPhoneNumberAssignmentByProfileResource"]


class PhoneNumberAssignmentByProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberAssignmentByProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberAssignmentByProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberAssignmentByProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumberAssignmentByProfileResourceWithStreamingResponse(self)

    def assign(
        self,
        *,
        messaging_profile_id: str,
        campaign_id: str | Omit = omit,
        tcr_campaign_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignmentByProfileAssignResponse:
        """
        This endpoint allows you to link all phone numbers associated with a Messaging
        Profile to a campaign. **Please note:** if you want to assign phone numbers to a
        campaign that you did not create with Telnyx 10DLC services, this endpoint
        allows that provided that you've shared the campaign with Telnyx. In this case,
        only provide the parameter, `tcrCampaignId`, and not `campaignId`. In all other
        cases (where the campaign you're assigning was created with Telnyx 10DLC
        services), only provide `campaignId`, not `tcrCampaignId`.

        Args:
          messaging_profile_id: The ID of the messaging profile that you want to link to the specified campaign.

          campaign_id: The ID of the campaign you want to link to the specified messaging profile. If
              you supply this ID in the request, do not also include a tcrCampaignId.

          tcr_campaign_id: The TCR ID of the shared campaign you want to link to the specified messaging
              profile (for campaigns not created using Telnyx 10DLC services only). If you
              supply this ID in the request, do not also include a campaignId.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/10dlc/phoneNumberAssignmentByProfile",
            body=maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "campaign_id": campaign_id,
                    "tcr_campaign_id": tcr_campaign_id,
                },
                phone_number_assignment_by_profile_assign_params.PhoneNumberAssignmentByProfileAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAssignmentByProfileAssignResponse,
        )

    def get_phone_number_status(
        self,
        task_id: str,
        *,
        page: int | Omit = omit,
        records_per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignmentByProfileGetPhoneNumberStatusResponse:
        """
        Check the status of the individual phone number/campaign assignments associated
        with the supplied `taskId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/10dlc/phoneNumberAssignmentByProfile/{task_id}/phoneNumbers",
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
                    phone_number_assignment_by_profile_get_phone_number_status_params.PhoneNumberAssignmentByProfileGetPhoneNumberStatusParams,
                ),
            ),
            cast_to=PhoneNumberAssignmentByProfileGetPhoneNumberStatusResponse,
        )

    def get_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignmentByProfileGetTaskStatusResponse:
        """
        Check the status of the task associated with assigning all phone numbers on a
        messaging profile to a campaign by `taskId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/10dlc/phoneNumberAssignmentByProfile/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAssignmentByProfileGetTaskStatusResponse,
        )


class AsyncPhoneNumberAssignmentByProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse(self)

    async def assign(
        self,
        *,
        messaging_profile_id: str,
        campaign_id: str | Omit = omit,
        tcr_campaign_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignmentByProfileAssignResponse:
        """
        This endpoint allows you to link all phone numbers associated with a Messaging
        Profile to a campaign. **Please note:** if you want to assign phone numbers to a
        campaign that you did not create with Telnyx 10DLC services, this endpoint
        allows that provided that you've shared the campaign with Telnyx. In this case,
        only provide the parameter, `tcrCampaignId`, and not `campaignId`. In all other
        cases (where the campaign you're assigning was created with Telnyx 10DLC
        services), only provide `campaignId`, not `tcrCampaignId`.

        Args:
          messaging_profile_id: The ID of the messaging profile that you want to link to the specified campaign.

          campaign_id: The ID of the campaign you want to link to the specified messaging profile. If
              you supply this ID in the request, do not also include a tcrCampaignId.

          tcr_campaign_id: The TCR ID of the shared campaign you want to link to the specified messaging
              profile (for campaigns not created using Telnyx 10DLC services only). If you
              supply this ID in the request, do not also include a campaignId.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/10dlc/phoneNumberAssignmentByProfile",
            body=await async_maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "campaign_id": campaign_id,
                    "tcr_campaign_id": tcr_campaign_id,
                },
                phone_number_assignment_by_profile_assign_params.PhoneNumberAssignmentByProfileAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAssignmentByProfileAssignResponse,
        )

    async def get_phone_number_status(
        self,
        task_id: str,
        *,
        page: int | Omit = omit,
        records_per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignmentByProfileGetPhoneNumberStatusResponse:
        """
        Check the status of the individual phone number/campaign assignments associated
        with the supplied `taskId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/10dlc/phoneNumberAssignmentByProfile/{task_id}/phoneNumbers",
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
                    phone_number_assignment_by_profile_get_phone_number_status_params.PhoneNumberAssignmentByProfileGetPhoneNumberStatusParams,
                ),
            ),
            cast_to=PhoneNumberAssignmentByProfileGetPhoneNumberStatusResponse,
        )

    async def get_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAssignmentByProfileGetTaskStatusResponse:
        """
        Check the status of the task associated with assigning all phone numbers on a
        messaging profile to a campaign by `taskId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/10dlc/phoneNumberAssignmentByProfile/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAssignmentByProfileGetTaskStatusResponse,
        )


class PhoneNumberAssignmentByProfileResourceWithRawResponse:
    def __init__(self, phone_number_assignment_by_profile: PhoneNumberAssignmentByProfileResource) -> None:
        self._phone_number_assignment_by_profile = phone_number_assignment_by_profile

        self.assign = to_raw_response_wrapper(
            phone_number_assignment_by_profile.assign,
        )
        self.get_phone_number_status = to_raw_response_wrapper(
            phone_number_assignment_by_profile.get_phone_number_status,
        )
        self.get_task_status = to_raw_response_wrapper(
            phone_number_assignment_by_profile.get_task_status,
        )


class AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse:
    def __init__(self, phone_number_assignment_by_profile: AsyncPhoneNumberAssignmentByProfileResource) -> None:
        self._phone_number_assignment_by_profile = phone_number_assignment_by_profile

        self.assign = async_to_raw_response_wrapper(
            phone_number_assignment_by_profile.assign,
        )
        self.get_phone_number_status = async_to_raw_response_wrapper(
            phone_number_assignment_by_profile.get_phone_number_status,
        )
        self.get_task_status = async_to_raw_response_wrapper(
            phone_number_assignment_by_profile.get_task_status,
        )


class PhoneNumberAssignmentByProfileResourceWithStreamingResponse:
    def __init__(self, phone_number_assignment_by_profile: PhoneNumberAssignmentByProfileResource) -> None:
        self._phone_number_assignment_by_profile = phone_number_assignment_by_profile

        self.assign = to_streamed_response_wrapper(
            phone_number_assignment_by_profile.assign,
        )
        self.get_phone_number_status = to_streamed_response_wrapper(
            phone_number_assignment_by_profile.get_phone_number_status,
        )
        self.get_task_status = to_streamed_response_wrapper(
            phone_number_assignment_by_profile.get_task_status,
        )


class AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse:
    def __init__(self, phone_number_assignment_by_profile: AsyncPhoneNumberAssignmentByProfileResource) -> None:
        self._phone_number_assignment_by_profile = phone_number_assignment_by_profile

        self.assign = async_to_streamed_response_wrapper(
            phone_number_assignment_by_profile.assign,
        )
        self.get_phone_number_status = async_to_streamed_response_wrapper(
            phone_number_assignment_by_profile.get_phone_number_status,
        )
        self.get_task_status = async_to_streamed_response_wrapper(
            phone_number_assignment_by_profile.get_task_status,
        )
