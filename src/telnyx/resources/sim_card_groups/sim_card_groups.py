# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import (
    sim_card_group_list_params,
    sim_card_group_create_params,
    sim_card_group_update_params,
    sim_card_group_retrieve_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
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
from ...types.sim_card_group_list_response import SimCardGroupListResponse
from ...types.sim_card_group_create_response import SimCardGroupCreateResponse
from ...types.sim_card_group_delete_response import SimCardGroupDeleteResponse
from ...types.sim_card_group_update_response import SimCardGroupUpdateResponse
from ...types.sim_card_group_retrieve_response import SimCardGroupRetrieveResponse

__all__ = ["SimCardGroupsResource", "AsyncSimCardGroupsResource"]


class SimCardGroupsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SimCardGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SimCardGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimCardGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SimCardGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        data_limit: sim_card_group_create_params.DataLimit | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupCreateResponse:
        """
        Creates a new SIM card group object

        Args:
          name: A user friendly name for the SIM card group.

          data_limit: Upper limit on the amount of data the SIM cards, within the group, can use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sim_card_groups",
            body=maybe_transform(
                {
                    "name": name,
                    "data_limit": data_limit,
                },
                sim_card_group_create_params.SimCardGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGroupCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        include_iccids: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupRetrieveResponse:
        """
        Returns the details regarding a specific SIM card group

        Args:
          include_iccids: It includes a list of associated ICCIDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_card_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_iccids": include_iccids}, sim_card_group_retrieve_params.SimCardGroupRetrieveParams
                ),
            ),
            cast_to=SimCardGroupRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        data_limit: sim_card_group_update_params.DataLimit | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupUpdateResponse:
        """
        Updates a SIM card group

        Args:
          data_limit: Upper limit on the amount of data the SIM cards, within the group, can use.

          name: A user friendly name for the SIM card group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/sim_card_groups/{id}",
            body=maybe_transform(
                {
                    "data_limit": data_limit,
                    "name": name,
                },
                sim_card_group_update_params.SimCardGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGroupUpdateResponse,
        )

    def list(
        self,
        *,
        filter_name: str | NotGiven = NOT_GIVEN,
        filter_private_wireless_gateway_id: str | NotGiven = NOT_GIVEN,
        filter_wireless_blocklist_id: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupListResponse:
        """
        Get all SIM card groups belonging to the user that match the given filters.

        Args:
          filter_name: A valid SIM card group name.

          filter_private_wireless_gateway_id: A Private Wireless Gateway ID associated with the group.

          filter_wireless_blocklist_id: A Wireless Blocklist ID associated with the group.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sim_card_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_private_wireless_gateway_id": filter_private_wireless_gateway_id,
                        "filter_wireless_blocklist_id": filter_wireless_blocklist_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    sim_card_group_list_params.SimCardGroupListParams,
                ),
            ),
            cast_to=SimCardGroupListResponse,
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
    ) -> SimCardGroupDeleteResponse:
        """
        Permanently deletes a SIM card group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/sim_card_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGroupDeleteResponse,
        )


class AsyncSimCardGroupsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimCardGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimCardGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimCardGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSimCardGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        data_limit: sim_card_group_create_params.DataLimit | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupCreateResponse:
        """
        Creates a new SIM card group object

        Args:
          name: A user friendly name for the SIM card group.

          data_limit: Upper limit on the amount of data the SIM cards, within the group, can use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sim_card_groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "data_limit": data_limit,
                },
                sim_card_group_create_params.SimCardGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGroupCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        include_iccids: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupRetrieveResponse:
        """
        Returns the details regarding a specific SIM card group

        Args:
          include_iccids: It includes a list of associated ICCIDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_card_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_iccids": include_iccids}, sim_card_group_retrieve_params.SimCardGroupRetrieveParams
                ),
            ),
            cast_to=SimCardGroupRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        data_limit: sim_card_group_update_params.DataLimit | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupUpdateResponse:
        """
        Updates a SIM card group

        Args:
          data_limit: Upper limit on the amount of data the SIM cards, within the group, can use.

          name: A user friendly name for the SIM card group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/sim_card_groups/{id}",
            body=await async_maybe_transform(
                {
                    "data_limit": data_limit,
                    "name": name,
                },
                sim_card_group_update_params.SimCardGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGroupUpdateResponse,
        )

    async def list(
        self,
        *,
        filter_name: str | NotGiven = NOT_GIVEN,
        filter_private_wireless_gateway_id: str | NotGiven = NOT_GIVEN,
        filter_wireless_blocklist_id: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGroupListResponse:
        """
        Get all SIM card groups belonging to the user that match the given filters.

        Args:
          filter_name: A valid SIM card group name.

          filter_private_wireless_gateway_id: A Private Wireless Gateway ID associated with the group.

          filter_wireless_blocklist_id: A Wireless Blocklist ID associated with the group.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sim_card_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_private_wireless_gateway_id": filter_private_wireless_gateway_id,
                        "filter_wireless_blocklist_id": filter_wireless_blocklist_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    sim_card_group_list_params.SimCardGroupListParams,
                ),
            ),
            cast_to=SimCardGroupListResponse,
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
    ) -> SimCardGroupDeleteResponse:
        """
        Permanently deletes a SIM card group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/sim_card_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGroupDeleteResponse,
        )


class SimCardGroupsResourceWithRawResponse:
    def __init__(self, sim_card_groups: SimCardGroupsResource) -> None:
        self._sim_card_groups = sim_card_groups

        self.create = to_raw_response_wrapper(
            sim_card_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sim_card_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sim_card_groups.update,
        )
        self.list = to_raw_response_wrapper(
            sim_card_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            sim_card_groups.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._sim_card_groups.actions)


class AsyncSimCardGroupsResourceWithRawResponse:
    def __init__(self, sim_card_groups: AsyncSimCardGroupsResource) -> None:
        self._sim_card_groups = sim_card_groups

        self.create = async_to_raw_response_wrapper(
            sim_card_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sim_card_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sim_card_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            sim_card_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sim_card_groups.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._sim_card_groups.actions)


class SimCardGroupsResourceWithStreamingResponse:
    def __init__(self, sim_card_groups: SimCardGroupsResource) -> None:
        self._sim_card_groups = sim_card_groups

        self.create = to_streamed_response_wrapper(
            sim_card_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sim_card_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sim_card_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            sim_card_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            sim_card_groups.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._sim_card_groups.actions)


class AsyncSimCardGroupsResourceWithStreamingResponse:
    def __init__(self, sim_card_groups: AsyncSimCardGroupsResource) -> None:
        self._sim_card_groups = sim_card_groups

        self.create = async_to_streamed_response_wrapper(
            sim_card_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sim_card_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sim_card_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sim_card_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sim_card_groups.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._sim_card_groups.actions)
