# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

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
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.enterprises.reputation import remediation_list_params, remediation_submit_params
from ....types.enterprises.reputation.remediation_list_response import RemediationListResponse
from ....types.enterprises.reputation.remediation_submit_response import RemediationSubmitResponse
from ....types.enterprises.reputation.remediation_retrieve_response import RemediationRetrieveResponse

__all__ = ["RemediationResource", "AsyncRemediationResource"]


class RemediationResource(SyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> RemediationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RemediationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemediationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return RemediationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        remediation_id: str,
        *,
        enterprise_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationRetrieveResponse:
        """
        Retrieve the full detail of a remediation request, including current status,
        per-number results (once available), and submission metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return self._get(
            path_template(
                "/enterprises/{enterprise_id}/reputation/remediation/{remediation_id}",
                enterprise_id=enterprise_id,
                remediation_id=remediation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationRetrieveResponse,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        filter_created_at_gte: Union[str, datetime] | Omit = omit,
        filter_created_at_lte: Union[str, datetime] | Omit = omit,
        filter_status: Literal["pending", "in_progress", "completed", "failed", "cancelled"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RemediationListResponse]:
        """Paginated list of remediation requests for this enterprise.

        List items omit
        per-number results and webhook URLs to keep the response small; call GET by id
        for full detail. Supports JSON:API pagination and optional filters on status and
        created-at range.

        Args:
          filter_created_at_gte: Only requests created on or after this timestamp (ISO 8601).

          filter_created_at_lte: Only requests created on or before this timestamp (ISO 8601).

          filter_status: Filter by customer-facing status.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/reputation/remediation", enterprise_id=enterprise_id),
            page=SyncDefaultFlatPagination[RemediationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at_gte": filter_created_at_gte,
                        "filter_created_at_lte": filter_created_at_lte,
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    remediation_list_params.RemediationListParams,
                ),
            ),
            model=RemediationListResponse,
        )

    def submit(
        self,
        enterprise_id: str,
        *,
        call_purpose: str,
        phone_numbers: SequenceNotStr[str],
        contact_email: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationSubmitResponse:
        """
        Submit a batch of phone numbers belonging to this enterprise for reputation
        remediation. The request is accepted asynchronously: this endpoint returns `202`
        with the persisted request id, then the request transitions through processing
        states until completion. Use the GET endpoints to poll status and per-number
        results.

        Each phone number must be in E.164 format and belong to this enterprise. A
        number that already has an in-flight remediation request is rejected.

        Args:
          call_purpose: How the numbers are used (free text).

          phone_numbers: Phone numbers in E.164 format. Each must belong to this enterprise. Maximum
              2,000 per request.

          contact_email: Optional contact email for this remediation request.

          webhook_url: Optional https:// URL for status notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation/remediation", enterprise_id=enterprise_id),
            body=maybe_transform(
                {
                    "call_purpose": call_purpose,
                    "phone_numbers": phone_numbers,
                    "contact_email": contact_email,
                    "webhook_url": webhook_url,
                },
                remediation_submit_params.RemediationSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationSubmitResponse,
        )


class AsyncRemediationResource(AsyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> AsyncRemediationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRemediationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemediationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncRemediationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        remediation_id: str,
        *,
        enterprise_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationRetrieveResponse:
        """
        Retrieve the full detail of a remediation request, including current status,
        per-number results (once available), and submission metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not remediation_id:
            raise ValueError(f"Expected a non-empty value for `remediation_id` but received {remediation_id!r}")
        return await self._get(
            path_template(
                "/enterprises/{enterprise_id}/reputation/remediation/{remediation_id}",
                enterprise_id=enterprise_id,
                remediation_id=remediation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationRetrieveResponse,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        filter_created_at_gte: Union[str, datetime] | Omit = omit,
        filter_created_at_lte: Union[str, datetime] | Omit = omit,
        filter_status: Literal["pending", "in_progress", "completed", "failed", "cancelled"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RemediationListResponse, AsyncDefaultFlatPagination[RemediationListResponse]]:
        """Paginated list of remediation requests for this enterprise.

        List items omit
        per-number results and webhook URLs to keep the response small; call GET by id
        for full detail. Supports JSON:API pagination and optional filters on status and
        created-at range.

        Args:
          filter_created_at_gte: Only requests created on or after this timestamp (ISO 8601).

          filter_created_at_lte: Only requests created on or before this timestamp (ISO 8601).

          filter_status: Filter by customer-facing status.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/reputation/remediation", enterprise_id=enterprise_id),
            page=AsyncDefaultFlatPagination[RemediationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at_gte": filter_created_at_gte,
                        "filter_created_at_lte": filter_created_at_lte,
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    remediation_list_params.RemediationListParams,
                ),
            ),
            model=RemediationListResponse,
        )

    async def submit(
        self,
        enterprise_id: str,
        *,
        call_purpose: str,
        phone_numbers: SequenceNotStr[str],
        contact_email: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemediationSubmitResponse:
        """
        Submit a batch of phone numbers belonging to this enterprise for reputation
        remediation. The request is accepted asynchronously: this endpoint returns `202`
        with the persisted request id, then the request transitions through processing
        states until completion. Use the GET endpoints to poll status and per-number
        results.

        Each phone number must be in E.164 format and belong to this enterprise. A
        number that already has an in-flight remediation request is rejected.

        Args:
          call_purpose: How the numbers are used (free text).

          phone_numbers: Phone numbers in E.164 format. Each must belong to this enterprise. Maximum
              2,000 per request.

          contact_email: Optional contact email for this remediation request.

          webhook_url: Optional https:// URL for status notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation/remediation", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {
                    "call_purpose": call_purpose,
                    "phone_numbers": phone_numbers,
                    "contact_email": contact_email,
                    "webhook_url": webhook_url,
                },
                remediation_submit_params.RemediationSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RemediationSubmitResponse,
        )


class RemediationResourceWithRawResponse:
    def __init__(self, remediation: RemediationResource) -> None:
        self._remediation = remediation

        self.retrieve = to_raw_response_wrapper(
            remediation.retrieve,
        )
        self.list = to_raw_response_wrapper(
            remediation.list,
        )
        self.submit = to_raw_response_wrapper(
            remediation.submit,
        )


class AsyncRemediationResourceWithRawResponse:
    def __init__(self, remediation: AsyncRemediationResource) -> None:
        self._remediation = remediation

        self.retrieve = async_to_raw_response_wrapper(
            remediation.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            remediation.list,
        )
        self.submit = async_to_raw_response_wrapper(
            remediation.submit,
        )


class RemediationResourceWithStreamingResponse:
    def __init__(self, remediation: RemediationResource) -> None:
        self._remediation = remediation

        self.retrieve = to_streamed_response_wrapper(
            remediation.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            remediation.list,
        )
        self.submit = to_streamed_response_wrapper(
            remediation.submit,
        )


class AsyncRemediationResourceWithStreamingResponse:
    def __init__(self, remediation: AsyncRemediationResource) -> None:
        self._remediation = remediation

        self.retrieve = async_to_streamed_response_wrapper(
            remediation.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            remediation.list,
        )
        self.submit = async_to_streamed_response_wrapper(
            remediation.submit,
        )
