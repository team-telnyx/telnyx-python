# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...types import (
    sim_card_list_params,
    sim_card_delete_params,
    sim_card_update_params,
    sim_card_retrieve_params,
    sim_card_list_wireless_connectivity_logs_params,
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
from ...types.sim_card_list_response import SimCardListResponse
from ...types.sim_card_delete_response import SimCardDeleteResponse
from ...types.sim_card_update_response import SimCardUpdateResponse
from ...types.sim_card_retrieve_response import SimCardRetrieveResponse
from ...types.shared_params.sim_card_status import SimCardStatus
from ...types.sim_card_get_public_ip_response import SimCardGetPublicIPResponse
from ...types.sim_card_get_device_details_response import SimCardGetDeviceDetailsResponse
from ...types.sim_card_get_activation_code_response import SimCardGetActivationCodeResponse
from ...types.sim_card_list_wireless_connectivity_logs_response import SimCardListWirelessConnectivityLogsResponse

__all__ = ["SimCardsResource", "AsyncSimCardsResource"]


class SimCardsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SimCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SimCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SimCardsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        include_pin_puk_codes: bool | NotGiven = NOT_GIVEN,
        include_sim_card_group: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardRetrieveResponse:
        """
        Returns the details regarding a specific SIM card.

        Args:
          include_pin_puk_codes: When set to true, includes the PIN and PUK codes in the response. These codes
              are used for SIM card security and unlocking purposes. Available for both
              physical SIM cards and eSIMs.

          include_sim_card_group: It includes the associated SIM card group object in the response when present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_cards/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_pin_puk_codes": include_pin_puk_codes,
                        "include_sim_card_group": include_sim_card_group,
                    },
                    sim_card_retrieve_params.SimCardRetrieveParams,
                ),
            ),
            cast_to=SimCardRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        authorized_imeis: List[str] | NotGiven = NOT_GIVEN,
        data_limit: sim_card_update_params.DataLimit | NotGiven = NOT_GIVEN,
        sim_card_group_id: str | NotGiven = NOT_GIVEN,
        status: SimCardStatus | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardUpdateResponse:
        """
        Updates SIM card data

        Args:
          authorized_imeis: List of IMEIs authorized to use a given SIM card.

          data_limit: The SIM card individual data limit configuration.

          sim_card_group_id: The group SIMCardGroup identification. This attribute can be <code>null</code>
              when it's present in an associated resource.

          tags: Searchable tags associated with the SIM card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/sim_cards/{id}",
            body=maybe_transform(
                {
                    "authorized_imeis": authorized_imeis,
                    "data_limit": data_limit,
                    "sim_card_group_id": sim_card_group_id,
                    "status": status,
                    "tags": tags,
                },
                sim_card_update_params.SimCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardUpdateResponse,
        )

    def list(
        self,
        *,
        filter: sim_card_list_params.Filter | NotGiven = NOT_GIVEN,
        filter_sim_card_group_id: str | NotGiven = NOT_GIVEN,
        include_sim_card_group: bool | NotGiven = NOT_GIVEN,
        page: sim_card_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["current_billing_period_consumed_data.amount"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardListResponse:
        """
        Get all SIM cards belonging to the user that match the given filters.

        Args:
          filter:
              Consolidated filter parameter for SIM cards (deepObject style). Originally:
              filter[tags], filter[iccid], filter[status]

          filter_sim_card_group_id: A valid SIM card group ID.

          include_sim_card_group: It includes the associated SIM card group object in the response when present.

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Sorts SIM cards by the given field. Defaults to ascending order unless field is
              prefixed with a minus sign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sim_cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "filter_sim_card_group_id": filter_sim_card_group_id,
                        "include_sim_card_group": include_sim_card_group,
                        "page": page,
                        "sort": sort,
                    },
                    sim_card_list_params.SimCardListParams,
                ),
            ),
            cast_to=SimCardListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        report_lost: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDeleteResponse:
        """
        The SIM card will be decommissioned, removed from your account and you will stop
        being charged.<br />The SIM card won't be able to connect to the network after
        the deletion is completed, thus making it impossible to consume data.<br/>
        Transitioning to the disabled state may take a period of time. Until the
        transition is completed, the SIM card status will be disabling
        <code>disabling</code>.<br />In order to re-enable the SIM card, you will need
        to re-register it.

        Args:
          report_lost: Enables deletion of disabled eSIMs that can't be uninstalled from a device. This
              is irreversible and the eSIM cannot be re-registered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/sim_cards/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"report_lost": report_lost}, sim_card_delete_params.SimCardDeleteParams),
            ),
            cast_to=SimCardDeleteResponse,
        )

    def get_activation_code(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGetActivationCodeResponse:
        """
        It returns the activation code for an eSIM.<br/><br/> This API is only available
        for eSIMs. If the given SIM is a physical SIM card, or has already been
        installed, an error will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_cards/{id}/activation_code",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGetActivationCodeResponse,
        )

    def get_device_details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGetDeviceDetailsResponse:
        """
        It returns the device details where a SIM card is currently being used.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_cards/{id}/device_details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGetDeviceDetailsResponse,
        )

    def get_public_ip(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGetPublicIPResponse:
        """
        It returns the public IP requested for a SIM card.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_cards/{id}/public_ip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGetPublicIPResponse,
        )

    def list_wireless_connectivity_logs(
        self,
        id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardListWirelessConnectivityLogsResponse:
        """
        This API allows listing a paginated collection of Wireless Connectivity Logs
        associated with a SIM Card, for troubleshooting purposes.

        Args:
          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_cards/{id}/wireless_connectivity_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    sim_card_list_wireless_connectivity_logs_params.SimCardListWirelessConnectivityLogsParams,
                ),
            ),
            cast_to=SimCardListWirelessConnectivityLogsResponse,
        )


class AsyncSimCardsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSimCardsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        include_pin_puk_codes: bool | NotGiven = NOT_GIVEN,
        include_sim_card_group: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardRetrieveResponse:
        """
        Returns the details regarding a specific SIM card.

        Args:
          include_pin_puk_codes: When set to true, includes the PIN and PUK codes in the response. These codes
              are used for SIM card security and unlocking purposes. Available for both
              physical SIM cards and eSIMs.

          include_sim_card_group: It includes the associated SIM card group object in the response when present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_cards/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_pin_puk_codes": include_pin_puk_codes,
                        "include_sim_card_group": include_sim_card_group,
                    },
                    sim_card_retrieve_params.SimCardRetrieveParams,
                ),
            ),
            cast_to=SimCardRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        authorized_imeis: List[str] | NotGiven = NOT_GIVEN,
        data_limit: sim_card_update_params.DataLimit | NotGiven = NOT_GIVEN,
        sim_card_group_id: str | NotGiven = NOT_GIVEN,
        status: SimCardStatus | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardUpdateResponse:
        """
        Updates SIM card data

        Args:
          authorized_imeis: List of IMEIs authorized to use a given SIM card.

          data_limit: The SIM card individual data limit configuration.

          sim_card_group_id: The group SIMCardGroup identification. This attribute can be <code>null</code>
              when it's present in an associated resource.

          tags: Searchable tags associated with the SIM card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/sim_cards/{id}",
            body=await async_maybe_transform(
                {
                    "authorized_imeis": authorized_imeis,
                    "data_limit": data_limit,
                    "sim_card_group_id": sim_card_group_id,
                    "status": status,
                    "tags": tags,
                },
                sim_card_update_params.SimCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: sim_card_list_params.Filter | NotGiven = NOT_GIVEN,
        filter_sim_card_group_id: str | NotGiven = NOT_GIVEN,
        include_sim_card_group: bool | NotGiven = NOT_GIVEN,
        page: sim_card_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["current_billing_period_consumed_data.amount"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardListResponse:
        """
        Get all SIM cards belonging to the user that match the given filters.

        Args:
          filter:
              Consolidated filter parameter for SIM cards (deepObject style). Originally:
              filter[tags], filter[iccid], filter[status]

          filter_sim_card_group_id: A valid SIM card group ID.

          include_sim_card_group: It includes the associated SIM card group object in the response when present.

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Sorts SIM cards by the given field. Defaults to ascending order unless field is
              prefixed with a minus sign.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sim_cards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "filter_sim_card_group_id": filter_sim_card_group_id,
                        "include_sim_card_group": include_sim_card_group,
                        "page": page,
                        "sort": sort,
                    },
                    sim_card_list_params.SimCardListParams,
                ),
            ),
            cast_to=SimCardListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        report_lost: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDeleteResponse:
        """
        The SIM card will be decommissioned, removed from your account and you will stop
        being charged.<br />The SIM card won't be able to connect to the network after
        the deletion is completed, thus making it impossible to consume data.<br/>
        Transitioning to the disabled state may take a period of time. Until the
        transition is completed, the SIM card status will be disabling
        <code>disabling</code>.<br />In order to re-enable the SIM card, you will need
        to re-register it.

        Args:
          report_lost: Enables deletion of disabled eSIMs that can't be uninstalled from a device. This
              is irreversible and the eSIM cannot be re-registered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/sim_cards/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"report_lost": report_lost}, sim_card_delete_params.SimCardDeleteParams
                ),
            ),
            cast_to=SimCardDeleteResponse,
        )

    async def get_activation_code(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGetActivationCodeResponse:
        """
        It returns the activation code for an eSIM.<br/><br/> This API is only available
        for eSIMs. If the given SIM is a physical SIM card, or has already been
        installed, an error will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_cards/{id}/activation_code",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGetActivationCodeResponse,
        )

    async def get_device_details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGetDeviceDetailsResponse:
        """
        It returns the device details where a SIM card is currently being used.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_cards/{id}/device_details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGetDeviceDetailsResponse,
        )

    async def get_public_ip(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardGetPublicIPResponse:
        """
        It returns the public IP requested for a SIM card.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_cards/{id}/public_ip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardGetPublicIPResponse,
        )

    async def list_wireless_connectivity_logs(
        self,
        id: str,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardListWirelessConnectivityLogsResponse:
        """
        This API allows listing a paginated collection of Wireless Connectivity Logs
        associated with a SIM Card, for troubleshooting purposes.

        Args:
          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_cards/{id}/wireless_connectivity_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    sim_card_list_wireless_connectivity_logs_params.SimCardListWirelessConnectivityLogsParams,
                ),
            ),
            cast_to=SimCardListWirelessConnectivityLogsResponse,
        )


