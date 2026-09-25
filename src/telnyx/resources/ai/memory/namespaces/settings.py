# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ai.memory.namespaces import setting_patch_all_params
from .....types.ai.memory.namespaces.namespace_settings_response import NamespaceSettingsResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    """How a namespace's summaries are written."""

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def list(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceSettingsResponse:
        """What is currently set for this namespace.

        `instructions: null` means none are
        set and summaries use the neutral default.

        Args:
          namespace: The namespace. `default` exists for every organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get(
            path_template("/ai/memory/namespaces/{namespace}/settings", namespace=namespace),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceSettingsResponse,
        )

    def patch_all(
        self,
        namespace: str,
        *,
        summary: Optional[setting_patch_all_params.Summary] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceSettingsResponse:
        """
        Only the fields you send are changed; anything omitted is left as it is, so `{}`
        changes nothing. Sending `instructions: null`, or an empty or whitespace-only
        string, clears them and returns summaries to the neutral default.

        Instructions are capped at 2000 characters. A longer note is refused rather than
        truncated, because a note cut mid-sentence is a worse steer than none. A change
        reaches each summary the next time that summary is regenerated, not immediately.

        Args:
          namespace: The namespace. `default` exists for every organization.

          summary: A partial update to a namespace's summary settings.

              Only the fields present in the request are changed; the rest are left as they
              are. Sending `instructions: null` (or empty) clears the instructions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._patch(
            path_template("/ai/memory/namespaces/{namespace}/settings", namespace=namespace),
            body=maybe_transform({"summary": summary}, setting_patch_all_params.SettingPatchAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceSettingsResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    """How a namespace's summaries are written."""

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def list(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceSettingsResponse:
        """What is currently set for this namespace.

        `instructions: null` means none are
        set and summaries use the neutral default.

        Args:
          namespace: The namespace. `default` exists for every organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._get(
            path_template("/ai/memory/namespaces/{namespace}/settings", namespace=namespace),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceSettingsResponse,
        )

    async def patch_all(
        self,
        namespace: str,
        *,
        summary: Optional[setting_patch_all_params.Summary] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceSettingsResponse:
        """
        Only the fields you send are changed; anything omitted is left as it is, so `{}`
        changes nothing. Sending `instructions: null`, or an empty or whitespace-only
        string, clears them and returns summaries to the neutral default.

        Instructions are capped at 2000 characters. A longer note is refused rather than
        truncated, because a note cut mid-sentence is a worse steer than none. A change
        reaches each summary the next time that summary is regenerated, not immediately.

        Args:
          namespace: The namespace. `default` exists for every organization.

          summary: A partial update to a namespace's summary settings.

              Only the fields present in the request are changed; the rest are left as they
              are. Sending `instructions: null` (or empty) clears the instructions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return await self._patch(
            path_template("/ai/memory/namespaces/{namespace}/settings", namespace=namespace),
            body=await async_maybe_transform({"summary": summary}, setting_patch_all_params.SettingPatchAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceSettingsResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.list = to_raw_response_wrapper(
            settings.list,
        )
        self.patch_all = to_raw_response_wrapper(
            settings.patch_all,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.list = async_to_raw_response_wrapper(
            settings.list,
        )
        self.patch_all = async_to_raw_response_wrapper(
            settings.patch_all,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.list = to_streamed_response_wrapper(
            settings.list,
        )
        self.patch_all = to_streamed_response_wrapper(
            settings.patch_all,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.list = async_to_streamed_response_wrapper(
            settings.list,
        )
        self.patch_all = async_to_streamed_response_wrapper(
            settings.patch_all,
        )
