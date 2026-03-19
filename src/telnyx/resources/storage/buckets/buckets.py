# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .ssl_certificate import (
    SslCertificateResource,
    AsyncSslCertificateResource,
    SslCertificateResourceWithRawResponse,
    AsyncSslCertificateResourceWithRawResponse,
    SslCertificateResourceWithStreamingResponse,
    AsyncSslCertificateResourceWithStreamingResponse,
)
from ....types.storage import bucket_create_presigned_url_params
from ....types.storage.bucket_create_presigned_url_response import BucketCreatePresignedURLResponse

__all__ = ["BucketsResource", "AsyncBucketsResource"]


class BucketsResource(SyncAPIResource):
    """Presigned object URL operations"""

    @cached_property
    def ssl_certificate(self) -> SslCertificateResource:
        """SSL certificate operations"""
        return SslCertificateResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        """Bucket Usage operations"""
        return UsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> BucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BucketsResourceWithStreamingResponse(self)

    def create_presigned_url(
        self,
        object_name: str,
        *,
        bucket_name: str,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketCreatePresignedURLResponse:
        """
        Returns a timed and authenticated URL to download (GET) or upload (PUT) an
        object. This is the equivalent to AWS S3’s “presigned” URL. Please note that
        Telnyx performs authentication differently from AWS S3 and you MUST NOT use the
        presign method of AWS s3api CLI or SDK to generate the presigned URL.

        Refer to: https://developers.telnyx.com/docs/cloud-storage/presigned-urls

        Args:
          ttl: The time to live of the token in seconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return self._post(
            path_template(
                "/storage/buckets/{bucket_name}/{object_name}/presigned_url",
                bucket_name=bucket_name,
                object_name=object_name,
            ),
            body=maybe_transform({"ttl": ttl}, bucket_create_presigned_url_params.BucketCreatePresignedURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketCreatePresignedURLResponse,
        )


class AsyncBucketsResource(AsyncAPIResource):
    """Presigned object URL operations"""

    @cached_property
    def ssl_certificate(self) -> AsyncSslCertificateResource:
        """SSL certificate operations"""
        return AsyncSslCertificateResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        """Bucket Usage operations"""
        return AsyncUsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBucketsResourceWithStreamingResponse(self)

    async def create_presigned_url(
        self,
        object_name: str,
        *,
        bucket_name: str,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketCreatePresignedURLResponse:
        """
        Returns a timed and authenticated URL to download (GET) or upload (PUT) an
        object. This is the equivalent to AWS S3’s “presigned” URL. Please note that
        Telnyx performs authentication differently from AWS S3 and you MUST NOT use the
        presign method of AWS s3api CLI or SDK to generate the presigned URL.

        Refer to: https://developers.telnyx.com/docs/cloud-storage/presigned-urls

        Args:
          ttl: The time to live of the token in seconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_name:
            raise ValueError(f"Expected a non-empty value for `object_name` but received {object_name!r}")
        return await self._post(
            path_template(
                "/storage/buckets/{bucket_name}/{object_name}/presigned_url",
                bucket_name=bucket_name,
                object_name=object_name,
            ),
            body=await async_maybe_transform(
                {"ttl": ttl}, bucket_create_presigned_url_params.BucketCreatePresignedURLParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketCreatePresignedURLResponse,
        )


class BucketsResourceWithRawResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create_presigned_url = to_raw_response_wrapper(
            buckets.create_presigned_url,
        )

    @cached_property
    def ssl_certificate(self) -> SslCertificateResourceWithRawResponse:
        """SSL certificate operations"""
        return SslCertificateResourceWithRawResponse(self._buckets.ssl_certificate)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        """Bucket Usage operations"""
        return UsageResourceWithRawResponse(self._buckets.usage)


class AsyncBucketsResourceWithRawResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create_presigned_url = async_to_raw_response_wrapper(
            buckets.create_presigned_url,
        )

    @cached_property
    def ssl_certificate(self) -> AsyncSslCertificateResourceWithRawResponse:
        """SSL certificate operations"""
        return AsyncSslCertificateResourceWithRawResponse(self._buckets.ssl_certificate)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        """Bucket Usage operations"""
        return AsyncUsageResourceWithRawResponse(self._buckets.usage)


class BucketsResourceWithStreamingResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create_presigned_url = to_streamed_response_wrapper(
            buckets.create_presigned_url,
        )

    @cached_property
    def ssl_certificate(self) -> SslCertificateResourceWithStreamingResponse:
        """SSL certificate operations"""
        return SslCertificateResourceWithStreamingResponse(self._buckets.ssl_certificate)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        """Bucket Usage operations"""
        return UsageResourceWithStreamingResponse(self._buckets.usage)


class AsyncBucketsResourceWithStreamingResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create_presigned_url = async_to_streamed_response_wrapper(
            buckets.create_presigned_url,
        )

    @cached_property
    def ssl_certificate(self) -> AsyncSslCertificateResourceWithStreamingResponse:
        """SSL certificate operations"""
        return AsyncSslCertificateResourceWithStreamingResponse(self._buckets.ssl_certificate)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        """Bucket Usage operations"""
        return AsyncUsageResourceWithStreamingResponse(self._buckets.usage)
