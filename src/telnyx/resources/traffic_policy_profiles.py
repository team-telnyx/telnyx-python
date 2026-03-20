# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    traffic_policy_profile_list_params,
    traffic_policy_profile_create_params,
    traffic_policy_profile_update_params,
    traffic_policy_profile_list_services_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.traffic_policy_profile_list_response import TrafficPolicyProfileListResponse
from ..types.traffic_policy_profile_create_response import TrafficPolicyProfileCreateResponse
from ..types.traffic_policy_profile_delete_response import TrafficPolicyProfileDeleteResponse
from ..types.traffic_policy_profile_update_response import TrafficPolicyProfileUpdateResponse
from ..types.traffic_policy_profile_retrieve_response import TrafficPolicyProfileRetrieveResponse
from ..types.traffic_policy_profile_list_services_response import TrafficPolicyProfileListServicesResponse

__all__ = ["TrafficPolicyProfilesResource", "AsyncTrafficPolicyProfilesResource"]


class TrafficPolicyProfilesResource(SyncAPIResource):
    """Traffic Policy Profiles operations"""

    @cached_property
    def with_raw_response(self) -> TrafficPolicyProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TrafficPolicyProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrafficPolicyProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TrafficPolicyProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["whitelist", "blacklist"],
        domains: SequenceNotStr[str] | Omit = omit,
        ip_ranges: SequenceNotStr[str] | Omit = omit,
        limit_bw_kbps: Literal[512, 1024] | Omit = omit,
        services: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileCreateResponse:
        """Create a new traffic policy profile.

        At least one of `services`, `ip_ranges`, or
        `domains` must be provided.

        Args:
          type: The type of the traffic policy profile.

          domains: Array of domain names.

          ip_ranges: Array of IP ranges in CIDR notation.

          limit_bw_kbps: Bandwidth limit in kbps. Must be 512 or 1024.

          services: Array of PCEF service IDs to include in the profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/traffic_policy_profiles",
            body=maybe_transform(
                {
                    "type": type,
                    "domains": domains,
                    "ip_ranges": ip_ranges,
                    "limit_bw_kbps": limit_bw_kbps,
                    "services": services,
                },
                traffic_policy_profile_create_params.TrafficPolicyProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileRetrieveResponse:
        """
        Returns the details regarding a specific traffic policy profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/traffic_policy_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        domains: SequenceNotStr[str] | Omit = omit,
        ip_ranges: SequenceNotStr[str] | Omit = omit,
        limit_bw_kbps: Optional[Literal[512, 1024]] | Omit = omit,
        services: SequenceNotStr[str] | Omit = omit,
        type: Literal["whitelist", "blacklist", "throttling"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileUpdateResponse:
        """
        Updates a traffic policy profile.

        Args:
          domains: Array of domain names.

          ip_ranges: Array of IP ranges in CIDR notation.

          limit_bw_kbps: Bandwidth limit in kbps. Must be 512 or 1024, or null to remove.

          services: Array of PCEF service IDs to include in the profile.

          type: The type of the traffic policy profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/traffic_policy_profiles/{id}", id=id),
            body=maybe_transform(
                {
                    "domains": domains,
                    "ip_ranges": ip_ranges,
                    "limit_bw_kbps": limit_bw_kbps,
                    "services": services,
                    "type": type,
                },
                traffic_policy_profile_update_params.TrafficPolicyProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileUpdateResponse,
        )

    def list(
        self,
        *,
        filter_service: str | Omit = omit,
        filter_type: Literal["whitelist", "blacklist", "throttling"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["service", "-service", "type", "-type"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[TrafficPolicyProfileListResponse]:
        """
        Get all traffic policy profiles belonging to the user that match the given
        filters.

        Args:
          filter_service: Filter by service ID.

          filter_type: Filter by traffic policy profile type.

          page_number: The page number to load.

          page_size: The size of the page.

          sort: Sorts traffic policy profiles by the given field. Defaults to ascending order
              unless field is prefixed with a minus sign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/traffic_policy_profiles",
            page=SyncDefaultFlatPagination[TrafficPolicyProfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_service": filter_service,
                        "filter_type": filter_type,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    traffic_policy_profile_list_params.TrafficPolicyProfileListParams,
                ),
            ),
            model=TrafficPolicyProfileListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileDeleteResponse:
        """
        Deletes the traffic policy profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/traffic_policy_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileDeleteResponse,
        )

    def list_services(
        self,
        *,
        filter_group: str | Omit = omit,
        filter_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse]:
        """
        Get all available PCEF services that can be used in traffic policy profiles.

        Args:
          filter_group: Filter services by group.

          filter_name: Filter services by name.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/traffic_policy_profiles/services",
            page=SyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_group": filter_group,
                        "filter_name": filter_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    traffic_policy_profile_list_services_params.TrafficPolicyProfileListServicesParams,
                ),
            ),
            model=TrafficPolicyProfileListServicesResponse,
        )


