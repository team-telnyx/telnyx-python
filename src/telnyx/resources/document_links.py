# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import document_link_list_params
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
from ..types.document_link_list_response import DocumentLinkListResponse

__all__ = ["DocumentLinksResource", "AsyncDocumentLinksResource"]


class DocumentLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DocumentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DocumentLinksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: document_link_list_params.Filter | NotGiven = NOT_GIVEN,
        page: document_link_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentLinkListResponse:
        """
        List all documents links ordered by created_at descending.

        Args:
          filter:
              Consolidated filter parameter for document links (deepObject style). Originally:
              filter[linked_record_type], filter[linked_resource_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/document_links",
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
                    document_link_list_params.DocumentLinkListParams,
                ),
            ),
            cast_to=DocumentLinkListResponse,
        )


class AsyncDocumentLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDocumentLinksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: document_link_list_params.Filter | NotGiven = NOT_GIVEN,
        page: document_link_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentLinkListResponse:
        """
        List all documents links ordered by created_at descending.

        Args:
          filter:
              Consolidated filter parameter for document links (deepObject style). Originally:
              filter[linked_record_type], filter[linked_resource_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/document_links",
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
                    document_link_list_params.DocumentLinkListParams,
                ),
            ),
            cast_to=DocumentLinkListResponse,
        )


class DocumentLinksResourceWithRawResponse:
    def __init__(self, document_links: DocumentLinksResource) -> None:
        self._document_links = document_links

        self.list = to_raw_response_wrapper(
            document_links.list,
        )


class AsyncDocumentLinksResourceWithRawResponse:
    def __init__(self, document_links: AsyncDocumentLinksResource) -> None:
        self._document_links = document_links

        self.list = async_to_raw_response_wrapper(
            document_links.list,
        )


class DocumentLinksResourceWithStreamingResponse:
    def __init__(self, document_links: DocumentLinksResource) -> None:
        self._document_links = document_links

        self.list = to_streamed_response_wrapper(
            document_links.list,
        )


class AsyncDocumentLinksResourceWithStreamingResponse:
    def __init__(self, document_links: AsyncDocumentLinksResource) -> None:
        self._document_links = document_links

        self.list = async_to_streamed_response_wrapper(
            document_links.list,
        )
