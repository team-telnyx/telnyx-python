# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import call_reason_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.call_reason_list_response import CallReasonListResponse
from ..types.call_reason_validate_response import CallReasonValidateResponse

__all__ = ["CallReasonsResource", "AsyncCallReasonsResource"]


class CallReasonsResource(SyncAPIResource):
    """
    Static reference values the API accepts: call reasons, document types, rejection types.
    """

    @cached_property
    def with_raw_response(self) -> CallReasonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallReasonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallReasonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return CallReasonsResourceWithStreamingResponse(self)

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
    ) -> SyncDefaultFlatPagination[CallReasonListResponse]:
        """Telnyx maintains a library of pre-vetted call-reason phrases (e.g.

        "Appointment
        reminders", "Billing inquiries") that carry through DIR vetting smoothly. You
        can use any string that fits your use case in `DirCreateRequest.call_reasons`,
        but matching one of these reduces the chance the vetting team flags the phrasing
        for clarification.

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Default `100` for this endpoint (the call-reason library is
              small and most callers want the whole list in one call). Maximum 250; values
              above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/call_reasons",
            page=SyncDefaultFlatPagination[CallReasonListResponse],
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
                    call_reason_list_params.CallReasonListParams,
                ),
            ),
            model=CallReasonListResponse,
        )

    def validate(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallReasonValidateResponse:
        """
        Check up to 10 candidate `call_reasons` strings against Telnyx's vetting
        heuristics before sending them on a DIR create or update. The endpoint flags
        strings that are likely to be rejected during vetting (too generic, banned
        phrases, length issues, etc.) so you can fix them up front.

        Args:
          body: **Bare JSON array** of candidate call-reason strings (NOT an object - there is
              no top-level `call_reasons` key on this endpoint). 1–10 strings, each ≤64
              characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call_reasons/validate",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallReasonValidateResponse,
        )


class AsyncCallReasonsResource(AsyncAPIResource):
    """
    Static reference values the API accepts: call reasons, document types, rejection types.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCallReasonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallReasonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallReasonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncCallReasonsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[CallReasonListResponse, AsyncDefaultFlatPagination[CallReasonListResponse]]:
        """Telnyx maintains a library of pre-vetted call-reason phrases (e.g.

        "Appointment
        reminders", "Billing inquiries") that carry through DIR vetting smoothly. You
        can use any string that fits your use case in `DirCreateRequest.call_reasons`,
        but matching one of these reduces the chance the vetting team flags the phrasing
        for clarification.

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Default `100` for this endpoint (the call-reason library is
              small and most callers want the whole list in one call). Maximum 250; values
              above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/call_reasons",
            page=AsyncDefaultFlatPagination[CallReasonListResponse],
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
                    call_reason_list_params.CallReasonListParams,
                ),
            ),
            model=CallReasonListResponse,
        )

    async def validate(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallReasonValidateResponse:
        """
        Check up to 10 candidate `call_reasons` strings against Telnyx's vetting
        heuristics before sending them on a DIR create or update. The endpoint flags
        strings that are likely to be rejected during vetting (too generic, banned
        phrases, length issues, etc.) so you can fix them up front.

        Args:
          body: **Bare JSON array** of candidate call-reason strings (NOT an object - there is
              no top-level `call_reasons` key on this endpoint). 1–10 strings, each ≤64
              characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call_reasons/validate",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallReasonValidateResponse,
        )


class CallReasonsResourceWithRawResponse:
    def __init__(self, call_reasons: CallReasonsResource) -> None:
        self._call_reasons = call_reasons

        self.list = to_raw_response_wrapper(
            call_reasons.list,
        )
        self.validate = to_raw_response_wrapper(
            call_reasons.validate,
        )


class AsyncCallReasonsResourceWithRawResponse:
    def __init__(self, call_reasons: AsyncCallReasonsResource) -> None:
        self._call_reasons = call_reasons

        self.list = async_to_raw_response_wrapper(
            call_reasons.list,
        )
        self.validate = async_to_raw_response_wrapper(
            call_reasons.validate,
        )


class CallReasonsResourceWithStreamingResponse:
    def __init__(self, call_reasons: CallReasonsResource) -> None:
        self._call_reasons = call_reasons

        self.list = to_streamed_response_wrapper(
            call_reasons.list,
        )
        self.validate = to_streamed_response_wrapper(
            call_reasons.validate,
        )


class AsyncCallReasonsResourceWithStreamingResponse:
    def __init__(self, call_reasons: AsyncCallReasonsResource) -> None:
        self._call_reasons = call_reasons

        self.list = async_to_streamed_response_wrapper(
            call_reasons.list,
        )
        self.validate = async_to_streamed_response_wrapper(
            call_reasons.validate,
        )
