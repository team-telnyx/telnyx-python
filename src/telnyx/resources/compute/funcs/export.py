# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ....types.compute.funcs import export_create_params
from ....types.compute.funcs.func_log_export_config_response import FuncLogExportConfigResponse

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        endpoint: str,
        headers: Dict[str, str],
        invocation_export_enabled: bool,
        runtime_export_enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncLogExportConfigResponse:
        """
        Configures the external OTLP endpoint a function's runtime and/or invocation
        logs are pushed to as they happen. This operation is a **full replace, not a
        patch**: `endpoint`, `headers`, `runtime_export_enabled`, and
        `invocation_export_enabled` are all required on every call — omitting any of
        them is a 422, not "keep the current value". Headers are encrypted at rest and
        never returned in any response.

        The endpoint must be an HTTPS URL. When export is configured, new log records
        are converted to OTLP log records and delivered continuously; export never
        bypasses platform log storage, and delivery retries with a bounded policy while
        the destination is unreachable. Only logs generated after configuration are
        exported — there is no historical replay.

        Args:
          endpoint: HTTPS URL to push logs to

          headers: Headers attached to every export push, as key-value pairs (e.g. an auth token
              the collector expects). Required even when empty — {} means "no headers".
              Encrypted at rest; never returned.

          invocation_export_enabled: Export invocation records (one per HTTP request) to this destination

          runtime_export_enabled: Export runtime logs (function stdout/stderr) to this destination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/compute/funcs/{id}/logs/export", id=id),
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "headers": headers,
                    "invocation_export_enabled": invocation_export_enabled,
                    "runtime_export_enabled": runtime_export_enabled,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuncLogExportConfigResponse,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncLogExportConfigResponse:
        """
        Returns the function's configured log export destination and which log types are
        exported. Headers are never returned. Returns 404 (error code 10005) when no
        destination is configured for the function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/compute/funcs/{id}/logs/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuncLogExportConfigResponse,
        )

    def delete_all(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stops exporting a function's logs and removes its destination configuration.
        Idempotent: deleting when nothing is configured succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/compute/funcs/{id}/logs/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        endpoint: str,
        headers: Dict[str, str],
        invocation_export_enabled: bool,
        runtime_export_enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncLogExportConfigResponse:
        """
        Configures the external OTLP endpoint a function's runtime and/or invocation
        logs are pushed to as they happen. This operation is a **full replace, not a
        patch**: `endpoint`, `headers`, `runtime_export_enabled`, and
        `invocation_export_enabled` are all required on every call — omitting any of
        them is a 422, not "keep the current value". Headers are encrypted at rest and
        never returned in any response.

        The endpoint must be an HTTPS URL. When export is configured, new log records
        are converted to OTLP log records and delivered continuously; export never
        bypasses platform log storage, and delivery retries with a bounded policy while
        the destination is unreachable. Only logs generated after configuration are
        exported — there is no historical replay.

        Args:
          endpoint: HTTPS URL to push logs to

          headers: Headers attached to every export push, as key-value pairs (e.g. an auth token
              the collector expects). Required even when empty — {} means "no headers".
              Encrypted at rest; never returned.

          invocation_export_enabled: Export invocation records (one per HTTP request) to this destination

          runtime_export_enabled: Export runtime logs (function stdout/stderr) to this destination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/compute/funcs/{id}/logs/export", id=id),
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "headers": headers,
                    "invocation_export_enabled": invocation_export_enabled,
                    "runtime_export_enabled": runtime_export_enabled,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuncLogExportConfigResponse,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncLogExportConfigResponse:
        """
        Returns the function's configured log export destination and which log types are
        exported. Headers are never returned. Returns 404 (error code 10005) when no
        destination is configured for the function.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/compute/funcs/{id}/logs/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuncLogExportConfigResponse,
        )

    async def delete_all(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stops exporting a function's logs and removes its destination configuration.
        Idempotent: deleting when nothing is configured succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/compute/funcs/{id}/logs/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_raw_response_wrapper(
            export.create,
        )
        self.list = to_raw_response_wrapper(
            export.list,
        )
        self.delete_all = to_raw_response_wrapper(
            export.delete_all,
        )


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_raw_response_wrapper(
            export.create,
        )
        self.list = async_to_raw_response_wrapper(
            export.list,
        )
        self.delete_all = async_to_raw_response_wrapper(
            export.delete_all,
        )


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_streamed_response_wrapper(
            export.create,
        )
        self.list = to_streamed_response_wrapper(
            export.list,
        )
        self.delete_all = to_streamed_response_wrapper(
            export.delete_all,
        )


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_streamed_response_wrapper(
            export.create,
        )
        self.list = async_to_streamed_response_wrapper(
            export.list,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            export.delete_all,
        )