class SimCardsResourceWithRawResponse:
    def __init__(self, sim_cards: SimCardsResource) -> None:
        self._sim_cards = sim_cards

        self.retrieve = to_raw_response_wrapper(
            sim_cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sim_cards.update,
        )
        self.list = to_raw_response_wrapper(
            sim_cards.list,
        )
        self.delete = to_raw_response_wrapper(
            sim_cards.delete,
        )
        self.get_activation_code = to_raw_response_wrapper(
            sim_cards.get_activation_code,
        )
        self.get_device_details = to_raw_response_wrapper(
            sim_cards.get_device_details,
        )
        self.get_public_ip = to_raw_response_wrapper(
            sim_cards.get_public_ip,
        )
        self.list_wireless_connectivity_logs = to_raw_response_wrapper(
            sim_cards.list_wireless_connectivity_logs,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._sim_cards.actions)


class AsyncSimCardsResourceWithRawResponse:
    def __init__(self, sim_cards: AsyncSimCardsResource) -> None:
        self._sim_cards = sim_cards

        self.retrieve = async_to_raw_response_wrapper(
            sim_cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sim_cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            sim_cards.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sim_cards.delete,
        )
        self.get_activation_code = async_to_raw_response_wrapper(
            sim_cards.get_activation_code,
        )
        self.get_device_details = async_to_raw_response_wrapper(
            sim_cards.get_device_details,
        )
        self.get_public_ip = async_to_raw_response_wrapper(
            sim_cards.get_public_ip,
        )
        self.list_wireless_connectivity_logs = async_to_raw_response_wrapper(
            sim_cards.list_wireless_connectivity_logs,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._sim_cards.actions)


class SimCardsResourceWithStreamingResponse:
    def __init__(self, sim_cards: SimCardsResource) -> None:
        self._sim_cards = sim_cards

        self.retrieve = to_streamed_response_wrapper(
            sim_cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sim_cards.update,
        )
        self.list = to_streamed_response_wrapper(
            sim_cards.list,
        )
        self.delete = to_streamed_response_wrapper(
            sim_cards.delete,
        )
        self.get_activation_code = to_streamed_response_wrapper(
            sim_cards.get_activation_code,
        )
        self.get_device_details = to_streamed_response_wrapper(
            sim_cards.get_device_details,
        )
        self.get_public_ip = to_streamed_response_wrapper(
            sim_cards.get_public_ip,
        )
        self.list_wireless_connectivity_logs = to_streamed_response_wrapper(
            sim_cards.list_wireless_connectivity_logs,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._sim_cards.actions)


class AsyncSimCardsResourceWithStreamingResponse:
    def __init__(self, sim_cards: AsyncSimCardsResource) -> None:
        self._sim_cards = sim_cards

        self.retrieve = async_to_streamed_response_wrapper(
            sim_cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sim_cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sim_cards.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sim_cards.delete,
        )
        self.get_activation_code = async_to_streamed_response_wrapper(
            sim_cards.get_activation_code,
        )
        self.get_device_details = async_to_streamed_response_wrapper(
            sim_cards.get_device_details,
        )
        self.get_public_ip = async_to_streamed_response_wrapper(
            sim_cards.get_public_ip,
        )
        self.list_wireless_connectivity_logs = async_to_streamed_response_wrapper(
            sim_cards.list_wireless_connectivity_logs,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._sim_cards.actions)