class AsyncTrafficPolicyProfilesResource(AsyncAPIResource):
    """Traffic Policy Profiles operations"""

    @cached_property
    def with_raw_response(self) -> AsyncTrafficPolicyProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrafficPolicyProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrafficPolicyProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTrafficPolicyProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["whitelist", "blacklist"],
        domains: SequenceNotStr[str] | Omit = omit,
        ip_ranges: SequenceNotStr[str] | Omit = omit,
        limit_bw_kbps: Literal[512, 1024] | Omit = omit,
        services: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileCreateResponse:
        """Create a new traffic policy profile.

        At least one of `services`, `ip_ranges`, or
        `domains` must be provided.

        Args:
          type: The type of the traffic policy profile.

          domains: Array of domain names.

          ip_ranges: Array of IP ranges in CIDR notation.

          limit_bw_kbps: Bandwidth limit in kbps. Must be 512 or 1024.

          services: Array of PCEF service IDs to include in the profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/traffic_policy_profiles",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "domains": domains,
                    "ip_ranges": ip_ranges,
                    "limit_bw_kbps": limit_bw_kbps,
                    "services": services,
                },
                traffic_policy_profile_create_params.TrafficPolicyProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileRetrieveResponse:
        """
        Returns the details regarding a specific traffic policy profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/traffic_policy_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        domains: SequenceNotStr[str] | Omit = omit,
        ip_ranges: SequenceNotStr[str] | Omit = omit,
        limit_bw_kbps: Optional[Literal[512, 1024]] | Omit = omit,
        services: SequenceNotStr[str] | Omit = omit,
        type: Literal["whitelist", "blacklist", "throttling"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileUpdateResponse:
        """
        Updates a traffic policy profile.

        Args:
          domains: Array of domain names.

          ip_ranges: Array of IP ranges in CIDR notation.

          limit_bw_kbps: Bandwidth limit in kbps. Must be 512 or 1024, or null to remove.

          services: Array of PCEF service IDs to include in the profile.

          type: The type of the traffic policy profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/traffic_policy_profiles/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "domains": domains,
                    "ip_ranges": ip_ranges,
                    "limit_bw_kbps": limit_bw_kbps,
                    "services": services,
                    "type": type,
                },
                traffic_policy_profile_update_params.TrafficPolicyProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileUpdateResponse,
        )

    def list(
        self,
        *,
        filter_service: str | Omit = omit,
        filter_type: Literal["whitelist", "blacklist", "throttling"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["service", "-service", "type", "-type"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TrafficPolicyProfileListResponse, AsyncDefaultFlatPagination[TrafficPolicyProfileListResponse]]:
        """
        Get all traffic policy profiles belonging to the user that match the given
        filters.

        Args:
          filter_service: Filter by service ID.

          filter_type: Filter by traffic policy profile type.

          page_number: The page number to load.

          page_size: The size of the page.

          sort: Sorts traffic policy profiles by the given field. Defaults to ascending order
              unless field is prefixed with a minus sign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/traffic_policy_profiles",
            page=AsyncDefaultFlatPagination[TrafficPolicyProfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_service": filter_service,
                        "filter_type": filter_type,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    traffic_policy_profile_list_params.TrafficPolicyProfileListParams,
                ),
            ),
            model=TrafficPolicyProfileListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrafficPolicyProfileDeleteResponse:
        """
        Deletes the traffic policy profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/traffic_policy_profiles/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrafficPolicyProfileDeleteResponse,
        )

    def list_services(
        self,
        *,
        filter_group: str | Omit = omit,
        filter_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        TrafficPolicyProfileListServicesResponse, AsyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse]
    ]:
        """
        Get all available PCEF services that can be used in traffic policy profiles.

        Args:
          filter_group: Filter services by group.

          filter_name: Filter services by name.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/traffic_policy_profiles/services",
            page=AsyncDefaultFlatPagination[TrafficPolicyProfileListServicesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_group": filter_group,
                        "filter_name": filter_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    traffic_policy_profile_list_services_params.TrafficPolicyProfileListServicesParams,
                ),
            ),
            model=TrafficPolicyProfileListServicesResponse,
        )


class TrafficPolicyProfilesResourceWithRawResponse:
    def __init__(self, traffic_policy_profiles: TrafficPolicyProfilesResource) -> None:
        self._traffic_policy_profiles = traffic_policy_profiles

        self.create = to_raw_response_wrapper(
            traffic_policy_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            traffic_policy_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            traffic_policy_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            traffic_policy_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            traffic_policy_profiles.delete,
        )
        self.list_services = to_raw_response_wrapper(
            traffic_policy_profiles.list_services,
        )


class AsyncTrafficPolicyProfilesResourceWithRawResponse:
    def __init__(self, traffic_policy_profiles: AsyncTrafficPolicyProfilesResource) -> None:
        self._traffic_policy_profiles = traffic_policy_profiles

        self.create = async_to_raw_response_wrapper(
            traffic_policy_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            traffic_policy_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            traffic_policy_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            traffic_policy_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            traffic_policy_profiles.delete,
        )
        self.list_services = async_to_raw_response_wrapper(
            traffic_policy_profiles.list_services,
        )


class TrafficPolicyProfilesResourceWithStreamingResponse:
    def __init__(self, traffic_policy_profiles: TrafficPolicyProfilesResource) -> None:
        self._traffic_policy_profiles = traffic_policy_profiles

        self.create = to_streamed_response_wrapper(
            traffic_policy_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            traffic_policy_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            traffic_policy_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            traffic_policy_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            traffic_policy_profiles.delete,
        )
        self.list_services = to_streamed_response_wrapper(
            traffic_policy_profiles.list_services,
        )


class AsyncTrafficPolicyProfilesResourceWithStreamingResponse:
    def __init__(self, traffic_policy_profiles: AsyncTrafficPolicyProfilesResource) -> None:
        self._traffic_policy_profiles = traffic_policy_profiles

        self.create = async_to_streamed_response_wrapper(
            traffic_policy_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            traffic_policy_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            traffic_policy_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            traffic_policy_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            traffic_policy_profiles.delete,
        )
        self.list_services = async_to_streamed_response_wrapper(
            traffic_policy_profiles.list_services,
        )
