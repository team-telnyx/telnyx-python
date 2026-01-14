# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    managed_account_list_params,
    managed_account_create_params,
    managed_account_update_params,
    managed_account_update_global_channel_limit_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.managed_account_list_response import ManagedAccountListResponse
from ...types.managed_account_create_response import ManagedAccountCreateResponse
from ...types.managed_account_update_response import ManagedAccountUpdateResponse
from ...types.managed_account_retrieve_response import ManagedAccountRetrieveResponse
from ...types.managed_account_update_global_channel_limit_response import ManagedAccountUpdateGlobalChannelLimitResponse
from ...types.managed_account_get_allocatable_global_outbound_channels_response import (
    ManagedAccountGetAllocatableGlobalOutboundChannelsResponse,
)

__all__ = ["ManagedAccountsResource", "AsyncManagedAccountsResource"]


class ManagedAccountsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ManagedAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ManagedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagedAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ManagedAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_name: str,
        email: str | Omit = omit,
        managed_account_allow_custom_pricing: bool | Omit = omit,
        password: str | Omit = omit,
        rollup_billing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountCreateResponse:
        """Create a new managed account owned by the authenticated user.

        You need to be
        explictly approved by Telnyx in order to become a manager account.

        Args:
          business_name: The name of the business for which the new managed account is being created,
              that will be used as the managed accounts's organization's name.

          email: The email address for the managed account. If not provided, the email address
              will be generated based on the email address of the manager account.

          managed_account_allow_custom_pricing: Boolean value that indicates if the managed account is able to have custom
              pricing set for it or not. If false, uses the pricing of the manager account.
              Defaults to false. This value may be changed after creation, but there may be
              time lag between when the value is changed and pricing changes take effect.

          password: Password for the managed account. If a password is not supplied, the account
              will not be able to be signed into directly. (A password reset may still be
              performed later to enable sign-in via password.)

          rollup_billing: Boolean value that indicates if the billing information and charges to the
              managed account "roll up" to the manager account. If true, the managed account
              will not have its own balance and will use the shared balance with the manager
              account. This value cannot be changed after account creation without going
              through Telnyx support as changes require manual updates to the account ledger.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/managed_accounts",
            body=maybe_transform(
                {
                    "business_name": business_name,
                    "email": email,
                    "managed_account_allow_custom_pricing": managed_account_allow_custom_pricing,
                    "password": password,
                    "rollup_billing": rollup_billing,
                },
                managed_account_create_params.ManagedAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountCreateResponse,
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
    ) -> ManagedAccountRetrieveResponse:
        """
        Retrieves the details of a single managed account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/managed_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        managed_account_allow_custom_pricing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountUpdateResponse:
        """
        Update a single managed account.

        Args:
          managed_account_allow_custom_pricing: Boolean value that indicates if the managed account is able to have custom
              pricing set for it or not. If false, uses the pricing of the manager account.
              Defaults to false. This value may be changed, but there may be time lag between
              when the value is changed and pricing changes take effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/managed_accounts/{id}",
            body=maybe_transform(
                {"managed_account_allow_custom_pricing": managed_account_allow_custom_pricing},
                managed_account_update_params.ManagedAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountUpdateResponse,
        )

    def list(
        self,
        *,
        filter: managed_account_list_params.Filter | Omit = omit,
        include_cancelled_accounts: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "email"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ManagedAccountListResponse]:
        """Lists the accounts managed by the current user.

        Users need to be explictly
        approved by Telnyx in order to become manager accounts.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[email][contains], filter[email][eq], filter[organization_name][contains],
              filter[organization_name][eq]

          include_cancelled_accounts: Specifies if cancelled accounts should be included in the results.

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>email</code>: sorts the result by the
                  <code>email</code> field in ascending order.
                </li>

                <li>
                  <code>-email</code>: sorts the result by the
                  <code>email</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/managed_accounts",
            page=SyncDefaultFlatPagination[ManagedAccountListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_cancelled_accounts": include_cancelled_accounts,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    managed_account_list_params.ManagedAccountListParams,
                ),
            ),
            model=ManagedAccountListResponse,
        )

    def get_allocatable_global_outbound_channels(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountGetAllocatableGlobalOutboundChannelsResponse:
        """
        Display information about allocatable global outbound channels for the current
        user. Only usable by account managers.
        """
        return self._get(
            "/managed_accounts/allocatable_global_outbound_channels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountGetAllocatableGlobalOutboundChannelsResponse,
        )

    def update_global_channel_limit(
        self,
        id: str,
        *,
        channel_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountUpdateGlobalChannelLimitResponse:
        """
        Update the amount of allocatable global outbound channels allocated to a
        specific managed account.

        Args:
          channel_limit: Integer value that indicates the number of allocatable global outbound channels
              that should be allocated to the managed account. Must be 0 or more. If the value
              is 0 then the account will have no usable channels and will not be able to
              perform outbound calling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/managed_accounts/{id}/update_global_channel_limit",
            body=maybe_transform(
                {"channel_limit": channel_limit},
                managed_account_update_global_channel_limit_params.ManagedAccountUpdateGlobalChannelLimitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountUpdateGlobalChannelLimitResponse,
        )


class AsyncManagedAccountsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncManagedAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManagedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagedAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncManagedAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_name: str,
        email: str | Omit = omit,
        managed_account_allow_custom_pricing: bool | Omit = omit,
        password: str | Omit = omit,
        rollup_billing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountCreateResponse:
        """Create a new managed account owned by the authenticated user.

        You need to be
        explictly approved by Telnyx in order to become a manager account.

        Args:
          business_name: The name of the business for which the new managed account is being created,
              that will be used as the managed accounts's organization's name.

          email: The email address for the managed account. If not provided, the email address
              will be generated based on the email address of the manager account.

          managed_account_allow_custom_pricing: Boolean value that indicates if the managed account is able to have custom
              pricing set for it or not. If false, uses the pricing of the manager account.
              Defaults to false. This value may be changed after creation, but there may be
              time lag between when the value is changed and pricing changes take effect.

          password: Password for the managed account. If a password is not supplied, the account
              will not be able to be signed into directly. (A password reset may still be
              performed later to enable sign-in via password.)

          rollup_billing: Boolean value that indicates if the billing information and charges to the
              managed account "roll up" to the manager account. If true, the managed account
              will not have its own balance and will use the shared balance with the manager
              account. This value cannot be changed after account creation without going
              through Telnyx support as changes require manual updates to the account ledger.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/managed_accounts",
            body=await async_maybe_transform(
                {
                    "business_name": business_name,
                    "email": email,
                    "managed_account_allow_custom_pricing": managed_account_allow_custom_pricing,
                    "password": password,
                    "rollup_billing": rollup_billing,
                },
                managed_account_create_params.ManagedAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountCreateResponse,
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
    ) -> ManagedAccountRetrieveResponse:
        """
        Retrieves the details of a single managed account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/managed_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        managed_account_allow_custom_pricing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountUpdateResponse:
        """
        Update a single managed account.

        Args:
          managed_account_allow_custom_pricing: Boolean value that indicates if the managed account is able to have custom
              pricing set for it or not. If false, uses the pricing of the manager account.
              Defaults to false. This value may be changed, but there may be time lag between
              when the value is changed and pricing changes take effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/managed_accounts/{id}",
            body=await async_maybe_transform(
                {"managed_account_allow_custom_pricing": managed_account_allow_custom_pricing},
                managed_account_update_params.ManagedAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountUpdateResponse,
        )

    def list(
        self,
        *,
        filter: managed_account_list_params.Filter | Omit = omit,
        include_cancelled_accounts: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "email"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ManagedAccountListResponse, AsyncDefaultFlatPagination[ManagedAccountListResponse]]:
        """Lists the accounts managed by the current user.

        Users need to be explictly
        approved by Telnyx in order to become manager accounts.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[email][contains], filter[email][eq], filter[organization_name][contains],
              filter[organization_name][eq]

          include_cancelled_accounts: Specifies if cancelled accounts should be included in the results.

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>email</code>: sorts the result by the
                  <code>email</code> field in ascending order.
                </li>

                <li>
                  <code>-email</code>: sorts the result by the
                  <code>email</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/managed_accounts",
            page=AsyncDefaultFlatPagination[ManagedAccountListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_cancelled_accounts": include_cancelled_accounts,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    managed_account_list_params.ManagedAccountListParams,
                ),
            ),
            model=ManagedAccountListResponse,
        )

    async def get_allocatable_global_outbound_channels(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountGetAllocatableGlobalOutboundChannelsResponse:
        """
        Display information about allocatable global outbound channels for the current
        user. Only usable by account managers.
        """
        return await self._get(
            "/managed_accounts/allocatable_global_outbound_channels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountGetAllocatableGlobalOutboundChannelsResponse,
        )

    async def update_global_channel_limit(
        self,
        id: str,
        *,
        channel_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedAccountUpdateGlobalChannelLimitResponse:
        """
        Update the amount of allocatable global outbound channels allocated to a
        specific managed account.

        Args:
          channel_limit: Integer value that indicates the number of allocatable global outbound channels
              that should be allocated to the managed account. Must be 0 or more. If the value
              is 0 then the account will have no usable channels and will not be able to
              perform outbound calling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/managed_accounts/{id}/update_global_channel_limit",
            body=await async_maybe_transform(
                {"channel_limit": channel_limit},
                managed_account_update_global_channel_limit_params.ManagedAccountUpdateGlobalChannelLimitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedAccountUpdateGlobalChannelLimitResponse,
        )


class ManagedAccountsResourceWithRawResponse:
    def __init__(self, managed_accounts: ManagedAccountsResource) -> None:
        self._managed_accounts = managed_accounts

        self.create = to_raw_response_wrapper(
            managed_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            managed_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            managed_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            managed_accounts.list,
        )
        self.get_allocatable_global_outbound_channels = to_raw_response_wrapper(
            managed_accounts.get_allocatable_global_outbound_channels,
        )
        self.update_global_channel_limit = to_raw_response_wrapper(
            managed_accounts.update_global_channel_limit,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._managed_accounts.actions)


class AsyncManagedAccountsResourceWithRawResponse:
    def __init__(self, managed_accounts: AsyncManagedAccountsResource) -> None:
        self._managed_accounts = managed_accounts

        self.create = async_to_raw_response_wrapper(
            managed_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            managed_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            managed_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            managed_accounts.list,
        )
        self.get_allocatable_global_outbound_channels = async_to_raw_response_wrapper(
            managed_accounts.get_allocatable_global_outbound_channels,
        )
        self.update_global_channel_limit = async_to_raw_response_wrapper(
            managed_accounts.update_global_channel_limit,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._managed_accounts.actions)


class ManagedAccountsResourceWithStreamingResponse:
    def __init__(self, managed_accounts: ManagedAccountsResource) -> None:
        self._managed_accounts = managed_accounts

        self.create = to_streamed_response_wrapper(
            managed_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            managed_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            managed_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            managed_accounts.list,
        )
        self.get_allocatable_global_outbound_channels = to_streamed_response_wrapper(
            managed_accounts.get_allocatable_global_outbound_channels,
        )
        self.update_global_channel_limit = to_streamed_response_wrapper(
            managed_accounts.update_global_channel_limit,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._managed_accounts.actions)


class AsyncManagedAccountsResourceWithStreamingResponse:
    def __init__(self, managed_accounts: AsyncManagedAccountsResource) -> None:
        self._managed_accounts = managed_accounts

        self.create = async_to_streamed_response_wrapper(
            managed_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            managed_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            managed_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            managed_accounts.list,
        )
        self.get_allocatable_global_outbound_channels = async_to_streamed_response_wrapper(
            managed_accounts.get_allocatable_global_outbound_channels,
        )
        self.update_global_channel_limit = async_to_streamed_response_wrapper(
            managed_accounts.update_global_channel_limit,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._managed_accounts.actions)
