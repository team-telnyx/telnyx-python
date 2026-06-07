# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.enterprises.reputation import (
    number_list_params,
    number_refresh_params,
    number_retrieve_params,
    number_associate_params,
)
from ....types.enterprises.reputation.number_list_response import NumberListResponse
from ....types.enterprises.reputation.number_refresh_response import NumberRefreshResponse
from ....types.enterprises.reputation.number_retrieve_response import NumberRetrieveResponse
from ....types.enterprises.reputation.number_associate_response import NumberAssociateResponse

__all__ = ["NumbersResource", "AsyncNumbersResource"]


class NumbersResource(SyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> NumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumbersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        phone_number: str,
        *,
        enterprise_id: str,
        fresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """Retrieve one registered number with its latest reputation snapshot.

        The
        `phone_number` path parameter is in E.164 format and must be URL-encoded (e.g.
        `%2B19493253498`).

        Args:
          fresh: When true, fetches fresh reputation data (incurs API cost). When false
              (default), returns cached data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"fresh": fresh}, number_retrieve_params.NumberRetrieveParams),
            ),
            cast_to=NumberRetrieveResponse,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        filter_phone_number_contains: str | Omit = omit,
        filter_phone_number_eq: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[NumberListResponse]:
        """
        Paginated list of phone numbers registered for reputation monitoring under this
        enterprise. The response includes the latest reputation snapshot per number
        where one has been collected.

        Args:
          filter_phone_number_contains: Partial match on phone number. Must contain at least 5 digits.

          filter_phone_number_eq: Exact phone-number match (E.164).

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Default 10. Maximum 250; values above are clamped to 250.

          phone_number: Filter by specific phone number (E.164 format).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
            page=SyncDefaultFlatPagination[NumberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_phone_number_contains": filter_phone_number_contains,
                        "filter_phone_number_eq": filter_phone_number_eq,
                        "page_number": page_number,
                        "page_size": page_size,
                        "phone_number": phone_number,
                    },
                    number_list_params.NumberListParams,
                ),
            ),
            model=NumberListResponse,
        )

    def associate(
        self,
        enterprise_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberAssociateResponse:
        """Add up to 100 phone numbers to reputation monitoring on this enterprise.

        Each
        must be in E.164 format (`+1NPANXXXXXX` for US/CA) and belong to your Telnyx
        phone-number inventory.

        **Prerequisite**: reputation must already be enabled on this enterprise (see
        `POST .../reputation`).

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          phone_numbers: 1–100 phone numbers in E.164 format with a leading `+`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
            body=maybe_transform({"phone_numbers": phone_numbers}, number_associate_params.NumberAssociateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberAssociateResponse,
        )

    def disassociate(
        self,
        phone_number: str,
        *,
        enterprise_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Stop tracking the reputation of this phone number.

        The number itself remains in
        your inventory; only the reputation registration is removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def refresh(
        self,
        enterprise_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRefreshResponse:
        """Immediately refresh the stored reputation data for the listed numbers.

        This is
        in addition to the periodic refresh determined by `check_frequency`. Up to 100
        numbers per call. The response carries the kicked-off jobs; the actual refresh
        runs asynchronously.

        **Pricing:** Forcing a refresh performs live reputation lookups, which are
        billable. See https://telnyx.com/pricing/numbers for current pricing.

        Args:
          phone_numbers: Phone numbers to refresh reputation data for. 1–100 numbers per request, each in
              E.164 format. Reputation refreshes are subject to per-enterprise rate limits.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation/numbers/refresh", enterprise_id=enterprise_id),
            body=maybe_transform({"phone_numbers": phone_numbers}, number_refresh_params.NumberRefreshParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberRefreshResponse,
        )


class AsyncNumbersResource(AsyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> AsyncNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumbersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        phone_number: str,
        *,
        enterprise_id: str,
        fresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """Retrieve one registered number with its latest reputation snapshot.

        The
        `phone_number` path parameter is in E.164 format and must be URL-encoded (e.g.
        `%2B19493253498`).

        Args:
          fresh: When true, fetches fresh reputation data (incurs API cost). When false
              (default), returns cached data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"fresh": fresh}, number_retrieve_params.NumberRetrieveParams),
            ),
            cast_to=NumberRetrieveResponse,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        filter_phone_number_contains: str | Omit = omit,
        filter_phone_number_eq: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NumberListResponse, AsyncDefaultFlatPagination[NumberListResponse]]:
        """
        Paginated list of phone numbers registered for reputation monitoring under this
        enterprise. The response includes the latest reputation snapshot per number
        where one has been collected.

        Args:
          filter_phone_number_contains: Partial match on phone number. Must contain at least 5 digits.

          filter_phone_number_eq: Exact phone-number match (E.164).

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Default 10. Maximum 250; values above are clamped to 250.

          phone_number: Filter by specific phone number (E.164 format).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
            page=AsyncDefaultFlatPagination[NumberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_phone_number_contains": filter_phone_number_contains,
                        "filter_phone_number_eq": filter_phone_number_eq,
                        "page_number": page_number,
                        "page_size": page_size,
                        "phone_number": phone_number,
                    },
                    number_list_params.NumberListParams,
                ),
            ),
            model=NumberListResponse,
        )

    async def associate(
        self,
        enterprise_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberAssociateResponse:
        """Add up to 100 phone numbers to reputation monitoring on this enterprise.

        Each
        must be in E.164 format (`+1NPANXXXXXX` for US/CA) and belong to your Telnyx
        phone-number inventory.

        **Prerequisite**: reputation must already be enabled on this enterprise (see
        `POST .../reputation`).

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          phone_numbers: 1–100 phone numbers in E.164 format with a leading `+`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, number_associate_params.NumberAssociateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberAssociateResponse,
        )

    async def disassociate(
        self,
        phone_number: str,
        *,
        enterprise_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Stop tracking the reputation of this phone number.

        The number itself remains in
        your inventory; only the reputation registration is removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def refresh(
        self,
        enterprise_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRefreshResponse:
        """Immediately refresh the stored reputation data for the listed numbers.

        This is
        in addition to the periodic refresh determined by `check_frequency`. Up to 100
        numbers per call. The response carries the kicked-off jobs; the actual refresh
        runs asynchronously.

        **Pricing:** Forcing a refresh performs live reputation lookups, which are
        billable. See https://telnyx.com/pricing/numbers for current pricing.

        Args:
          phone_numbers: Phone numbers to refresh reputation data for. 1–100 numbers per request, each in
              E.164 format. Reputation refreshes are subject to per-enterprise rate limits.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation/numbers/refresh", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, number_refresh_params.NumberRefreshParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberRefreshResponse,
        )


class NumbersResourceWithRawResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = to_raw_response_wrapper(
            numbers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            numbers.list,
        )
        self.associate = to_raw_response_wrapper(
            numbers.associate,
        )
        self.disassociate = to_raw_response_wrapper(
            numbers.disassociate,
        )
        self.refresh = to_raw_response_wrapper(
            numbers.refresh,
        )


class AsyncNumbersResourceWithRawResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = async_to_raw_response_wrapper(
            numbers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            numbers.list,
        )
        self.associate = async_to_raw_response_wrapper(
            numbers.associate,
        )
        self.disassociate = async_to_raw_response_wrapper(
            numbers.disassociate,
        )
        self.refresh = async_to_raw_response_wrapper(
            numbers.refresh,
        )


class NumbersResourceWithStreamingResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            numbers.list,
        )
        self.associate = to_streamed_response_wrapper(
            numbers.associate,
        )
        self.disassociate = to_streamed_response_wrapper(
            numbers.disassociate,
        )
        self.refresh = to_streamed_response_wrapper(
            numbers.refresh,
        )


class AsyncNumbersResourceWithStreamingResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = async_to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            numbers.list,
        )
        self.associate = async_to_streamed_response_wrapper(
            numbers.associate,
        )
        self.disassociate = async_to_streamed_response_wrapper(
            numbers.disassociate,
        )
        self.refresh = async_to_streamed_response_wrapper(
            numbers.refresh,
        )
