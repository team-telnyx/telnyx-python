# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Mapping, cast
from typing_extensions import Literal, overload

import httpx

from ..types import document_list_params, document_update_params, document_upload_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, Base64FileInput
from .._utils import extract_files, required_args, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.document_list_response import DocumentListResponse
from ..types.document_delete_response import DocumentDeleteResponse
from ..types.document_update_response import DocumentUpdateResponse
from ..types.document_upload_response import DocumentUploadResponse
from ..types.document_retrieve_response import DocumentRetrieveResponse
from ..types.document_generate_download_link_response import DocumentGenerateDownloadLinkResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

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
    ) -> DocumentRetrieveResponse:
        """
        Retrieve a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUpdateResponse:
        """
        Update a document.

        Args:
          customer_reference: Optional reference string for customer tracking.

          filename: The filename of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/documents/{id}",
            body=maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "filename": filename,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    def list(
        self,
        *,
        filter: document_list_params.Filter | NotGiven = NOT_GIVEN,
        page: document_list_params.Page | NotGiven = NOT_GIVEN,
        sort: List[Literal["filename", "created_at", "updated_at", "-filename", "-created_at", "-updated_at"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentListResponse:
        """
        List all documents ordered by created_at descending.

        Args:
          filter:
              Consolidated filter parameter for documents (deepObject style). Originally:
              filter[filename][contains], filter[customer_reference][eq],
              filter[customer_reference][in][], filter[created_at][gt], filter[created_at][lt]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter for documents (deepObject style). Originally: sort[]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/documents",
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
                    document_list_params.DocumentListParams,
                ),
            ),
            cast_to=DocumentListResponse,
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
    ) -> DocumentDeleteResponse:
        """
        Delete a document.<br /><br />A document can only be deleted if it's not linked
        to a service. If it is linked to a service, it must be unlinked prior to
        deleting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    def download(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Download a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*", **(extra_headers or {})}
        return self._get(
            f"/documents/{id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def generate_download_link(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGenerateDownloadLinkResponse:
        """
        Generates a temporary pre-signed URL that can be used to download the document
        directly from the storage backend without authentication.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/documents/{id}/download_link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGenerateDownloadLinkResponse,
        )

    @overload
    def upload(
        self,
        *,
        url: str,
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        """
        Upload a document.<br /><br />Uploaded files must be linked to a service within
        30 minutes or they will be automatically deleted.

        Args:
          url: If the file is already hosted publicly, you can provide a URL and have the
              documents service fetch it for you.

          customer_reference: Optional reference string for customer tracking.

          filename: The filename of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def upload(
        self,
        *,
        file: Union[str, Base64FileInput],
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        """
        Upload a document.<br /><br />Uploaded files must be linked to a service within
        30 minutes or they will be automatically deleted.

        Args:
          file: The Base64 encoded contents of the file you are uploading.

          customer_reference: A customer reference string for customer look ups.

          filename: The filename of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["url"], ["file"])
    def upload(
        self,
        *,
        url: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        file: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        body = deepcopy_minimal(
            {
                "url": url,
                "customer_reference": customer_reference,
                "filename": filename,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/documents",
            body=maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUploadResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

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
    ) -> DocumentRetrieveResponse:
        """
        Retrieve a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUpdateResponse:
        """
        Update a document.

        Args:
          customer_reference: Optional reference string for customer tracking.

          filename: The filename of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/documents/{id}",
            body=await async_maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "filename": filename,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: document_list_params.Filter | NotGiven = NOT_GIVEN,
        page: document_list_params.Page | NotGiven = NOT_GIVEN,
        sort: List[Literal["filename", "created_at", "updated_at", "-filename", "-created_at", "-updated_at"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentListResponse:
        """
        List all documents ordered by created_at descending.

        Args:
          filter:
              Consolidated filter parameter for documents (deepObject style). Originally:
              filter[filename][contains], filter[customer_reference][eq],
              filter[customer_reference][in][], filter[created_at][gt], filter[created_at][lt]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter for documents (deepObject style). Originally: sort[]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/documents",
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
                    document_list_params.DocumentListParams,
                ),
            ),
            cast_to=DocumentListResponse,
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
    ) -> DocumentDeleteResponse:
        """
        Delete a document.<br /><br />A document can only be deleted if it's not linked
        to a service. If it is linked to a service, it must be unlinked prior to
        deleting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    async def download(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Download a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*", **(extra_headers or {})}
        return await self._get(
            f"/documents/{id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def generate_download_link(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGenerateDownloadLinkResponse:
        """
        Generates a temporary pre-signed URL that can be used to download the document
        directly from the storage backend without authentication.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/documents/{id}/download_link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGenerateDownloadLinkResponse,
        )

    @overload
    async def upload(
        self,
        *,
        url: str,
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        """
        Upload a document.<br /><br />Uploaded files must be linked to a service within
        30 minutes or they will be automatically deleted.

        Args:
          url: If the file is already hosted publicly, you can provide a URL and have the
              documents service fetch it for you.

          customer_reference: Optional reference string for customer tracking.

          filename: The filename of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def upload(
        self,
        *,
        file: Union[str, Base64FileInput],
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        """
        Upload a document.<br /><br />Uploaded files must be linked to a service within
        30 minutes or they will be automatically deleted.

        Args:
          file: The Base64 encoded contents of the file you are uploading.

          customer_reference: A customer reference string for customer look ups.

          filename: The filename of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["url"], ["file"])
    async def upload(
        self,
        *,
        url: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        filename: str | NotGiven = NOT_GIVEN,
        file: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUploadResponse:
        body = deepcopy_minimal(
            {
                "url": url,
                "customer_reference": customer_reference,
                "filename": filename,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/documents",
            body=await async_maybe_transform(body, document_upload_params.DocumentUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUploadResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.retrieve = to_raw_response_wrapper(
            documents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            documents.update,
        )
        self.list = to_raw_response_wrapper(
            documents.list,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )
        self.download = to_custom_raw_response_wrapper(
            documents.download,
            BinaryAPIResponse,
        )
        self.generate_download_link = to_raw_response_wrapper(
            documents.generate_download_link,
        )
        self.upload = to_raw_response_wrapper(
            documents.upload,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.retrieve = async_to_raw_response_wrapper(
            documents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            documents.update,
        )
        self.list = async_to_raw_response_wrapper(
            documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )
        self.download = async_to_custom_raw_response_wrapper(
            documents.download,
            AsyncBinaryAPIResponse,
        )
        self.generate_download_link = async_to_raw_response_wrapper(
            documents.generate_download_link,
        )
        self.upload = async_to_raw_response_wrapper(
            documents.upload,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            documents.update,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )
        self.download = to_custom_streamed_response_wrapper(
            documents.download,
            StreamedBinaryAPIResponse,
        )
        self.generate_download_link = to_streamed_response_wrapper(
            documents.generate_download_link,
        )
        self.upload = to_streamed_response_wrapper(
            documents.upload,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            documents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            documents.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.generate_download_link = async_to_streamed_response_wrapper(
            documents.generate_download_link,
        )
        self.upload = async_to_streamed_response_wrapper(
            documents.upload,
        )
