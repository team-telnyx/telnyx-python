# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.enterprises.reputation import external_verification_create_params
from ....types.enterprises.reputation.external_verification_wrapped import ExternalVerificationWrapped

__all__ = ["ExternalVerificationResource", "AsyncExternalVerificationResource"]


class ExternalVerificationResource(SyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> ExternalVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ExternalVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ExternalVerificationResourceWithStreamingResponse(self)

    def create(
        self,
        enterprise_id: str,
        *,
        document_ids: SequenceNotStr[str],
        phone_numbers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVerificationWrapped:
        """
        Request permission to add phone numbers that the enterprise owns but that are
        hosted with another provider. Submit one or more uploaded documents proving
        ownership, such as a carrier invoice or account statement. The request is
        reviewed once per enterprise. While it is `pending` or `rejected` you can submit
        again to replace the documents; once `approved` it cannot be changed.

        Args:
          document_ids: Ids of uploaded documents (Documents API) proving the enterprise owns its phone
              numbers hosted with another provider, for example a carrier invoice or account
              statement.

          phone_numbers: Optional. The phone numbers hosted with another provider that the documents
              cover, in E.164 format. Shown to the reviewer to match the documents to your
              numbers; you can still add numbers that are not listed here, and each is checked
              on its own.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation/external_verification", enterprise_id=enterprise_id),
            body=maybe_transform(
                {
                    "document_ids": document_ids,
                    "phone_numbers": phone_numbers,
                },
                external_verification_create_params.ExternalVerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVerificationWrapped,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVerificationWrapped:
        """
        Get the review status of the enterprise's ownership proof for phone numbers
        hosted with another provider. Returns 404 when no proof has been submitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get(
            path_template("/enterprises/{enterprise_id}/reputation/external_verification", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVerificationWrapped,
        )


class AsyncExternalVerificationResource(AsyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> AsyncExternalVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncExternalVerificationResourceWithStreamingResponse(self)

    async def create(
        self,
        enterprise_id: str,
        *,
        document_ids: SequenceNotStr[str],
        phone_numbers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVerificationWrapped:
        """
        Request permission to add phone numbers that the enterprise owns but that are
        hosted with another provider. Submit one or more uploaded documents proving
        ownership, such as a carrier invoice or account statement. The request is
        reviewed once per enterprise. While it is `pending` or `rejected` you can submit
        again to replace the documents; once `approved` it cannot be changed.

        Args:
          document_ids: Ids of uploaded documents (Documents API) proving the enterprise owns its phone
              numbers hosted with another provider, for example a carrier invoice or account
              statement.

          phone_numbers: Optional. The phone numbers hosted with another provider that the documents
              cover, in E.164 format. Shown to the reviewer to match the documents to your
              numbers; you can still add numbers that are not listed here, and each is checked
              on its own.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation/external_verification", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {
                    "document_ids": document_ids,
                    "phone_numbers": phone_numbers,
                },
                external_verification_create_params.ExternalVerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVerificationWrapped,
        )

    async def list(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVerificationWrapped:
        """
        Get the review status of the enterprise's ownership proof for phone numbers
        hosted with another provider. Returns 404 when no proof has been submitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._get(
            path_template("/enterprises/{enterprise_id}/reputation/external_verification", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVerificationWrapped,
        )


class ExternalVerificationResourceWithRawResponse:
    def __init__(self, external_verification: ExternalVerificationResource) -> None:
        self._external_verification = external_verification

        self.create = to_raw_response_wrapper(
            external_verification.create,
        )
        self.list = to_raw_response_wrapper(
            external_verification.list,
        )


class AsyncExternalVerificationResourceWithRawResponse:
    def __init__(self, external_verification: AsyncExternalVerificationResource) -> None:
        self._external_verification = external_verification

        self.create = async_to_raw_response_wrapper(
            external_verification.create,
        )
        self.list = async_to_raw_response_wrapper(
            external_verification.list,
        )


class ExternalVerificationResourceWithStreamingResponse:
    def __init__(self, external_verification: ExternalVerificationResource) -> None:
        self._external_verification = external_verification

        self.create = to_streamed_response_wrapper(
            external_verification.create,
        )
        self.list = to_streamed_response_wrapper(
            external_verification.list,
        )


class AsyncExternalVerificationResourceWithStreamingResponse:
    def __init__(self, external_verification: AsyncExternalVerificationResource) -> None:
        self._external_verification = external_verification

        self.create = async_to_streamed_response_wrapper(
            external_verification.create,
        )
        self.list = async_to_streamed_response_wrapper(
            external_verification.list,
        )
