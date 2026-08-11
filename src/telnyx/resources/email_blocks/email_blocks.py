# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    email_block_list_params,
    email_block_create_params,
    email_block_retrieve_events_params,
    email_block_retrieve_export_params,
)
from .import_ import (
    ImportResource,
    AsyncImportResource,
    ImportResourceWithRawResponse,
    AsyncImportResourceWithRawResponse,
    ImportResourceWithStreamingResponse,
    AsyncImportResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_block import EmailBlock
from ...types.email_block_response import EmailBlockResponse
from ...types.email_block_retrieve_events_response import EmailBlockRetrieveEventsResponse

__all__ = ["EmailBlocksResource", "AsyncEmailBlocksResource"]


class EmailBlocksResource(SyncAPIResource):
    """Recipient suppression records (`/v2/email_blocks`)."""

    @cached_property
    def import_(self) -> ImportResource:
        """Async CSV import of competitor suppression lists."""
        return ImportResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailBlocksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        to: str,
        domain_id: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        from_: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """
        Creates a suppression with `reason: manual_block` and `source: manual`.
        Caller-supplied `reason` / `source` are **ignored**; `scope` is **derived**
        server-side from `domain_id` / `from` and is never trusted. Idempotent: if a
        matching row already exists (NULL-safe dedupe key: account_id, scope, to,
        reason, domain_id, from), returns the existing record with `200` (no new audit
        event).

        `bounce_category`, `dsn_code`, `meta`, and `group_id` are **not accepted** on
        the public surface. Use the unsubscribe-group suppression endpoint or the
        internal create surface for those.

        Args:
          to: Recipient address (normalized: trim + lower-case).

          domain_id: `null` ⇒ account scope.

          from_: Sender address (normalized). `null` ⇒ account/domain scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/email_blocks",
            body=maybe_transform(
                {
                    "to": to,
                    "domain_id": domain_id,
                    "expires_at": expires_at,
                    "from_": from_,
                },
                email_block_create_params.EmailBlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """Returns the account-owned suppression identified by ID.

        Cross-account lookups
        and malformed IDs return `404` without exposing another account’s data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_blocks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    def list(
        self,
        *,
        filter_created_after: Union[str, datetime] | Omit = omit,
        filter_created_before: Union[str, datetime] | Omit = omit,
        filter_domain_id: str | Omit = omit,
        filter_reason: Literal["hard_bounce", "spam_complaint", "unsubscribe", "invalid", "manual_block"] | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EmailBlock]:
        """Account-scoped list.

        Two mutually exclusive pagination modes:

        - **Offset**: `page[number]` (default 1) + `page[size]` (default 25, max 100).
          `meta` contains `total_pages`.
        - **Cursor**: `page[after]` and/or `page[before]` (opaque `Base.url_encode64` of
          `{"created_at","id"}`). Cannot combine with `page[number]`; `after`+`before`
          together is an error. `meta` contains `next_cursor` / `previous_cursor`
          (omitted when their flag is false).

        Sort defaults to `-created_at` (desc); only `created_at` is sortable. A `--`
        prefix is an error. `nil`/empty filter values are silently dropped.

        Args:
          filter_created_after: `created_at > value` (ISO 8601).

          filter_created_before: `created_at < value` (ISO 8601).

          filter_domain_id: Exact-match filter on domain_id (UUID).

          filter_reason: Exact-match filter on reason.

          page_after: Opaque cursor (`Base.url_encode64` of `{"created_at","id"}`). Cursor mode;
              mutually exclusive with `page[number]` and `page[before]`.

          page_before: Opaque cursor (see `page[after]`). Mutually exclusive with `page[after]` and
              `page[number]`.

          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          sort: Sort field. Leading `-` = desc; only `created_at` is sortable. Default
              `-created_at`. `--` is an error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_blocks",
            page=SyncDefaultFlatPagination[EmailBlock],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_after": filter_created_after,
                        "filter_created_before": filter_created_before,
                        "filter_domain_id": filter_domain_id,
                        "filter_reason": filter_reason,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    email_block_list_params.EmailBlockListParams,
                ),
            ),
            model=EmailBlock,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """Soft-deletes (status → `removed`; tombstone retained).

        A `removed` audit event
        is appended unless the block was already `removed` (idempotent — returns the
        existing row with `200` and no new event). Mutates `updated_at`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/email_blocks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    def retrieve_events(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockRetrieveEventsResponse:
        """
        Offset pagination only (`page[number]` default 1, `page[size]` default **50**,
        max 100). No `sort`, no `filter`, no cursor — ordering is fixed
        `desc occurred_at, desc id`. Verifies the block belongs to the account first
        (cross-account → 404).

        Args:
          page_number: Offset page number (≥1, default 1).

          page_size: Page size (default 50, max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_blocks/{id}/events", id=id),
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
                    email_block_retrieve_events_params.EmailBlockRetrieveEventsParams,
                ),
            ),
            cast_to=EmailBlockRetrieveEventsResponse,
        )

    def retrieve_export(
        self,
        *,
        filter_created_after: Union[str, datetime] | Omit = omit,
        filter_created_before: Union[str, datetime] | Omit = omit,
        filter_domain_id: str | Omit = omit,
        filter_reason: Literal["hard_bounce", "spam_complaint", "unsubscribe", "invalid", "manual_block"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Streams the account's suppressions as a chunked CSV (server-side cursor; never
        materialized). Content-type `text/csv`, header
        `Content-Disposition: attachment; filename="email_blocks_export.csv"`.

        Filters (`filter[reason]`, `filter[domain_id]`, `filter[created_after]`,
        `filter[created_before]`) are the only params that affect output. `sort` and
        `page[*]` are **parsed** (bad values still produce `400`) but **ignored** — rows
        stream `ORDER BY created_at ASC, id ASC` with no pagination.

        CSV columns:
        `id,to,from,reason,source,scope,status,domain_id, created_at,updated_at,expires_at,group_id`.
        The CSV carries the `group_id` column so group-scoped suppressions' group link
        survives the export (empty for account-scope rows).

        Args:
          filter_created_after: `created_at > value` (ISO 8601).

          filter_created_before: `created_at < value` (ISO 8601).

          filter_domain_id: Exact-match filter on domain_id (UUID).

          filter_reason: Exact-match filter on reason.

          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          sort: Sort field. Leading `-` = desc; only `created_at` is sortable. Default
              `-created_at`. `--` is an error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            "/email_blocks/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_after": filter_created_after,
                        "filter_created_before": filter_created_before,
                        "filter_domain_id": filter_domain_id,
                        "filter_reason": filter_reason,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    email_block_retrieve_export_params.EmailBlockRetrieveExportParams,
                ),
            ),
            cast_to=str,
        )


class AsyncEmailBlocksResource(AsyncAPIResource):
    """Recipient suppression records (`/v2/email_blocks`)."""

    @cached_property
    def import_(self) -> AsyncImportResource:
        """Async CSV import of competitor suppression lists."""
        return AsyncImportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailBlocksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        to: str,
        domain_id: Optional[str] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        from_: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """
        Creates a suppression with `reason: manual_block` and `source: manual`.
        Caller-supplied `reason` / `source` are **ignored**; `scope` is **derived**
        server-side from `domain_id` / `from` and is never trusted. Idempotent: if a
        matching row already exists (NULL-safe dedupe key: account_id, scope, to,
        reason, domain_id, from), returns the existing record with `200` (no new audit
        event).

        `bounce_category`, `dsn_code`, `meta`, and `group_id` are **not accepted** on
        the public surface. Use the unsubscribe-group suppression endpoint or the
        internal create surface for those.

        Args:
          to: Recipient address (normalized: trim + lower-case).

          domain_id: `null` ⇒ account scope.

          from_: Sender address (normalized). `null` ⇒ account/domain scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/email_blocks",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "domain_id": domain_id,
                    "expires_at": expires_at,
                    "from_": from_,
                },
                email_block_create_params.EmailBlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """Returns the account-owned suppression identified by ID.

        Cross-account lookups
        and malformed IDs return `404` without exposing another account’s data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_blocks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    def list(
        self,
        *,
        filter_created_after: Union[str, datetime] | Omit = omit,
        filter_created_before: Union[str, datetime] | Omit = omit,
        filter_domain_id: str | Omit = omit,
        filter_reason: Literal["hard_bounce", "spam_complaint", "unsubscribe", "invalid", "manual_block"] | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailBlock, AsyncDefaultFlatPagination[EmailBlock]]:
        """Account-scoped list.

        Two mutually exclusive pagination modes:

        - **Offset**: `page[number]` (default 1) + `page[size]` (default 25, max 100).
          `meta` contains `total_pages`.
        - **Cursor**: `page[after]` and/or `page[before]` (opaque `Base.url_encode64` of
          `{"created_at","id"}`). Cannot combine with `page[number]`; `after`+`before`
          together is an error. `meta` contains `next_cursor` / `previous_cursor`
          (omitted when their flag is false).

        Sort defaults to `-created_at` (desc); only `created_at` is sortable. A `--`
        prefix is an error. `nil`/empty filter values are silently dropped.

        Args:
          filter_created_after: `created_at > value` (ISO 8601).

          filter_created_before: `created_at < value` (ISO 8601).

          filter_domain_id: Exact-match filter on domain_id (UUID).

          filter_reason: Exact-match filter on reason.

          page_after: Opaque cursor (`Base.url_encode64` of `{"created_at","id"}`). Cursor mode;
              mutually exclusive with `page[number]` and `page[before]`.

          page_before: Opaque cursor (see `page[after]`). Mutually exclusive with `page[after]` and
              `page[number]`.

          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          sort: Sort field. Leading `-` = desc; only `created_at` is sortable. Default
              `-created_at`. `--` is an error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_blocks",
            page=AsyncDefaultFlatPagination[EmailBlock],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_after": filter_created_after,
                        "filter_created_before": filter_created_before,
                        "filter_domain_id": filter_domain_id,
                        "filter_reason": filter_reason,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    email_block_list_params.EmailBlockListParams,
                ),
            ),
            model=EmailBlock,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """Soft-deletes (status → `removed`; tombstone retained).

        A `removed` audit event
        is appended unless the block was already `removed` (idempotent — returns the
        existing row with `200` and no new event). Mutates `updated_at`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/email_blocks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    async def retrieve_events(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockRetrieveEventsResponse:
        """
        Offset pagination only (`page[number]` default 1, `page[size]` default **50**,
        max 100). No `sort`, no `filter`, no cursor — ordering is fixed
        `desc occurred_at, desc id`. Verifies the block belongs to the account first
        (cross-account → 404).

        Args:
          page_number: Offset page number (≥1, default 1).

          page_size: Page size (default 50, max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_blocks/{id}/events", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    email_block_retrieve_events_params.EmailBlockRetrieveEventsParams,
                ),
            ),
            cast_to=EmailBlockRetrieveEventsResponse,
        )

    async def retrieve_export(
        self,
        *,
        filter_created_after: Union[str, datetime] | Omit = omit,
        filter_created_before: Union[str, datetime] | Omit = omit,
        filter_domain_id: str | Omit = omit,
        filter_reason: Literal["hard_bounce", "spam_complaint", "unsubscribe", "invalid", "manual_block"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Streams the account's suppressions as a chunked CSV (server-side cursor; never
        materialized). Content-type `text/csv`, header
        `Content-Disposition: attachment; filename="email_blocks_export.csv"`.

        Filters (`filter[reason]`, `filter[domain_id]`, `filter[created_after]`,
        `filter[created_before]`) are the only params that affect output. `sort` and
        `page[*]` are **parsed** (bad values still produce `400`) but **ignored** — rows
        stream `ORDER BY created_at ASC, id ASC` with no pagination.

        CSV columns:
        `id,to,from,reason,source,scope,status,domain_id, created_at,updated_at,expires_at,group_id`.
        The CSV carries the `group_id` column so group-scoped suppressions' group link
        survives the export (empty for account-scope rows).

        Args:
          filter_created_after: `created_at > value` (ISO 8601).

          filter_created_before: `created_at < value` (ISO 8601).

          filter_domain_id: Exact-match filter on domain_id (UUID).

          filter_reason: Exact-match filter on reason.

          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          sort: Sort field. Leading `-` = desc; only `created_at` is sortable. Default
              `-created_at`. `--` is an error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            "/email_blocks/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_created_after": filter_created_after,
                        "filter_created_before": filter_created_before,
                        "filter_domain_id": filter_domain_id,
                        "filter_reason": filter_reason,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    email_block_retrieve_export_params.EmailBlockRetrieveExportParams,
                ),
            ),
            cast_to=str,
        )


