# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ...types.sim_cards import (
    action_list_params,
    action_set_public_ip_params,
    action_bulk_set_public_ips_params,
    action_validate_registration_codes_params,
)
from ...types.sim_cards.action_list_response import ActionListResponse
from ...types.sim_cards.action_enable_response import ActionEnableResponse
from ...types.sim_cards.action_disable_response import ActionDisableResponse
from ...types.sim_cards.action_retrieve_response import ActionRetrieveResponse
from ...types.sim_cards.action_set_standby_response import ActionSetStandbyResponse
from ...types.sim_cards.action_set_public_ip_response import ActionSetPublicIPResponse
from ...types.sim_cards.action_remove_public_ip_response import ActionRemovePublicIPResponse
from ...types.sim_cards.action_bulk_set_public_ips_response import ActionBulkSetPublicIPsResponse
from ...types.sim_cards.action_validate_registration_codes_response import ActionValidateRegistrationCodesResponse

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
        This API fetches detailed information about a SIM card action to follow-up on an
        existing asynchronous operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_card_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: action_list_params.Filter | NotGiven = NOT_GIVEN,
        page: action_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """This API lists a paginated collection of SIM card actions.

        It enables exploring
        a collection of existing asynchronous operations using specific filters.

        Args:
          filter: Consolidated filter parameter for SIM card actions (deepObject style).
              Originally: filter[sim_card_id], filter[status],
              filter[bulk_sim_card_action_id], filter[action_type]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sim_card_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    def bulk_set_public_ips(
        self,
        *,
        sim_card_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionBulkSetPublicIPsResponse:
        """
        This API triggers an asynchronous operation to set a public IP for each of the
        specified SIM cards.<br/> For each SIM Card a SIM Card Action will be generated.
        The status of the SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sim_cards/actions/bulk_set_public_ips",
            body=maybe_transform(
                {"sim_card_ids": sim_card_ids}, action_bulk_set_public_ips_params.ActionBulkSetPublicIPsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionBulkSetPublicIPsResponse,
        )

    def disable(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableResponse:
        """
        This API disables a SIM card, disconnecting it from the network and making it
        impossible to consume data.<br/> The API will trigger an asynchronous operation
        called a SIM Card Action. Transitioning to the disabled state may take a period
        of time. The status of the SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_cards/{id}/actions/disable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisableResponse,
        )

    def enable(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableResponse:
        """
        This API enables a SIM card, connecting it to the network and making it possible
        to consume data.<br/> To enable a SIM card, it must be associated with a SIM
        card group.<br/> The API will trigger an asynchronous operation called a SIM
        Card Action. Transitioning to the enabled state may take a period of time. The
        status of the SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_cards/{id}/actions/enable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableResponse,
        )

    def remove_public_ip(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemovePublicIPResponse:
        """This API removes an existing public IP from a SIM card.

        <br/><br/> The API will
        trigger an asynchronous operation called a SIM Card Action. The status of the
        SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_cards/{id}/actions/remove_public_ip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemovePublicIPResponse,
        )

    def set_public_ip(
        self,
        id: str,
        *,
        region_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetPublicIPResponse:
        """
        This API makes a SIM card reachable on the public internet by mapping a random
        public IP to the SIM card. <br/><br/> The API will trigger an asynchronous
        operation called a SIM Card Action. The status of the SIM Card Action can be
        followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API. <br/><br/> Setting a Public IP to a SIM Card incurs a charge and will only
        succeed if the account has sufficient funds.

        Args:
          region_code: The code of the region where the public IP should be assigned. A list of
              available regions can be found at the regions endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_cards/{id}/actions/set_public_ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"region_code": region_code}, action_set_public_ip_params.ActionSetPublicIPParams
                ),
            ),
            cast_to=ActionSetPublicIPResponse,
        )

    def set_standby(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetStandbyResponse:
        """
        The SIM card will be able to connect to the network once the process to set it
        to standby has been completed, thus making it possible to consume data.<br/> To
        set a SIM card to standby, it must be associated with SIM card group.<br/> The
        API will trigger an asynchronous operation called a SIM Card Action.
        Transitioning to the standby state may take a period of time. The status of the
        SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sim_cards/{id}/actions/set_standby",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetStandbyResponse,
        )

    def validate_registration_codes(
        self,
        *,
        registration_codes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionValidateRegistrationCodesResponse:
        """
        It validates whether SIM card registration codes are valid or not.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sim_cards/actions/validate_registration_codes",
            body=maybe_transform(
                {"registration_codes": registration_codes},
                action_validate_registration_codes_params.ActionValidateRegistrationCodesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionValidateRegistrationCodesResponse,
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
        This API fetches detailed information about a SIM card action to follow-up on an
        existing asynchronous operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_card_actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: action_list_params.Filter | NotGiven = NOT_GIVEN,
        page: action_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """This API lists a paginated collection of SIM card actions.

        It enables exploring
        a collection of existing asynchronous operations using specific filters.

        Args:
          filter: Consolidated filter parameter for SIM card actions (deepObject style).
              Originally: filter[sim_card_id], filter[status],
              filter[bulk_sim_card_action_id], filter[action_type]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sim_card_actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    async def bulk_set_public_ips(
        self,
        *,
        sim_card_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionBulkSetPublicIPsResponse:
        """
        This API triggers an asynchronous operation to set a public IP for each of the
        specified SIM cards.<br/> For each SIM Card a SIM Card Action will be generated.
        The status of the SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sim_cards/actions/bulk_set_public_ips",
            body=await async_maybe_transform(
                {"sim_card_ids": sim_card_ids}, action_bulk_set_public_ips_params.ActionBulkSetPublicIPsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionBulkSetPublicIPsResponse,
        )

    async def disable(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableResponse:
        """
        This API disables a SIM card, disconnecting it from the network and making it
        impossible to consume data.<br/> The API will trigger an asynchronous operation
        called a SIM Card Action. Transitioning to the disabled state may take a period
        of time. The status of the SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_cards/{id}/actions/disable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisableResponse,
        )

    async def enable(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableResponse:
        """
        This API enables a SIM card, connecting it to the network and making it possible
        to consume data.<br/> To enable a SIM card, it must be associated with a SIM
        card group.<br/> The API will trigger an asynchronous operation called a SIM
        Card Action. Transitioning to the enabled state may take a period of time. The
        status of the SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_cards/{id}/actions/enable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableResponse,
        )

    async def remove_public_ip(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemovePublicIPResponse:
        """This API removes an existing public IP from a SIM card.

        <br/><br/> The API will
        trigger an asynchronous operation called a SIM Card Action. The status of the
        SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_cards/{id}/actions/remove_public_ip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemovePublicIPResponse,
        )

    async def set_public_ip(
        self,
        id: str,
        *,
        region_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetPublicIPResponse:
        """
        This API makes a SIM card reachable on the public internet by mapping a random
        public IP to the SIM card. <br/><br/> The API will trigger an asynchronous
        operation called a SIM Card Action. The status of the SIM Card Action can be
        followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API. <br/><br/> Setting a Public IP to a SIM Card incurs a charge and will only
        succeed if the account has sufficient funds.

        Args:
          region_code: The code of the region where the public IP should be assigned. A list of
              available regions can be found at the regions endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_cards/{id}/actions/set_public_ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"region_code": region_code}, action_set_public_ip_params.ActionSetPublicIPParams
                ),
            ),
            cast_to=ActionSetPublicIPResponse,
        )

    async def set_standby(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetStandbyResponse:
        """
        The SIM card will be able to connect to the network once the process to set it
        to standby has been completed, thus making it possible to consume data.<br/> To
        set a SIM card to standby, it must be associated with SIM card group.<br/> The
        API will trigger an asynchronous operation called a SIM Card Action.
        Transitioning to the standby state may take a period of time. The status of the
        SIM Card Action can be followed through the
        [List SIM Card Action](https://developersdev.telnyx.com/docs/api/v2/wireless/SIM-Card-Actions#ListSIMCardActions)
        API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sim_cards/{id}/actions/set_standby",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetStandbyResponse,
        )

    async def validate_registration_codes(
        self,
        *,
        registration_codes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionValidateRegistrationCodesResponse:
        """
        It validates whether SIM card registration codes are valid or not.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sim_cards/actions/validate_registration_codes",
            body=await async_maybe_transform(
                {"registration_codes": registration_codes},
                action_validate_registration_codes_params.ActionValidateRegistrationCodesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionValidateRegistrationCodesResponse,
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
        self.bulk_set_public_ips = to_raw_response_wrapper(
            actions.bulk_set_public_ips,
        )
        self.disable = to_raw_response_wrapper(
            actions.disable,
        )
        self.enable = to_raw_response_wrapper(
            actions.enable,
        )
        self.remove_public_ip = to_raw_response_wrapper(
            actions.remove_public_ip,
        )
        self.set_public_ip = to_raw_response_wrapper(
            actions.set_public_ip,
        )
        self.set_standby = to_raw_response_wrapper(
            actions.set_standby,
        )
        self.validate_registration_codes = to_raw_response_wrapper(
            actions.validate_registration_codes,
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
        self.bulk_set_public_ips = async_to_raw_response_wrapper(
            actions.bulk_set_public_ips,
        )
        self.disable = async_to_raw_response_wrapper(
            actions.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            actions.enable,
        )
        self.remove_public_ip = async_to_raw_response_wrapper(
            actions.remove_public_ip,
        )
        self.set_public_ip = async_to_raw_response_wrapper(
            actions.set_public_ip,
        )
        self.set_standby = async_to_raw_response_wrapper(
            actions.set_standby,
        )
        self.validate_registration_codes = async_to_raw_response_wrapper(
            actions.validate_registration_codes,
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
        self.bulk_set_public_ips = to_streamed_response_wrapper(
            actions.bulk_set_public_ips,
        )
        self.disable = to_streamed_response_wrapper(
            actions.disable,
        )
        self.enable = to_streamed_response_wrapper(
            actions.enable,
        )
        self.remove_public_ip = to_streamed_response_wrapper(
            actions.remove_public_ip,
        )
        self.set_public_ip = to_streamed_response_wrapper(
            actions.set_public_ip,
        )
        self.set_standby = to_streamed_response_wrapper(
            actions.set_standby,
        )
        self.validate_registration_codes = to_streamed_response_wrapper(
            actions.validate_registration_codes,
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
        self.bulk_set_public_ips = async_to_streamed_response_wrapper(
            actions.bulk_set_public_ips,
        )
        self.disable = async_to_streamed_response_wrapper(
            actions.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            actions.enable,
        )
        self.remove_public_ip = async_to_streamed_response_wrapper(
            actions.remove_public_ip,
        )
        self.set_public_ip = async_to_streamed_response_wrapper(
            actions.set_public_ip,
        )
        self.set_standby = async_to_streamed_response_wrapper(
            actions.set_standby,
        )
        self.validate_registration_codes = async_to_streamed_response_wrapper(
            actions.validate_registration_codes,
        )
