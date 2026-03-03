# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import session_analysis_retrieve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.session_analysis_retrieve_response import SessionAnalysisRetrieveResponse

__all__ = ["SessionAnalysisResource", "AsyncSessionAnalysisResource"]


class SessionAnalysisResource(SyncAPIResource):
    """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""

    @cached_property
    def metadata(self) -> MetadataResource:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        return MetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SessionAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SessionAnalysisResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        record_type: str,
        date_time: Union[str, datetime] | Omit = omit,
        expand: Literal["record", "none"] | Omit = omit,
        include_children: bool | Omit = omit,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionAnalysisRetrieveResponse:
        """
        Retrieves a full session analysis tree for a given event, including costs, child
        events, and product linkages.

        Args:
          date_time: ISO 8601 timestamp to narrow index selection for faster lookups.

          expand: Controls what data to expand on each event node.

          include_children: Whether to include child events in the response.

          max_depth: Maximum traversal depth for the event tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_type:
            raise ValueError(f"Expected a non-empty value for `record_type` but received {record_type!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/session_analysis/{record_type}/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_time": date_time,
                        "expand": expand,
                        "include_children": include_children,
                        "max_depth": max_depth,
                    },
                    session_analysis_retrieve_params.SessionAnalysisRetrieveParams,
                ),
            ),
            cast_to=SessionAnalysisRetrieveResponse,
        )


class AsyncSessionAnalysisResource(AsyncAPIResource):
    """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        return AsyncMetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSessionAnalysisResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        record_type: str,
        date_time: Union[str, datetime] | Omit = omit,
        expand: Literal["record", "none"] | Omit = omit,
        include_children: bool | Omit = omit,
        max_depth: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionAnalysisRetrieveResponse:
        """
        Retrieves a full session analysis tree for a given event, including costs, child
        events, and product linkages.

        Args:
          date_time: ISO 8601 timestamp to narrow index selection for faster lookups.

          expand: Controls what data to expand on each event node.

          include_children: Whether to include child events in the response.

          max_depth: Maximum traversal depth for the event tree.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not record_type:
            raise ValueError(f"Expected a non-empty value for `record_type` but received {record_type!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/session_analysis/{record_type}/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_time": date_time,
                        "expand": expand,
                        "include_children": include_children,
                        "max_depth": max_depth,
                    },
                    session_analysis_retrieve_params.SessionAnalysisRetrieveParams,
                ),
            ),
            cast_to=SessionAnalysisRetrieveResponse,
        )


class SessionAnalysisResourceWithRawResponse:
    def __init__(self, session_analysis: SessionAnalysisResource) -> None:
        self._session_analysis = session_analysis

        self.retrieve = to_raw_response_wrapper(
            session_analysis.retrieve,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        return MetadataResourceWithRawResponse(self._session_analysis.metadata)


class AsyncSessionAnalysisResourceWithRawResponse:
    def __init__(self, session_analysis: AsyncSessionAnalysisResource) -> None:
        self._session_analysis = session_analysis

        self.retrieve = async_to_raw_response_wrapper(
            session_analysis.retrieve,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        return AsyncMetadataResourceWithRawResponse(self._session_analysis.metadata)


class SessionAnalysisResourceWithStreamingResponse:
    def __init__(self, session_analysis: SessionAnalysisResource) -> None:
        self._session_analysis = session_analysis

        self.retrieve = to_streamed_response_wrapper(
            session_analysis.retrieve,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        return MetadataResourceWithStreamingResponse(self._session_analysis.metadata)


class AsyncSessionAnalysisResourceWithStreamingResponse:
    def __init__(self, session_analysis: AsyncSessionAnalysisResource) -> None:
        self._session_analysis = session_analysis

        self.retrieve = async_to_streamed_response_wrapper(
            session_analysis.retrieve,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        """Analyze voice AI sessions, costs, and event hierarchies across Telnyx products."""
        return AsyncMetadataResourceWithStreamingResponse(self._session_analysis.metadata)