class EmailBlocksResourceWithRawResponse:
    def __init__(self, email_blocks: EmailBlocksResource) -> None:
        self._email_blocks = email_blocks

        self.create = to_raw_response_wrapper(
            email_blocks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_blocks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            email_blocks.list,
        )
        self.delete = to_raw_response_wrapper(
            email_blocks.delete,
        )
        self.retrieve_events = to_raw_response_wrapper(
            email_blocks.retrieve_events,
        )
        self.retrieve_export = to_raw_response_wrapper(
            email_blocks.retrieve_export,
        )

    @cached_property
    def import_(self) -> ImportResourceWithRawResponse:
        """Async CSV import of competitor suppression lists."""
        return ImportResourceWithRawResponse(self._email_blocks.import_)


class AsyncEmailBlocksResourceWithRawResponse:
    def __init__(self, email_blocks: AsyncEmailBlocksResource) -> None:
        self._email_blocks = email_blocks

        self.create = async_to_raw_response_wrapper(
            email_blocks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_blocks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            email_blocks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_blocks.delete,
        )
        self.retrieve_events = async_to_raw_response_wrapper(
            email_blocks.retrieve_events,
        )
        self.retrieve_export = async_to_raw_response_wrapper(
            email_blocks.retrieve_export,
        )

    @cached_property
    def import_(self) -> AsyncImportResourceWithRawResponse:
        """Async CSV import of competitor suppression lists."""
        return AsyncImportResourceWithRawResponse(self._email_blocks.import_)


