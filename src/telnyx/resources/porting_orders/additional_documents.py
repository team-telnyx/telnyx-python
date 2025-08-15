# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.porting_orders import additional_document_list_params, additional_document_create_params
from ...types.porting_orders.additional_document_list_response import AdditionalDocumentListResponse
from ...types.porting_orders.additional_document_create_response import AdditionalDocumentCreateResponse

__all__ = ["AdditionalDocumentsResource", "AsyncAdditionalDocumentsResource"]


class AdditionalDocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdditionalDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AdditionalDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdditionalDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AdditionalDocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        additional_documents: Iterable[additional_document_create_params.AdditionalDocument] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalDocumentCreateResponse:
        """
        Creates a list of additional documents for a porting order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/porting_orders/{id}/additional_documents",
            body=maybe_transform(
                {"additional_documents": additional_documents},
                additional_document_create_params.AdditionalDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalDocumentCreateResponse,
        )

    def list(
        self,
        id: str,
        *,
        filter: additional_document_list_params.Filter | NotGiven = NOT_GIVEN,
        page: additional_document_list_params.Page | NotGiven = NOT_GIVEN,
        sort: additional_document_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalDocumentListResponse:
        """
        Returns a list of additional documents for a porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[document_type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting_orders/{id}/additional_documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    additional_document_list_params.AdditionalDocumentListParams,
                ),
            ),
            cast_to=AdditionalDocumentListResponse,
        )

    def delete(
        self,
        additional_document_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an additional document for a porting order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not additional_document_id:
            raise ValueError(
                f"Expected a non-empty value for `additional_document_id` but received {additional_document_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/porting_orders/{id}/additional_documents/{additional_document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAdditionalDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdditionalDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdditionalDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdditionalDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAdditionalDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        additional_documents: Iterable[additional_document_create_params.AdditionalDocument] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalDocumentCreateResponse:
        """
        Creates a list of additional documents for a porting order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/porting_orders/{id}/additional_documents",
            body=await async_maybe_transform(
                {"additional_documents": additional_documents},
                additional_document_create_params.AdditionalDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdditionalDocumentCreateResponse,
        )

    async def list(
        self,
        id: str,
        *,
        filter: additional_document_list_params.Filter | NotGiven = NOT_GIVEN,
        page: additional_document_list_params.Page | NotGiven = NOT_GIVEN,
        sort: additional_document_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdditionalDocumentListResponse:
        """
        Returns a list of additional documents for a porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[document_type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting_orders/{id}/additional_documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    additional_document_list_params.AdditionalDocumentListParams,
                ),
            ),
            cast_to=AdditionalDocumentListResponse,
        )

    async def delete(
        self,
        additional_document_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an additional document for a porting order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not additional_document_id:
            raise ValueError(
                f"Expected a non-empty value for `additional_document_id` but received {additional_document_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/porting_orders/{id}/additional_documents/{additional_document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AdditionalDocumentsResourceWithRawResponse:
    def __init__(self, additional_documents: AdditionalDocumentsResource) -> None:
        self._additional_documents = additional_documents

        self.create = to_raw_response_wrapper(
            additional_documents.create,
        )
        self.list = to_raw_response_wrapper(
            additional_documents.list,
        )
        self.delete = to_raw_response_wrapper(
            additional_documents.delete,
        )


class AsyncAdditionalDocumentsResourceWithRawResponse:
    def __init__(self, additional_documents: AsyncAdditionalDocumentsResource) -> None:
        self._additional_documents = additional_documents

        self.create = async_to_raw_response_wrapper(
            additional_documents.create,
        )
        self.list = async_to_raw_response_wrapper(
            additional_documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            additional_documents.delete,
        )


class AdditionalDocumentsResourceWithStreamingResponse:
    def __init__(self, additional_documents: AdditionalDocumentsResource) -> None:
        self._additional_documents = additional_documents

        self.create = to_streamed_response_wrapper(
            additional_documents.create,
        )
        self.list = to_streamed_response_wrapper(
            additional_documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            additional_documents.delete,
        )


class AsyncAdditionalDocumentsResourceWithStreamingResponse:
    def __init__(self, additional_documents: AsyncAdditionalDocumentsResource) -> None:
        self._additional_documents = additional_documents

        self.create = async_to_streamed_response_wrapper(
            additional_documents.create,
        )
        self.list = async_to_streamed_response_wrapper(
            additional_documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            additional_documents.delete,
        )
