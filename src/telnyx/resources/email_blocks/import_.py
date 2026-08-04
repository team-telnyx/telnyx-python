# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.email_blocks import import_create_params
from ...types.email_blocks.email_block_import_response import EmailBlockImportResponse

__all__ = ["ImportResource", "AsyncImportResource"]


class ImportResource(SyncAPIResource):
    """Async CSV import of competitor suppression lists."""

    @cached_property
    def with_raw_response(self) -> ImportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ImportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ImportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        block_ttl_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockImportResponse:
        """
        Accepts `multipart/form-data` with a `file` field (the CSV) and an optional
        `block_ttl_days` (integer >0, default 30). Validates:

        - content ≤ 25 MiB, else `413`
        - row count ≤ 250 000, else `413`
        - header-only / all-blank / undetectable provider → `400` Returns `202` with the
          import record (status `pending`); an Oban worker (`EmailBlockImportWorker`,
          max_attempts 3) transitions `pending → processing → completed | failed`.
          `block_ttl_days` applies only to imported `manual_block` rows; other reasons
          get `expires_at: nil`. Provider is auto-detected from the CSV header
          (`sendgrid` / `mailgun` / `ses` / `generic`).

        Args:
          file: The CSV file (Plug.Upload). Missing/non-upload → 400.

          block_ttl_days: TTL for imported `manual_block` rows; other reasons get `expires_at: null`.
              Invalid/missing → falls back to 30.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "block_ttl_days": block_ttl_days,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/email_blocks/import",
            body=maybe_transform(body, import_create_params.ImportCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockImportResponse,
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
    ) -> EmailBlockImportResponse:
        """Account-scoped fetch (cross-account → 404; malformed UUID → 404).

        Nullable
        fields are omitted until terminal: `provider`/`completed_at` when nil;
        `processed_rows`/`created_count`/`existing_count`/ `skipped_count`/`error_count`
        only when `status == completed`; `errors` only when non-empty; `failure_reason`
        only on terminal failure.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_blocks/import/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockImportResponse,
        )


class AsyncImportResource(AsyncAPIResource):
    """Async CSV import of competitor suppression lists."""

    @cached_property
    def with_raw_response(self) -> AsyncImportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncImportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        block_ttl_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockImportResponse:
        """
        Accepts `multipart/form-data` with a `file` field (the CSV) and an optional
        `block_ttl_days` (integer >0, default 30). Validates:

        - content ≤ 25 MiB, else `413`
        - row count ≤ 250 000, else `413`
        - header-only / all-blank / undetectable provider → `400` Returns `202` with the
          import record (status `pending`); an Oban worker (`EmailBlockImportWorker`,
          max_attempts 3) transitions `pending → processing → completed | failed`.
          `block_ttl_days` applies only to imported `manual_block` rows; other reasons
          get `expires_at: nil`. Provider is auto-detected from the CSV header
          (`sendgrid` / `mailgun` / `ses` / `generic`).

        Args:
          file: The CSV file (Plug.Upload). Missing/non-upload → 400.

          block_ttl_days: TTL for imported `manual_block` rows; other reasons get `expires_at: null`.
              Invalid/missing → falls back to 30.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "block_ttl_days": block_ttl_days,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/email_blocks/import",
            body=await async_maybe_transform(body, import_create_params.ImportCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockImportResponse,
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
    ) -> EmailBlockImportResponse:
        """Account-scoped fetch (cross-account → 404; malformed UUID → 404).

        Nullable
        fields are omitted until terminal: `provider`/`completed_at` when nil;
        `processed_rows`/`created_count`/`existing_count`/ `skipped_count`/`error_count`
        only when `status == completed`; `errors` only when non-empty; `failure_reason`
        only on terminal failure.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_blocks/import/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockImportResponse,
        )


class ImportResourceWithRawResponse:
    def __init__(self, import_: ImportResource) -> None:
        self._import_ = import_

        self.create = to_raw_response_wrapper(
            import_.create,
        )
        self.retrieve = to_raw_response_wrapper(
            import_.retrieve,
        )


class AsyncImportResourceWithRawResponse:
    def __init__(self, import_: AsyncImportResource) -> None:
        self._import_ = import_

        self.create = async_to_raw_response_wrapper(
            import_.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            import_.retrieve,
        )


class ImportResourceWithStreamingResponse:
    def __init__(self, import_: ImportResource) -> None:
        self._import_ = import_

        self.create = to_streamed_response_wrapper(
            import_.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            import_.retrieve,
        )


class AsyncImportResourceWithStreamingResponse:
    def __init__(self, import_: AsyncImportResource) -> None:
        self._import_ = import_

        self.create = async_to_streamed_response_wrapper(
            import_.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            import_.retrieve,
        )
