# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.dir import (
    DirPhoneNumberStatus,
    phone_number_add_params,
    phone_number_list_params,
    phone_number_remove_params,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dir.dir_phone_number import DirPhoneNumber
from ...types.dir.phone_number_add_response import PhoneNumberAddResponse
from ...types.dir.phone_number_remove_response import PhoneNumberRemoveResponse

if TYPE_CHECKING:
    from ...types.document_param import DocumentParam
    from ...types.dir.dir_phone_number_status import DirPhoneNumberStatus

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    """
    Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
    """

    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        dir_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: DirPhoneNumberStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[DirPhoneNumber]:
        """List the phone numbers registered under a DIR.

        The enterprise is resolved
        server-side from the DIR id.

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          status: Filter by phone-number status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get_api_list(
            path_template("/dir/{dir_id}/phone_numbers", dir_id=dir_id),
            page=SyncDefaultFlatPagination[DirPhoneNumber],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=DirPhoneNumber,
        )

    def add(
        self,
        dir_id: str,
        *,
        documents: Iterable[DocumentParam],
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAddResponse:
        """Register phone numbers under a DIR.

        The enterprise is resolved server-side from
        the DIR id. Same body, failure modes, and batch semantics whichever path form
        you use.

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          documents: Supporting documents covering this batch. At least one entry with
              `document_type: letter_of_authorization` is required - the LOA authorises Telnyx
              to register these numbers under the DIR. Each `document_id` must come from the
              Telnyx Documents API. Additional document types (e.g. business registration) may
              be included alongside the LOA.

          phone_numbers: 1–15 phone numbers in E.164 format. 10-digit US numbers are auto-prefixed with
              `1`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._post(
            path_template("/dir/{dir_id}/phone_numbers", dir_id=dir_id),
            body=maybe_transform(
                {
                    "documents": documents,
                    "phone_numbers": phone_numbers,
                },
                phone_number_add_params.PhoneNumberAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAddResponse,
        )

    def remove(
        self,
        dir_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberRemoveResponse:
        """Deregister phone numbers from a DIR.

        The enterprise is resolved server-side from
        the DIR id. Returns a partial-success envelope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._delete(
            path_template("/dir/{dir_id}/phone_numbers", dir_id=dir_id),
            body=maybe_transform({"phone_numbers": phone_numbers}, phone_number_remove_params.PhoneNumberRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberRemoveResponse,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    """
    Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        dir_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: DirPhoneNumberStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DirPhoneNumber, AsyncDefaultFlatPagination[DirPhoneNumber]]:
        """List the phone numbers registered under a DIR.

        The enterprise is resolved
        server-side from the DIR id.

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          status: Filter by phone-number status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get_api_list(
            path_template("/dir/{dir_id}/phone_numbers", dir_id=dir_id),
            page=AsyncDefaultFlatPagination[DirPhoneNumber],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=DirPhoneNumber,
        )

    async def add(
        self,
        dir_id: str,
        *,
        documents: Iterable[DocumentParam],
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberAddResponse:
        """Register phone numbers under a DIR.

        The enterprise is resolved server-side from
        the DIR id. Same body, failure modes, and batch semantics whichever path form
        you use.

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          documents: Supporting documents covering this batch. At least one entry with
              `document_type: letter_of_authorization` is required - the LOA authorises Telnyx
              to register these numbers under the DIR. Each `document_id` must come from the
              Telnyx Documents API. Additional document types (e.g. business registration) may
              be included alongside the LOA.

          phone_numbers: 1–15 phone numbers in E.164 format. 10-digit US numbers are auto-prefixed with
              `1`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._post(
            path_template("/dir/{dir_id}/phone_numbers", dir_id=dir_id),
            body=await async_maybe_transform(
                {
                    "documents": documents,
                    "phone_numbers": phone_numbers,
                },
                phone_number_add_params.PhoneNumberAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberAddResponse,
        )

    async def remove(
        self,
        dir_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberRemoveResponse:
        """Deregister phone numbers from a DIR.

        The enterprise is resolved server-side from
        the DIR id. Returns a partial-success envelope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._delete(
            path_template("/dir/{dir_id}/phone_numbers", dir_id=dir_id),
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, phone_number_remove_params.PhoneNumberRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberRemoveResponse,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.add = to_raw_response_wrapper(
            phone_numbers.add,
        )
        self.remove = to_raw_response_wrapper(
            phone_numbers.remove,
        )


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.add = async_to_raw_response_wrapper(
            phone_numbers.add,
        )
        self.remove = async_to_raw_response_wrapper(
            phone_numbers.remove,
        )


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.add = to_streamed_response_wrapper(
            phone_numbers.add,
        )
        self.remove = to_streamed_response_wrapper(
            phone_numbers.remove,
        )


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.add = async_to_streamed_response_wrapper(
            phone_numbers.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            phone_numbers.remove,
        )
