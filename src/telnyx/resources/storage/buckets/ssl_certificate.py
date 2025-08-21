# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage.buckets import ssl_certificate_create_params
from ....types.storage.buckets.ssl_certificate_create_response import SslCertificateCreateResponse
from ....types.storage.buckets.ssl_certificate_delete_response import SslCertificateDeleteResponse
from ....types.storage.buckets.ssl_certificate_retrieve_response import SslCertificateRetrieveResponse

__all__ = ["SslCertificateResource", "AsyncSslCertificateResource"]


class SslCertificateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SslCertificateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SslCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SslCertificateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SslCertificateResourceWithStreamingResponse(self)

    def create(
        self,
        bucket_name: str,
        *,
        certificate: FileTypes | NotGiven = NOT_GIVEN,
        private_key: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SslCertificateCreateResponse:
        """
        Uploads an SSL certificate and its matching secret so that you can use Telnyx’s
        storage as your CDN.

        Args:
          certificate: The SSL certificate file

          private_key: The private key file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        body = deepcopy_minimal(
            {
                "certificate": certificate,
                "private_key": private_key,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["certificate"], ["private_key"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/storage/buckets/{bucket_name}/ssl_certificate",
            body=maybe_transform(body, ssl_certificate_create_params.SslCertificateCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslCertificateCreateResponse,
        )

    def retrieve(
        self,
        bucket_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SslCertificateRetrieveResponse:
        """
        Returns the stored certificate detail of a bucket, if applicable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            f"/storage/buckets/{bucket_name}/ssl_certificate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslCertificateRetrieveResponse,
        )

    def delete(
        self,
        bucket_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SslCertificateDeleteResponse:
        """
        Deletes an SSL certificate and its matching secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._delete(
            f"/storage/buckets/{bucket_name}/ssl_certificate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslCertificateDeleteResponse,
        )


class AsyncSslCertificateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSslCertificateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSslCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSslCertificateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSslCertificateResourceWithStreamingResponse(self)

    async def create(
        self,
        bucket_name: str,
        *,
        certificate: FileTypes | NotGiven = NOT_GIVEN,
        private_key: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SslCertificateCreateResponse:
        """
        Uploads an SSL certificate and its matching secret so that you can use Telnyx’s
        storage as your CDN.

        Args:
          certificate: The SSL certificate file

          private_key: The private key file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        body = deepcopy_minimal(
            {
                "certificate": certificate,
                "private_key": private_key,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["certificate"], ["private_key"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/storage/buckets/{bucket_name}/ssl_certificate",
            body=await async_maybe_transform(body, ssl_certificate_create_params.SslCertificateCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslCertificateCreateResponse,
        )

    async def retrieve(
        self,
        bucket_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SslCertificateRetrieveResponse:
        """
        Returns the stored certificate detail of a bucket, if applicable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            f"/storage/buckets/{bucket_name}/ssl_certificate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslCertificateRetrieveResponse,
        )

    async def delete(
        self,
        bucket_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SslCertificateDeleteResponse:
        """
        Deletes an SSL certificate and its matching secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._delete(
            f"/storage/buckets/{bucket_name}/ssl_certificate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SslCertificateDeleteResponse,
        )


class SslCertificateResourceWithRawResponse:
    def __init__(self, ssl_certificate: SslCertificateResource) -> None:
        self._ssl_certificate = ssl_certificate

        self.create = to_raw_response_wrapper(
            ssl_certificate.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ssl_certificate.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            ssl_certificate.delete,
        )


class AsyncSslCertificateResourceWithRawResponse:
    def __init__(self, ssl_certificate: AsyncSslCertificateResource) -> None:
        self._ssl_certificate = ssl_certificate

        self.create = async_to_raw_response_wrapper(
            ssl_certificate.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ssl_certificate.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            ssl_certificate.delete,
        )


class SslCertificateResourceWithStreamingResponse:
    def __init__(self, ssl_certificate: SslCertificateResource) -> None:
        self._ssl_certificate = ssl_certificate

        self.create = to_streamed_response_wrapper(
            ssl_certificate.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ssl_certificate.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            ssl_certificate.delete,
        )


class AsyncSslCertificateResourceWithStreamingResponse:
    def __init__(self, ssl_certificate: AsyncSslCertificateResource) -> None:
        self._ssl_certificate = ssl_certificate

        self.create = async_to_streamed_response_wrapper(
            ssl_certificate.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ssl_certificate.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            ssl_certificate.delete,
        )
