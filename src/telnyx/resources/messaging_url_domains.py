# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import messaging_url_domain_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.messaging_url_domain_list_response import MessagingURLDomainListResponse

__all__ = ["MessagingURLDomainsResource", "AsyncMessagingURLDomainsResource"]


class MessagingURLDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingURLDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingURLDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingURLDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingURLDomainsResourceWithStreamingResponse(self)

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
    ) -> SyncDefaultFlatPagination[MessagingURLDomainListResponse]:
        """
        List messaging URL domains

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_url_domains",
            page=SyncDefaultFlatPagination[MessagingURLDomainListResponse],
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
                    messaging_url_domain_list_params.MessagingURLDomainListParams,
                ),
            ),
            model=MessagingURLDomainListResponse,
        )


class AsyncMessagingURLDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingURLDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingURLDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingURLDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingURLDomainsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[MessagingURLDomainListResponse, AsyncDefaultFlatPagination[MessagingURLDomainListResponse]]:
        """
        List messaging URL domains

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_url_domains",
            page=AsyncDefaultFlatPagination[MessagingURLDomainListResponse],
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
                    messaging_url_domain_list_params.MessagingURLDomainListParams,
                ),
            ),
            model=MessagingURLDomainListResponse,
        )


class MessagingURLDomainsResourceWithRawResponse:
    def __init__(self, messaging_url_domains: MessagingURLDomainsResource) -> None:
        self._messaging_url_domains = messaging_url_domains

        self.list = to_raw_response_wrapper(
            messaging_url_domains.list,
        )


class AsyncMessagingURLDomainsResourceWithRawResponse:
    def __init__(self, messaging_url_domains: AsyncMessagingURLDomainsResource) -> None:
        self._messaging_url_domains = messaging_url_domains

        self.list = async_to_raw_response_wrapper(
            messaging_url_domains.list,
        )


class MessagingURLDomainsResourceWithStreamingResponse:
    def __init__(self, messaging_url_domains: MessagingURLDomainsResource) -> None:
        self._messaging_url_domains = messaging_url_domains

        self.list = to_streamed_response_wrapper(
            messaging_url_domains.list,
        )


class AsyncMessagingURLDomainsResourceWithStreamingResponse:
    def __init__(self, messaging_url_domains: AsyncMessagingURLDomainsResource) -> None:
        self._messaging_url_domains = messaging_url_domains

        self.list = async_to_streamed_response_wrapper(
            messaging_url_domains.list,
        )
