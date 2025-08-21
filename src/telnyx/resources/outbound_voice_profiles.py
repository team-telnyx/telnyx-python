# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    ServicePlan,
    TrafficType,
    UsagePaymentMethod,
    outbound_voice_profile_list_params,
    outbound_voice_profile_create_params,
    outbound_voice_profile_update_params,
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
from ..types.service_plan import ServicePlan
from ..types.traffic_type import TrafficType
from ..types.usage_payment_method import UsagePaymentMethod
from ..types.outbound_call_recording_param import OutboundCallRecordingParam
from ..types.outbound_voice_profile_list_response import OutboundVoiceProfileListResponse
from ..types.outbound_voice_profile_create_response import OutboundVoiceProfileCreateResponse
from ..types.outbound_voice_profile_delete_response import OutboundVoiceProfileDeleteResponse
from ..types.outbound_voice_profile_update_response import OutboundVoiceProfileUpdateResponse
from ..types.outbound_voice_profile_retrieve_response import OutboundVoiceProfileRetrieveResponse

__all__ = ["OutboundVoiceProfilesResource", "AsyncOutboundVoiceProfilesResource"]


class OutboundVoiceProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutboundVoiceProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OutboundVoiceProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutboundVoiceProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OutboundVoiceProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        billing_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        call_recording: OutboundCallRecordingParam | NotGiven = NOT_GIVEN,
        concurrent_call_limit: Optional[int] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        max_destination_rate: float | NotGiven = NOT_GIVEN,
        service_plan: ServicePlan | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        traffic_type: TrafficType | NotGiven = NOT_GIVEN,
        usage_payment_method: UsagePaymentMethod | NotGiven = NOT_GIVEN,
        whitelisted_destinations: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileCreateResponse:
        """
        Create an outbound voice profile.

        Args:
          name: A user-supplied name to help with organization.

          billing_group_id: The ID of the billing group associated with the outbound proflile. Defaults to
              null (for no group assigned).

          concurrent_call_limit: Must be no more than your global concurrent call limit. Null means no limit.

          daily_spend_limit: The maximum amount of usage charges, in USD, you want Telnyx to allow on this
              outbound voice profile in a day before disallowing new calls.

          daily_spend_limit_enabled: Specifies whether to enforce the daily_spend_limit on this outbound voice
              profile.

          enabled: Specifies whether the outbound voice profile can be used. Disabled profiles will
              result in outbound calls being blocked for the associated Connections.

          max_destination_rate: Maximum rate (price per minute) for a Destination to be allowed when making
              outbound calls.

          service_plan: Indicates the coverage of the termination regions.

          traffic_type: Specifies the type of traffic allowed in this profile.

          usage_payment_method: Setting for how costs for outbound profile are calculated.

          whitelisted_destinations: The list of destinations you want to be able to call using this outbound voice
              profile formatted in alpha2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/outbound_voice_profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "billing_group_id": billing_group_id,
                    "call_recording": call_recording,
                    "concurrent_call_limit": concurrent_call_limit,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "max_destination_rate": max_destination_rate,
                    "service_plan": service_plan,
                    "tags": tags,
                    "traffic_type": traffic_type,
                    "usage_payment_method": usage_payment_method,
                    "whitelisted_destinations": whitelisted_destinations,
                },
                outbound_voice_profile_create_params.OutboundVoiceProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileRetrieveResponse:
        """
        Retrieves the details of an existing outbound voice profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/outbound_voice_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        billing_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        call_recording: OutboundCallRecordingParam | NotGiven = NOT_GIVEN,
        concurrent_call_limit: Optional[int] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        max_destination_rate: float | NotGiven = NOT_GIVEN,
        service_plan: ServicePlan | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        traffic_type: TrafficType | NotGiven = NOT_GIVEN,
        usage_payment_method: UsagePaymentMethod | NotGiven = NOT_GIVEN,
        whitelisted_destinations: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileUpdateResponse:
        """
        Updates an existing outbound voice profile.

        Args:
          name: A user-supplied name to help with organization.

          billing_group_id: The ID of the billing group associated with the outbound proflile. Defaults to
              null (for no group assigned).

          concurrent_call_limit: Must be no more than your global concurrent call limit. Null means no limit.

          daily_spend_limit: The maximum amount of usage charges, in USD, you want Telnyx to allow on this
              outbound voice profile in a day before disallowing new calls.

          daily_spend_limit_enabled: Specifies whether to enforce the daily_spend_limit on this outbound voice
              profile.

          enabled: Specifies whether the outbound voice profile can be used. Disabled profiles will
              result in outbound calls being blocked for the associated Connections.

          max_destination_rate: Maximum rate (price per minute) for a Destination to be allowed when making
              outbound calls.

          service_plan: Indicates the coverage of the termination regions.

          traffic_type: Specifies the type of traffic allowed in this profile.

          usage_payment_method: Setting for how costs for outbound profile are calculated.

          whitelisted_destinations: The list of destinations you want to be able to call using this outbound voice
              profile formatted in alpha2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/outbound_voice_profiles/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "billing_group_id": billing_group_id,
                    "call_recording": call_recording,
                    "concurrent_call_limit": concurrent_call_limit,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "max_destination_rate": max_destination_rate,
                    "service_plan": service_plan,
                    "tags": tags,
                    "traffic_type": traffic_type,
                    "usage_payment_method": usage_payment_method,
                    "whitelisted_destinations": whitelisted_destinations,
                },
                outbound_voice_profile_update_params.OutboundVoiceProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileUpdateResponse,
        )

    def list(
        self,
        *,
        filter: outbound_voice_profile_list_params.Filter | NotGiven = NOT_GIVEN,
        page: outbound_voice_profile_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal[
            "enabled",
            "-enabled",
            "created_at",
            "-created_at",
            "name",
            "-name",
            "service_plan",
            "-service_plan",
            "traffic_type",
            "-traffic_type",
            "usage_payment_method",
            "-usage_payment_method",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileListResponse:
        """
        Get all outbound voice profiles belonging to the user that match the given
        filters.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[name][contains]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code>-</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>name</code>: sorts the result by the
                  <code>name</code> field in ascending order.
                </li>

                <li>
                  <code>-name</code>: sorts the result by the
                  <code>name</code> field in descending order.
                </li>
              </ul> <br/>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/outbound_voice_profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    outbound_voice_profile_list_params.OutboundVoiceProfileListParams,
                ),
            ),
            cast_to=OutboundVoiceProfileListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileDeleteResponse:
        """
        Deletes an existing outbound voice profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/outbound_voice_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileDeleteResponse,
        )


class AsyncOutboundVoiceProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutboundVoiceProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutboundVoiceProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutboundVoiceProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOutboundVoiceProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        billing_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        call_recording: OutboundCallRecordingParam | NotGiven = NOT_GIVEN,
        concurrent_call_limit: Optional[int] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        max_destination_rate: float | NotGiven = NOT_GIVEN,
        service_plan: ServicePlan | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        traffic_type: TrafficType | NotGiven = NOT_GIVEN,
        usage_payment_method: UsagePaymentMethod | NotGiven = NOT_GIVEN,
        whitelisted_destinations: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileCreateResponse:
        """
        Create an outbound voice profile.

        Args:
          name: A user-supplied name to help with organization.

          billing_group_id: The ID of the billing group associated with the outbound proflile. Defaults to
              null (for no group assigned).

          concurrent_call_limit: Must be no more than your global concurrent call limit. Null means no limit.

          daily_spend_limit: The maximum amount of usage charges, in USD, you want Telnyx to allow on this
              outbound voice profile in a day before disallowing new calls.

          daily_spend_limit_enabled: Specifies whether to enforce the daily_spend_limit on this outbound voice
              profile.

          enabled: Specifies whether the outbound voice profile can be used. Disabled profiles will
              result in outbound calls being blocked for the associated Connections.

          max_destination_rate: Maximum rate (price per minute) for a Destination to be allowed when making
              outbound calls.

          service_plan: Indicates the coverage of the termination regions.

          traffic_type: Specifies the type of traffic allowed in this profile.

          usage_payment_method: Setting for how costs for outbound profile are calculated.

          whitelisted_destinations: The list of destinations you want to be able to call using this outbound voice
              profile formatted in alpha2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/outbound_voice_profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "billing_group_id": billing_group_id,
                    "call_recording": call_recording,
                    "concurrent_call_limit": concurrent_call_limit,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "max_destination_rate": max_destination_rate,
                    "service_plan": service_plan,
                    "tags": tags,
                    "traffic_type": traffic_type,
                    "usage_payment_method": usage_payment_method,
                    "whitelisted_destinations": whitelisted_destinations,
                },
                outbound_voice_profile_create_params.OutboundVoiceProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileRetrieveResponse:
        """
        Retrieves the details of an existing outbound voice profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/outbound_voice_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        billing_group_id: Optional[str] | NotGiven = NOT_GIVEN,
        call_recording: OutboundCallRecordingParam | NotGiven = NOT_GIVEN,
        concurrent_call_limit: Optional[int] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        max_destination_rate: float | NotGiven = NOT_GIVEN,
        service_plan: ServicePlan | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        traffic_type: TrafficType | NotGiven = NOT_GIVEN,
        usage_payment_method: UsagePaymentMethod | NotGiven = NOT_GIVEN,
        whitelisted_destinations: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileUpdateResponse:
        """
        Updates an existing outbound voice profile.

        Args:
          name: A user-supplied name to help with organization.

          billing_group_id: The ID of the billing group associated with the outbound proflile. Defaults to
              null (for no group assigned).

          concurrent_call_limit: Must be no more than your global concurrent call limit. Null means no limit.

          daily_spend_limit: The maximum amount of usage charges, in USD, you want Telnyx to allow on this
              outbound voice profile in a day before disallowing new calls.

          daily_spend_limit_enabled: Specifies whether to enforce the daily_spend_limit on this outbound voice
              profile.

          enabled: Specifies whether the outbound voice profile can be used. Disabled profiles will
              result in outbound calls being blocked for the associated Connections.

          max_destination_rate: Maximum rate (price per minute) for a Destination to be allowed when making
              outbound calls.

          service_plan: Indicates the coverage of the termination regions.

          traffic_type: Specifies the type of traffic allowed in this profile.

          usage_payment_method: Setting for how costs for outbound profile are calculated.

          whitelisted_destinations: The list of destinations you want to be able to call using this outbound voice
              profile formatted in alpha2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/outbound_voice_profiles/{id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "billing_group_id": billing_group_id,
                    "call_recording": call_recording,
                    "concurrent_call_limit": concurrent_call_limit,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "max_destination_rate": max_destination_rate,
                    "service_plan": service_plan,
                    "tags": tags,
                    "traffic_type": traffic_type,
                    "usage_payment_method": usage_payment_method,
                    "whitelisted_destinations": whitelisted_destinations,
                },
                outbound_voice_profile_update_params.OutboundVoiceProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: outbound_voice_profile_list_params.Filter | NotGiven = NOT_GIVEN,
        page: outbound_voice_profile_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal[
            "enabled",
            "-enabled",
            "created_at",
            "-created_at",
            "name",
            "-name",
            "service_plan",
            "-service_plan",
            "traffic_type",
            "-traffic_type",
            "usage_payment_method",
            "-usage_payment_method",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileListResponse:
        """
        Get all outbound voice profiles belonging to the user that match the given
        filters.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[name][contains]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code>-</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>name</code>: sorts the result by the
                  <code>name</code> field in ascending order.
                </li>

                <li>
                  <code>-name</code>: sorts the result by the
                  <code>name</code> field in descending order.
                </li>
              </ul> <br/>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/outbound_voice_profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    outbound_voice_profile_list_params.OutboundVoiceProfileListParams,
                ),
            ),
            cast_to=OutboundVoiceProfileListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundVoiceProfileDeleteResponse:
        """
        Deletes an existing outbound voice profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/outbound_voice_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundVoiceProfileDeleteResponse,
        )


