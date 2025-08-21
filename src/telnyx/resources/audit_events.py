# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import audit_event_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
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
        filter: audit_event_list_params.Filter | NotGiven = NOT_GIVEN,
        page: audit_event_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuditEventListResponse:
        """Retrieve a list of audit log entries.

        Audit logs are a best-effort, eventually
        consistent record of significant account-related changes.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[created_before], filter[created_after]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Set the order of the results by the creation date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/audit_events",
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
                    audit_event_list_params.AuditEventListParams,
                ),
            ),
            cast_to=AuditEventListResponse,
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

    async def list(
        self,
        *,
        filter: audit_event_list_params.Filter | NotGiven = NOT_GIVEN,
        page: audit_event_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuditEventListResponse:
        """Retrieve a list of audit log entries.

        Audit logs are a best-effort, eventually
        consistent record of significant account-related changes.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[created_before], filter[created_after]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Set the order of the results by the creation date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/audit_events",
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
                    audit_event_list_params.AuditEventListParams,
                ),
            ),
            cast_to=AuditEventListResponse,
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
