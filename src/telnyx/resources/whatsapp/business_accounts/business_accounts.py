# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .phone_numbers import (
    PhoneNumbersResource,
    AsyncPhoneNumbersResource,
    PhoneNumbersResourceWithRawResponse,
    AsyncPhoneNumbersResourceWithRawResponse,
    PhoneNumbersResourceWithStreamingResponse,
    AsyncPhoneNumbersResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.whatsapp import business_account_list_params
from ....types.whatsapp.business_account_list_response import BusinessAccountListResponse
from ....types.whatsapp.business_account_retrieve_response import BusinessAccountRetrieveResponse

__all__ = ["BusinessAccountsResource", "AsyncBusinessAccountsResource"]


class BusinessAccountsResource(SyncAPIResource):
    """Manage Whatsapp business accounts"""

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        return PhoneNumbersResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        """Manage Whatsapp business accounts"""
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BusinessAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BusinessAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BusinessAccountsResourceWithStreamingResponse(self)

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
    ) -> BusinessAccountRetrieveResponse:
        """
        Get a single Whatsapp Business Account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v2/whatsapp/business_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessAccountRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[BusinessAccountListResponse]:
        """
        List Whatsapp Business Accounts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/whatsapp/business_accounts",
            page=SyncDefaultFlatPagination[BusinessAccountListResponse],
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
                    business_account_list_params.BusinessAccountListParams,
                ),
            ),
            model=BusinessAccountListResponse,
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
    ) -> None:
        """
        Delete a Whatsapp Business Account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/whatsapp/business_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBusinessAccountsResource(AsyncAPIResource):
    """Manage Whatsapp business accounts"""

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """Manage Whatsapp business accounts"""
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBusinessAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBusinessAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBusinessAccountsResourceWithStreamingResponse(self)

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
    ) -> BusinessAccountRetrieveResponse:
        """
        Get a single Whatsapp Business Account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v2/whatsapp/business_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessAccountRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BusinessAccountListResponse, AsyncDefaultFlatPagination[BusinessAccountListResponse]]:
        """
        List Whatsapp Business Accounts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/whatsapp/business_accounts",
            page=AsyncDefaultFlatPagination[BusinessAccountListResponse],
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
                    business_account_list_params.BusinessAccountListParams,
                ),
            ),
            model=BusinessAccountListResponse,
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
    ) -> None:
        """
        Delete a Whatsapp Business Account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/whatsapp/business_accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BusinessAccountsResourceWithRawResponse:
    def __init__(self, business_accounts: BusinessAccountsResource) -> None:
        self._business_accounts = business_accounts

        self.retrieve = to_raw_response_wrapper(
            business_accounts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            business_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            business_accounts.delete,
        )

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        return PhoneNumbersResourceWithRawResponse(self._business_accounts.phone_numbers)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """Manage Whatsapp business accounts"""
        return SettingsResourceWithRawResponse(self._business_accounts.settings)


class AsyncBusinessAccountsResourceWithRawResponse:
    def __init__(self, business_accounts: AsyncBusinessAccountsResource) -> None:
        self._business_accounts = business_accounts

        self.retrieve = async_to_raw_response_wrapper(
            business_accounts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            business_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            business_accounts.delete,
        )

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        return AsyncPhoneNumbersResourceWithRawResponse(self._business_accounts.phone_numbers)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """Manage Whatsapp business accounts"""
        return AsyncSettingsResourceWithRawResponse(self._business_accounts.settings)


class BusinessAccountsResourceWithStreamingResponse:
    def __init__(self, business_accounts: BusinessAccountsResource) -> None:
        self._business_accounts = business_accounts

        self.retrieve = to_streamed_response_wrapper(
            business_accounts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            business_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            business_accounts.delete,
        )

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        return PhoneNumbersResourceWithStreamingResponse(self._business_accounts.phone_numbers)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """Manage Whatsapp business accounts"""
        return SettingsResourceWithStreamingResponse(self._business_accounts.settings)


class AsyncBusinessAccountsResourceWithStreamingResponse:
    def __init__(self, business_accounts: AsyncBusinessAccountsResource) -> None:
        self._business_accounts = business_accounts

        self.retrieve = async_to_streamed_response_wrapper(
            business_accounts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            business_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            business_accounts.delete,
        )

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._business_accounts.phone_numbers)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """Manage Whatsapp business accounts"""
        return AsyncSettingsResourceWithStreamingResponse(self._business_accounts.settings)