class OutboundVoiceProfilesResourceWithRawResponse:
    def __init__(self, outbound_voice_profiles: OutboundVoiceProfilesResource) -> None:
        self._outbound_voice_profiles = outbound_voice_profiles

        self.create = to_raw_response_wrapper(
            outbound_voice_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            outbound_voice_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            outbound_voice_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            outbound_voice_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            outbound_voice_profiles.delete,
        )


class AsyncOutboundVoiceProfilesResourceWithRawResponse:
    def __init__(self, outbound_voice_profiles: AsyncOutboundVoiceProfilesResource) -> None:
        self._outbound_voice_profiles = outbound_voice_profiles

        self.create = async_to_raw_response_wrapper(
            outbound_voice_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            outbound_voice_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            outbound_voice_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            outbound_voice_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            outbound_voice_profiles.delete,
        )


class OutboundVoiceProfilesResourceWithStreamingResponse:
    def __init__(self, outbound_voice_profiles: OutboundVoiceProfilesResource) -> None:
        self._outbound_voice_profiles = outbound_voice_profiles

        self.create = to_streamed_response_wrapper(
            outbound_voice_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            outbound_voice_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            outbound_voice_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            outbound_voice_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            outbound_voice_profiles.delete,
        )


class AsyncOutboundVoiceProfilesResourceWithStreamingResponse:
    def __init__(self, outbound_voice_profiles: AsyncOutboundVoiceProfilesResource) -> None:
        self._outbound_voice_profiles = outbound_voice_profiles

        self.create = async_to_streamed_response_wrapper(
            outbound_voice_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            outbound_voice_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            outbound_voice_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            outbound_voice_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            outbound_voice_profiles.delete,
        )