class EmailBlocksResourceWithStreamingResponse:
    def __init__(self, email_blocks: EmailBlocksResource) -> None:
        self._email_blocks = email_blocks

        self.create = to_streamed_response_wrapper(
            email_blocks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_blocks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            email_blocks.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_blocks.delete,
        )
        self.retrieve_events = to_streamed_response_wrapper(
            email_blocks.retrieve_events,
        )
        self.retrieve_export = to_streamed_response_wrapper(
            email_blocks.retrieve_export,
        )

    @cached_property
    def import_(self) -> ImportResourceWithStreamingResponse:
        """Async CSV import of competitor suppression lists."""
        return ImportResourceWithStreamingResponse(self._email_blocks.import_)


class AsyncEmailBlocksResourceWithStreamingResponse:
    def __init__(self, email_blocks: AsyncEmailBlocksResource) -> None:
        self._email_blocks = email_blocks

        self.create = async_to_streamed_response_wrapper(
            email_blocks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_blocks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            email_blocks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_blocks.delete,
        )
        self.retrieve_events = async_to_streamed_response_wrapper(
            email_blocks.retrieve_events,
        )
        self.retrieve_export = async_to_streamed_response_wrapper(
            email_blocks.retrieve_export,
        )

    @cached_property
    def import_(self) -> AsyncImportResourceWithStreamingResponse:
        """Async CSV import of competitor suppression lists."""
        return AsyncImportResourceWithStreamingResponse(self._email_blocks.import_)
