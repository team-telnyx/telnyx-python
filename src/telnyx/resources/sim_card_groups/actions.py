# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.sim_card_groups import (
    action_list_params,
    action_set_wireless_blocklist_params,
    action_set_private_wireless_gateway_params,
)
from ...types.sim_card_groups.action_list_response import ActionListResponse
from ...types.sim_card_groups.action_retrieve_response import ActionRetrieveResponse
from ...types.sim_card_groups.action_set_wireless_blocklist_response import ActionSetWirelessBlocklistResponse
from ...types.sim_card_groups.action_remove_wireless_blocklist_response import ActionRemoveWirelessBlocklistResponse
from ...types.sim_card_groups.action_set_private_wireless_gateway_response import (
    ActionSetPrivateWirelessGatewayResponse,
)
from ...types.sim_card_groups.action_remove_private_wireless_gateway_response import (
    ActionRemovePrivateWirelessGatewayResponse,
)

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

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
    ) -> ActionRetrieveResponse:
        """
        This API allows fetching detailed information about a SIM card group action
        resource to make follow-ups in an existing asynchronous operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_card_group_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_sim_card_group_id: str | NotGiven = NOT_GIVEN,
        filter_status: Literal["in-progress", "completed", "failed"] | NotGiven = NOT_GIVEN,
        filter_type: Literal[
            "set_private_wireless_gateway",
            "remove_private_wireless_gateway",
            "set_wireless_blocklist",
            "remove_wireless_blocklist",
        ]
        | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """This API allows listing a paginated collection a SIM card group actions.

        It
        allows to explore a collection of existing asynchronous operation using specific
        filters.

        Args:
          filter_sim_card_group_id: A valid SIM card group ID.

          filter_status: Filter by a specific status of the resource's lifecycle.

          filter_type: Filter by action type.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sim_card_group_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_sim_card_group_id": filter_sim_card_group_id,
                        "filter_status": filter_status,
                        "filter_type": filter_type,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    def remove_private_wireless_gateway(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemovePrivateWirelessGatewayResponse:
        """
        This action will asynchronously remove an existing Private Wireless Gateway
        definition from a SIM card group. Completing this operation defines that all SIM
        cards in the SIM card group will get their traffic handled by Telnyx's default
        mobile network configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_card_groups/{id}/actions/remove_private_wireless_gateway",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemovePrivateWirelessGatewayResponse,
        )

    def remove_wireless_blocklist(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveWirelessBlocklistResponse:
        """
        This action will asynchronously remove an existing Wireless Blocklist to all the
        SIMs in the SIM card group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_card_groups/{id}/actions/remove_wireless_blocklist",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveWirelessBlocklistResponse,
        )

    def set_private_wireless_gateway(
        self,
        id: str,
        *,
        private_wireless_gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetPrivateWirelessGatewayResponse:
        """
        This action will asynchronously assign a provisioned Private Wireless Gateway to
        the SIM card group. Completing this operation defines that all SIM cards in the
        SIM card group will get their traffic controlled by the associated Private
        Wireless Gateway. This operation will also imply that new SIM cards assigned to
        a group will inherit its network definitions. If it's moved to a different group
        that doesn't have a Private Wireless Gateway, it'll use Telnyx's default mobile
        network configuration.

        Args:
          private_wireless_gateway_id: The identification of the related Private Wireless Gateway resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_card_groups/{id}/actions/set_private_wireless_gateway",
            body=maybe_transform(
                {"private_wireless_gateway_id": private_wireless_gateway_id},
                action_set_private_wireless_gateway_params.ActionSetPrivateWirelessGatewayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetPrivateWirelessGatewayResponse,
        )

    def set_wireless_blocklist(
        self,
        id: str,
        *,
        wireless_blocklist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetWirelessBlocklistResponse:
        """
        This action will asynchronously assign a Wireless Blocklist to all the SIMs in
        the SIM card group.

        Args:
          wireless_blocklist_id: The identification of the related Wireless Blocklist resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_card_groups/{id}/actions/set_wireless_blocklist",
            body=maybe_transform(
                {"wireless_blocklist_id": wireless_blocklist_id},
                action_set_wireless_blocklist_params.ActionSetWirelessBlocklistParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetWirelessBlocklistResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

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
    ) -> ActionRetrieveResponse:
        """
        This API allows fetching detailed information about a SIM card group action
        resource to make follow-ups in an existing asynchronous operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_card_group_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter_sim_card_group_id: str | NotGiven = NOT_GIVEN,
        filter_status: Literal["in-progress", "completed", "failed"] | NotGiven = NOT_GIVEN,
        filter_type: Literal[
            "set_private_wireless_gateway",
            "remove_private_wireless_gateway",
            "set_wireless_blocklist",
            "remove_wireless_blocklist",
        ]
        | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """This API allows listing a paginated collection a SIM card group actions.

        It
        allows to explore a collection of existing asynchronous operation using specific
        filters.

        Args:
          filter_sim_card_group_id: A valid SIM card group ID.

          filter_status: Filter by a specific status of the resource's lifecycle.

          filter_type: Filter by action type.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sim_card_group_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_sim_card_group_id": filter_sim_card_group_id,
                        "filter_status": filter_status,
                        "filter_type": filter_type,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    async def remove_private_wireless_gateway(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemovePrivateWirelessGatewayResponse:
        """
        This action will asynchronously remove an existing Private Wireless Gateway
        definition from a SIM card group. Completing this operation defines that all SIM
        cards in the SIM card group will get their traffic handled by Telnyx's default
        mobile network configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_card_groups/{id}/actions/remove_private_wireless_gateway",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemovePrivateWirelessGatewayResponse,
        )

    async def remove_wireless_blocklist(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveWirelessBlocklistResponse:
        """
        This action will asynchronously remove an existing Wireless Blocklist to all the
        SIMs in the SIM card group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_card_groups/{id}/actions/remove_wireless_blocklist",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveWirelessBlocklistResponse,
        )

    async def set_private_wireless_gateway(
        self,
        id: str,
        *,
        private_wireless_gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetPrivateWirelessGatewayResponse:
        """
        This action will asynchronously assign a provisioned Private Wireless Gateway to
        the SIM card group. Completing this operation defines that all SIM cards in the
        SIM card group will get their traffic controlled by the associated Private
        Wireless Gateway. This operation will also imply that new SIM cards assigned to
        a group will inherit its network definitions. If it's moved to a different group
        that doesn't have a Private Wireless Gateway, it'll use Telnyx's default mobile
        network configuration.

        Args:
          private_wireless_gateway_id: The identification of the related Private Wireless Gateway resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_card_groups/{id}/actions/set_private_wireless_gateway",
            body=await async_maybe_transform(
                {"private_wireless_gateway_id": private_wireless_gateway_id},
                action_set_private_wireless_gateway_params.ActionSetPrivateWirelessGatewayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetPrivateWirelessGatewayResponse,
        )

    async def set_wireless_blocklist(
        self,
        id: str,
        *,
        wireless_blocklist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetWirelessBlocklistResponse:
        """
        This action will asynchronously assign a Wireless Blocklist to all the SIMs in
        the SIM card group.

        Args:
          wireless_blocklist_id: The identification of the related Wireless Blocklist resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_card_groups/{id}/actions/set_wireless_blocklist",
            body=await async_maybe_transform(
                {"wireless_blocklist_id": wireless_blocklist_id},
                action_set_wireless_blocklist_params.ActionSetWirelessBlocklistParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetWirelessBlocklistResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )
        self.remove_private_wireless_gateway = to_raw_response_wrapper(
            actions.remove_private_wireless_gateway,
        )
        self.remove_wireless_blocklist = to_raw_response_wrapper(
            actions.remove_wireless_blocklist,
        )
        self.set_private_wireless_gateway = to_raw_response_wrapper(
            actions.set_private_wireless_gateway,
        )
        self.set_wireless_blocklist = to_raw_response_wrapper(
            actions.set_wireless_blocklist,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.remove_private_wireless_gateway = async_to_raw_response_wrapper(
            actions.remove_private_wireless_gateway,
        )
        self.remove_wireless_blocklist = async_to_raw_response_wrapper(
            actions.remove_wireless_blocklist,
        )
        self.set_private_wireless_gateway = async_to_raw_response_wrapper(
            actions.set_private_wireless_gateway,
        )
        self.set_wireless_blocklist = async_to_raw_response_wrapper(
            actions.set_wireless_blocklist,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.remove_private_wireless_gateway = to_streamed_response_wrapper(
            actions.remove_private_wireless_gateway,
        )
        self.remove_wireless_blocklist = to_streamed_response_wrapper(
            actions.remove_wireless_blocklist,
        )
        self.set_private_wireless_gateway = to_streamed_response_wrapper(
            actions.set_private_wireless_gateway,
        )
        self.set_wireless_blocklist = to_streamed_response_wrapper(
            actions.set_wireless_blocklist,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.remove_private_wireless_gateway = async_to_streamed_response_wrapper(
            actions.remove_private_wireless_gateway,
        )
        self.remove_wireless_blocklist = async_to_streamed_response_wrapper(
            actions.remove_wireless_blocklist,
        )
        self.set_private_wireless_gateway = async_to_streamed_response_wrapper(
            actions.set_private_wireless_gateway,
        )
        self.set_wireless_blocklist = async_to_streamed_response_wrapper(
            actions.set_wireless_blocklist,
        )
