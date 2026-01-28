# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import audit_event_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.audit_event_list_response import AuditEventListResponse

__all__ = ["AuditEventsResource", "AsyncAuditEventsResource"]


class AuditEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AuditEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AuditEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: audit_event_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[AuditEventListResponse]:
        """Retrieve a list of audit log entries.

        Audit logs are a best-effort, eventually
        consistent record of significant account-related changes.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[created_before], filter[created_after]

          sort: Set the order of the results by the creation date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audit_events",
            page=SyncDefaultFlatPagination[AuditEventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    audit_event_list_params.AuditEventListParams,
                ),
            ),
            model=AuditEventListResponse,
        )


class AsyncAuditEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAuditEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: audit_event_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditEventListResponse, AsyncDefaultFlatPagination[AuditEventListResponse]]:
        """Retrieve a list of audit log entries.

        Audit logs are a best-effort, eventually
        consistent record of significant account-related changes.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[created_before], filter[created_after]

          sort: Set the order of the results by the creation date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/audit_events",
            page=AsyncDefaultFlatPagination[AuditEventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    audit_event_list_params.AuditEventListParams,
                ),
            ),
            model=AuditEventListResponse,
        )


class AuditEventsResourceWithRawResponse:
    def __init__(self, audit_events: AuditEventsResource) -> None:
        self._audit_events = audit_events

        self.list = to_raw_response_wrapper(
            audit_events.list,
        )


class AsyncAuditEventsResourceWithRawResponse:
    def __init__(self, audit_events: AsyncAuditEventsResource) -> None:
        self._audit_events = audit_events

        self.list = async_to_raw_response_wrapper(
            audit_events.list,
        )


class AuditEventsResourceWithStreamingResponse:
    def __init__(self, audit_events: AuditEventsResource) -> None:
        self._audit_events = audit_events

        self.list = to_streamed_response_wrapper(
            audit_events.list,
        )


class AsyncAuditEventsResourceWithStreamingResponse:
    def __init__(self, audit_events: AsyncAuditEventsResource) -> None:
        self._audit_events = audit_events

        self.list = async_to_streamed_response_wrapper(
            audit_events.list,
        )
