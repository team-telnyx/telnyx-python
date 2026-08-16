# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

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
from ...._base_client import make_request_options
from ....types.storage.sqldbs import action_query_params
from ....types.storage.sqldbs.action_query_response import ActionQueryResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """Manage SQL databases and run SQL against them"""

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def query(
        self,
        id: str,
        *,
        sql: str,
        params: SequenceNotStr[Union[str, float, bool, None]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionQueryResponse:
        """
        Runs SQL against the database and returns the resulting rows — empty for
        statements that return none, such as DDL. Bind positional `?` placeholders with
        `params` rather than interpolating values into the SQL string.

        Args:
          sql: The SQL to run. Use positional `?` placeholders and supply the values in
              `params` rather than interpolating them into this string.

          params: Positional bind parameters, in placeholder order. Each value is a string, a
              number, a boolean, or null; booleans are cast to `1`/`0`. The count must match
              the number of `?` placeholders exactly — a mismatch is rejected with 422 rather
              than binding null for the ones you left out. (Not enforced for multi-statement
              scripts or named parameters, where the placeholder count is not the number
              bound.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/storage/sqldbs/{id}/actions/query", id=id),
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                action_query_params.ActionQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionQueryResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    """Manage SQL databases and run SQL against them"""

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def query(
        self,
        id: str,
        *,
        sql: str,
        params: SequenceNotStr[Union[str, float, bool, None]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionQueryResponse:
        """
        Runs SQL against the database and returns the resulting rows — empty for
        statements that return none, such as DDL. Bind positional `?` placeholders with
        `params` rather than interpolating values into the SQL string.

        Args:
          sql: The SQL to run. Use positional `?` placeholders and supply the values in
              `params` rather than interpolating them into this string.

          params: Positional bind parameters, in placeholder order. Each value is a string, a
              number, a boolean, or null; booleans are cast to `1`/`0`. The count must match
              the number of `?` placeholders exactly — a mismatch is rejected with 422 rather
              than binding null for the ones you left out. (Not enforced for multi-statement
              scripts or named parameters, where the placeholder count is not the number
              bound.)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/storage/sqldbs/{id}/actions/query", id=id),
            body=await async_maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                action_query_params.ActionQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionQueryResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.query = to_raw_response_wrapper(
            actions.query,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.query = async_to_raw_response_wrapper(
            actions.query,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.query = to_streamed_response_wrapper(
            actions.query,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.query = async_to_streamed_response_wrapper(
            actions.query,
        )
