# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import email_event_list_params, email_event_retrieve_stats_params
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
from .._base_client import make_request_options
from ..types.email_event_list_response import EmailEventListResponse
from ..types.email_event_retrieve_stats_response import EmailEventRetrieveStatsResponse

__all__ = ["EmailEventsResource", "AsyncEmailEventsResource"]


class EmailEventsResource(SyncAPIResource):
    """Retrieve account-level email events and event statistics."""

    @cached_property
    def with_raw_response(self) -> EmailEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        email_id: str | Omit = omit,
        event_type: Union[str, SequenceNotStr[str]] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        page_cursor: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailEventListResponse:
        """
        Lists account-level email events sorted oldest first by
        `occurred_at asc, id asc`. Each row contains a legacy email.-prefixed event_type
        and an additive canonical_event_type. Gateway rejection renders email.failed
        with canonical email.gw_reject; ambiguous injection timeout renders
        email.injection_timeout in both; MTA expiration renders email.bounced with
        canonical email.expired. Message-scoped queued, sending, sandbox, cancelled, and
        daily_limit_exceeded rows fan out per durable recipient with stable derived IDs
        matching webhook delivery. Scheduled is the cardinality exception: account
        polling retains one message-scoped scheduled row with its stored event ID, while
        scheduled webhook publication fans out per recipient with derived IDs; reconcile
        scheduled events by message ID, event type, and occurrence time rather than
        event UUID. Recipient-scoped stored rows retain their stored UUIDs across
        polling and webhook delivery. Legacy names are derived from stored rows; an
        AdminBounce row stored as failed renders email.failed in polling while its
        webhook retains email.bounced, both with canonical email.failed.

        Args:
          email_id: Filter events for a specific email message UUID. Invalid UUID values are
              silently ignored (no filter applied).

          event_type: Comma-separated list of event types to include. Also accepts repeated query
              parameters (e.g. event_type=delivered&event_type=bounced). Unknown values return
              no matches.

              Dual-name compatibility: values are accepted bare or `email.`-prefixed. A legacy
              value keeps matching the rows it matched pre-rename — no widening: `failed` also
              matches the rows that now store the canonical names of the outcomes it covered
              (`gw_reject`, `injection_timeout`, `expired`); `bounced` matches stored
              `bounced` rows only (recipient-scoped Expirations stored `failed` pre-rename and
              never matched `bounced`, so `expired` is deliberately not a `bounced`
              expansion). A canonical value matches its own rows plus legacy rows whose
              recorded payload evidence proves that outcome (`expired` also surfaces legacy
              `bounced` rows with `bounce_category: transient`). The additive
              `canonical_event_type` field in each response row names the canonical outcome.

          from_: Inclusive ISO 8601 start timestamp. Defaults to 30 days ago when omitted.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          page_cursor: Opaque URL-safe Base64 cursor returned by a previous event list response. The
              legacy `page[after]` and flat `page_cursor` forms are also accepted.

          to: Inclusive ISO 8601 end timestamp. When `from` is provided without `to`, defaults
              to `from + 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/email_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email_id": email_id,
                        "event_type": event_type,
                        "from_": from_,
                        "page_size": page_size,
                        "page_cursor": page_cursor,
                        "to": to,
                    },
                    email_event_list_params.EmailEventListParams,
                ),
            ),
            cast_to=EmailEventListResponse,
        )

    def retrieve_stats(
        self,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailEventRetrieveStatsResponse:
        """Returns counts and rates for email events over a time range.

        The default start
        time is 30 days ago.

        Args:
          from_: Inclusive ISO 8601 start timestamp. Defaults to 30 days ago when omitted.

          to: Inclusive ISO 8601 end timestamp. When `from` is provided without `to`, defaults
              to `from + 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/email_events/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    email_event_retrieve_stats_params.EmailEventRetrieveStatsParams,
                ),
            ),
            cast_to=EmailEventRetrieveStatsResponse,
        )


class AsyncEmailEventsResource(AsyncAPIResource):
    """Retrieve account-level email events and event statistics."""

    @cached_property
    def with_raw_response(self) -> AsyncEmailEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        email_id: str | Omit = omit,
        event_type: Union[str, SequenceNotStr[str]] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        page_size: int | Omit = omit,
        page_cursor: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailEventListResponse:
        """
        Lists account-level email events sorted oldest first by
        `occurred_at asc, id asc`. Each row contains a legacy email.-prefixed event_type
        and an additive canonical_event_type. Gateway rejection renders email.failed
        with canonical email.gw_reject; ambiguous injection timeout renders
        email.injection_timeout in both; MTA expiration renders email.bounced with
        canonical email.expired. Message-scoped queued, sending, sandbox, cancelled, and
        daily_limit_exceeded rows fan out per durable recipient with stable derived IDs
        matching webhook delivery. Scheduled is the cardinality exception: account
        polling retains one message-scoped scheduled row with its stored event ID, while
        scheduled webhook publication fans out per recipient with derived IDs; reconcile
        scheduled events by message ID, event type, and occurrence time rather than
        event UUID. Recipient-scoped stored rows retain their stored UUIDs across
        polling and webhook delivery. Legacy names are derived from stored rows; an
        AdminBounce row stored as failed renders email.failed in polling while its
        webhook retains email.bounced, both with canonical email.failed.

        Args:
          email_id: Filter events for a specific email message UUID. Invalid UUID values are
              silently ignored (no filter applied).

          event_type: Comma-separated list of event types to include. Also accepts repeated query
              parameters (e.g. event_type=delivered&event_type=bounced). Unknown values return
              no matches.

              Dual-name compatibility: values are accepted bare or `email.`-prefixed. A legacy
              value keeps matching the rows it matched pre-rename — no widening: `failed` also
              matches the rows that now store the canonical names of the outcomes it covered
              (`gw_reject`, `injection_timeout`, `expired`); `bounced` matches stored
              `bounced` rows only (recipient-scoped Expirations stored `failed` pre-rename and
              never matched `bounced`, so `expired` is deliberately not a `bounced`
              expansion). A canonical value matches its own rows plus legacy rows whose
              recorded payload evidence proves that outcome (`expired` also surfaces legacy
              `bounced` rows with `bounce_category: transient`). The additive
              `canonical_event_type` field in each response row names the canonical outcome.

          from_: Inclusive ISO 8601 start timestamp. Defaults to 30 days ago when omitted.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          page_cursor: Opaque URL-safe Base64 cursor returned by a previous event list response. The
              legacy `page[after]` and flat `page_cursor` forms are also accepted.

          to: Inclusive ISO 8601 end timestamp. When `from` is provided without `to`, defaults
              to `from + 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/email_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email_id": email_id,
                        "event_type": event_type,
                        "from_": from_,
                        "page_size": page_size,
                        "page_cursor": page_cursor,
                        "to": to,
                    },
                    email_event_list_params.EmailEventListParams,
                ),
            ),
            cast_to=EmailEventListResponse,
        )

    async def retrieve_stats(
        self,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailEventRetrieveStatsResponse:
        """Returns counts and rates for email events over a time range.

        The default start
        time is 30 days ago.

        Args:
          from_: Inclusive ISO 8601 start timestamp. Defaults to 30 days ago when omitted.

          to: Inclusive ISO 8601 end timestamp. When `from` is provided without `to`, defaults
              to `from + 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/email_events/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    email_event_retrieve_stats_params.EmailEventRetrieveStatsParams,
                ),
            ),
            cast_to=EmailEventRetrieveStatsResponse,
        )


class EmailEventsResourceWithRawResponse:
    def __init__(self, email_events: EmailEventsResource) -> None:
        self._email_events = email_events

        self.list = to_raw_response_wrapper(
            email_events.list,
        )
        self.retrieve_stats = to_raw_response_wrapper(
            email_events.retrieve_stats,
        )


class AsyncEmailEventsResourceWithRawResponse:
    def __init__(self, email_events: AsyncEmailEventsResource) -> None:
        self._email_events = email_events

        self.list = async_to_raw_response_wrapper(
            email_events.list,
        )
        self.retrieve_stats = async_to_raw_response_wrapper(
            email_events.retrieve_stats,
        )


class EmailEventsResourceWithStreamingResponse:
    def __init__(self, email_events: EmailEventsResource) -> None:
        self._email_events = email_events

        self.list = to_streamed_response_wrapper(
            email_events.list,
        )
        self.retrieve_stats = to_streamed_response_wrapper(
            email_events.retrieve_stats,
        )


class AsyncEmailEventsResourceWithStreamingResponse:
    def __init__(self, email_events: AsyncEmailEventsResource) -> None:
        self._email_events = email_events

        self.list = async_to_streamed_response_wrapper(
            email_events.list,
        )
        self.retrieve_stats = async_to_streamed_response_wrapper(
            email_events.retrieve_stats,
        )
