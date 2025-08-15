# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.portouts import supporting_document_create_params
from ...types.portouts.supporting_document_list_response import SupportingDocumentListResponse
from ...types.portouts.supporting_document_create_response import SupportingDocumentCreateResponse

__all__ = ["SupportingDocumentsResource", "AsyncSupportingDocumentsResource"]


class SupportingDocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupportingDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SupportingDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportingDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SupportingDocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        documents: Iterable[supporting_document_create_params.Document] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportingDocumentCreateResponse:
        """
        Creates a list of supporting documents on a portout request.

        Args:
          documents: List of supporting documents parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/portouts/{id}/supporting_documents",
            body=maybe_transform(
                {"documents": documents}, supporting_document_create_params.SupportingDocumentCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportingDocumentCreateResponse,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportingDocumentListResponse:
        """
        List every supporting documents for a portout request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/portouts/{id}/supporting_documents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportingDocumentListResponse,
        )


class AsyncSupportingDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupportingDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportingDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportingDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSupportingDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        documents: Iterable[supporting_document_create_params.Document] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportingDocumentCreateResponse:
        """
        Creates a list of supporting documents on a portout request.

        Args:
          documents: List of supporting documents parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/portouts/{id}/supporting_documents",
            body=await async_maybe_transform(
                {"documents": documents}, supporting_document_create_params.SupportingDocumentCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportingDocumentCreateResponse,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupportingDocumentListResponse:
        """
        List every supporting documents for a portout request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/portouts/{id}/supporting_documents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupportingDocumentListResponse,
        )


class SupportingDocumentsResourceWithRawResponse:
    def __init__(self, supporting_documents: SupportingDocumentsResource) -> None:
        self._supporting_documents = supporting_documents

        self.create = to_raw_response_wrapper(
            supporting_documents.create,
        )
        self.list = to_raw_response_wrapper(
            supporting_documents.list,
        )


class AsyncSupportingDocumentsResourceWithRawResponse:
    def __init__(self, supporting_documents: AsyncSupportingDocumentsResource) -> None:
        self._supporting_documents = supporting_documents

        self.create = async_to_raw_response_wrapper(
            supporting_documents.create,
        )
        self.list = async_to_raw_response_wrapper(
            supporting_documents.list,
        )


class SupportingDocumentsResourceWithStreamingResponse:
    def __init__(self, supporting_documents: SupportingDocumentsResource) -> None:
        self._supporting_documents = supporting_documents

        self.create = to_streamed_response_wrapper(
            supporting_documents.create,
        )
        self.list = to_streamed_response_wrapper(
            supporting_documents.list,
        )


class AsyncSupportingDocumentsResourceWithStreamingResponse:
    def __init__(self, supporting_documents: AsyncSupportingDocumentsResource) -> None:
        self._supporting_documents = supporting_documents

        self.create = async_to_streamed_response_wrapper(
            supporting_documents.create,
        )
        self.list = async_to_streamed_response_wrapper(
            supporting_documents.list,
        )
