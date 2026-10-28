# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.browser_sessions import action_create_params
from ...types.browser_sessions.action_create_response import ActionCreateResponse
from ...types.browser_sessions.action_retrieve_response import ActionRetrieveResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """
    Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
    """

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

    @overload
    def create(
        self,
        id: str,
        *,
        type: Literal["navigate"],
        url: str,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        wait_until: Literal["load", "dom_stable", "none"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        type: Literal["observe"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        observation_id: str,
        ref: str,
        type: Literal["click"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait: Literal["no_wait", "dom_stable", "url_change"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        observation_id: str,
        ref: str,
        type: Literal["fill"],
        value: str,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        observation_id: str,
        ref: str,
        type: Literal["select"],
        value: str,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        key: Literal[
            "Enter",
            "Tab",
            "Escape",
            "Backspace",
            "ArrowUp",
            "ArrowDown",
            "ArrowLeft",
            "ArrowRight",
            "PageUp",
            "PageDown",
            "Home",
            "End",
        ],
        type: Literal["press"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        type: Literal["scroll"],
        wait_seconds: int | Omit = omit,
        delta_x: int | Omit = omit,
        delta_y: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        type: Literal["screenshot"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        condition: action_create_params.WaitForActionCondition,
        type: Literal["wait_for"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        actions: Iterable[action_create_params.BatchActionAction],
        type: Literal["batch"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type", "url"],
        ["type"],
        ["observation_id", "ref", "type"],
        ["observation_id", "ref", "type", "value"],
        ["key", "type"],
        ["condition", "type"],
        ["actions", "type"],
    )
    def create(
        self,
        id: str,
        *,
        type: Literal["navigate"]
        | Literal["observe"]
        | Literal["click"]
        | Literal["fill"]
        | Literal["select"]
        | Literal["press"]
        | Literal["scroll"]
        | Literal["screenshot"]
        | Literal["wait_for"]
        | Literal["batch"],
        url: str | Omit = omit,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        wait_until: Literal["load", "dom_stable", "none"] | Omit = omit,
        observation_id: str | Omit = omit,
        ref: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait: Literal["no_wait", "dom_stable", "url_change"] | Omit = omit,
        value: str | Omit = omit,
        key: Literal[
            "Enter",
            "Tab",
            "Escape",
            "Backspace",
            "ArrowUp",
            "ArrowDown",
            "ArrowLeft",
            "ArrowRight",
            "PageUp",
            "PageDown",
            "Home",
            "End",
        ]
        | Omit = omit,
        delta_x: int | Omit = omit,
        delta_y: int | Omit = omit,
        condition: action_create_params.WaitForActionCondition | Omit = omit,
        actions: Iterable[action_create_params.BatchActionAction] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/browser_sessions/{id}/actions", id=id),
            body=maybe_transform(
                {
                    "type": type,
                    "url": url,
                    "idempotency_key": idempotency_key,
                    "include_observation": include_observation,
                    "wait_until": wait_until,
                    "observation_id": observation_id,
                    "ref": ref,
                    "timeout_ms": timeout_ms,
                    "wait": wait,
                    "value": value,
                    "key": key,
                    "delta_x": delta_x,
                    "delta_y": delta_y,
                    "condition": condition,
                    "actions": actions,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait_seconds": wait_seconds}, action_create_params.ActionCreateParams),
            ),
            cast_to=ActionCreateResponse,
        )

    def retrieve(
        self,
        action_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """Returns the stored status and result of an action.

        Use this to poll actions that
        returned 202; HTTP 200 can contain any action status. Stored observations
        contain metadata with empty tree and refs, not the full snapshot; submit a fresh
        observe action to obtain current refs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        return self._get(
            path_template("/browser_sessions/{id}/actions/{action_id}", id=id, action_id=action_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    """
    Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
    """

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

    @overload
    async def create(
        self,
        id: str,
        *,
        type: Literal["navigate"],
        url: str,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        wait_until: Literal["load", "dom_stable", "none"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        type: Literal["observe"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        observation_id: str,
        ref: str,
        type: Literal["click"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait: Literal["no_wait", "dom_stable", "url_change"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        observation_id: str,
        ref: str,
        type: Literal["fill"],
        value: str,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        observation_id: str,
        ref: str,
        type: Literal["select"],
        value: str,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        key: Literal[
            "Enter",
            "Tab",
            "Escape",
            "Backspace",
            "ArrowUp",
            "ArrowDown",
            "ArrowLeft",
            "ArrowRight",
            "PageUp",
            "PageDown",
            "Home",
            "End",
        ],
        type: Literal["press"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        type: Literal["scroll"],
        wait_seconds: int | Omit = omit,
        delta_x: int | Omit = omit,
        delta_y: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        type: Literal["screenshot"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        condition: action_create_params.WaitForActionCondition,
        type: Literal["wait_for"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        actions: Iterable[action_create_params.BatchActionAction],
        type: Literal["batch"],
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        """Executes a browser action on the session.

        Returns 200 if completed within
        wait_seconds, 202 if still in-flight.

        Action types: navigate, observe, click, fill, select, press, scroll, wait_for,
        screenshot, batch.

        Args:
          wait_seconds: Maximum seconds the submission request waits for completion, not an execution
              timeout. If still queued or running, returns 202 without cancelling execution;
              poll the returned action ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type", "url"],
        ["type"],
        ["observation_id", "ref", "type"],
        ["observation_id", "ref", "type", "value"],
        ["key", "type"],
        ["condition", "type"],
        ["actions", "type"],
    )
    async def create(
        self,
        id: str,
        *,
        type: Literal["navigate"]
        | Literal["observe"]
        | Literal["click"]
        | Literal["fill"]
        | Literal["select"]
        | Literal["press"]
        | Literal["scroll"]
        | Literal["screenshot"]
        | Literal["wait_for"]
        | Literal["batch"],
        url: str | Omit = omit,
        wait_seconds: int | Omit = omit,
        idempotency_key: str | Omit = omit,
        include_observation: bool | Omit = omit,
        wait_until: Literal["load", "dom_stable", "none"] | Omit = omit,
        observation_id: str | Omit = omit,
        ref: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait: Literal["no_wait", "dom_stable", "url_change"] | Omit = omit,
        value: str | Omit = omit,
        key: Literal[
            "Enter",
            "Tab",
            "Escape",
            "Backspace",
            "ArrowUp",
            "ArrowDown",
            "ArrowLeft",
            "ArrowRight",
            "PageUp",
            "PageDown",
            "Home",
            "End",
        ]
        | Omit = omit,
        delta_x: int | Omit = omit,
        delta_y: int | Omit = omit,
        condition: action_create_params.WaitForActionCondition | Omit = omit,
        actions: Iterable[action_create_params.BatchActionAction] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionCreateResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/browser_sessions/{id}/actions", id=id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "url": url,
                    "idempotency_key": idempotency_key,
                    "include_observation": include_observation,
                    "wait_until": wait_until,
                    "observation_id": observation_id,
                    "ref": ref,
                    "timeout_ms": timeout_ms,
                    "wait": wait,
                    "value": value,
                    "key": key,
                    "delta_x": delta_x,
                    "delta_y": delta_y,
                    "condition": condition,
                    "actions": actions,
                },
                action_create_params.ActionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"wait_seconds": wait_seconds}, action_create_params.ActionCreateParams
                ),
            ),
            cast_to=ActionCreateResponse,
        )

    async def retrieve(
        self,
        action_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionRetrieveResponse:
        """Returns the stored status and result of an action.

        Use this to poll actions that
        returned 202; HTTP 200 can contain any action status. Stored observations
        contain metadata with empty tree and refs, not the full snapshot; submit a fresh
        observe action to obtain current refs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        return await self._get(
            path_template("/browser_sessions/{id}/actions/{action_id}", id=id, action_id=action_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_raw_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.create = to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.create = async_to_streamed_response_wrapper(
            actions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
