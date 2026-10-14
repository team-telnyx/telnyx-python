# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.llm_token_gateway import (
    BudgetDuration,
    token_group_list_params,
    token_group_create_params,
    token_group_update_params,
)
from ...types.llm_token_gateway.token_group import TokenGroup
from ...types.llm_token_gateway.budget_duration import BudgetDuration
from ...types.llm_token_gateway.token_group_response import TokenGroupResponse

__all__ = ["TokenGroupsResource", "AsyncTokenGroupsResource"]


class TokenGroupsResource(SyncAPIResource):
    """Manage and report AI Gateway usage."""

    @cached_property
    def with_raw_response(self) -> TokenGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TokenGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TokenGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allowed_models: SequenceNotStr[str],
        name: str,
        idempotency_key: str,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        cache_ttl: Optional[int] | Omit = omit,
        fallbacks: Optional[Dict[str, SequenceNotStr[str]]] | Omit = omit,
        guardrails: Optional[token_group_create_params.Guardrails] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        provider_key_ids: SequenceNotStr[str] | Omit = omit,
        retries: Optional[token_group_create_params.Retries] | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenGroupResponse:
        """Create gateway token group within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response.

        Args:
          fallbacks: Per-group model fallbacks: primary alias -> ordered list of 1..3 other aliases.
              Every key and listed alias must be in allowed_models (a PATCH removing a
              referenced alias is 400); a chain never lists its own key; wildcards are
              rejected. Chains are one level deep (a step's own chain is not expanded).
              Fallback is attempted only for managed routes, only before the first provider
              event is forwarded, and only to steps the key may use; each attempt is reserved
              and recorded. {} and null both disable fallbacks.

          guardrails: Per-group guardrail policy. Missing actions default to ignore. profiles may be
              listed with both dlp actions ignore (staged, inactive) but a non-ignore dlp
              action requires at least one profile. streaming defaults to buffered when any
              response action is block and passthrough otherwise; passthrough with a response
              block is 400. Findings are codes and counts only; content is never stored. The
              stored form is echoed back canonicalised (all actions explicit, profiles
              sorted); {} is stored as an all-ignore policy, null disables.

          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          retries: Per-group same-route retries. max_attempts counts the first try of each step
              (the primary and each fallback) and is the ceiling for the x-ltg-max-attempts
              request header. A step is retried only when its attempt definitely did no
              provider work (connection failure before dispatch, or 429/529) before the first
              provider event; an uncertain failure (timeout, 408/500/502/503/504) moves to the
              next fallback step instead. max_attempts x (1 + the longest fallback chain) must
              not exceed 8, else 400. The n-th retry waits retry_delay_ms (constant),
              retry_delay_ms*n (linear) or retry_delay_ms*2^(n-1) (exponential), at most 5 s
              and never past the request deadline, then jittered uniformly down to half that
              value so concurrent retries spread out; a provider Retry-After of at most 5 s is
              honoured and a longer one moves to the next step. request_timeout_ms applies to
              streaming requests only: it bounds each attempt's time to its first provider
              event and never applies after it. Non-stream requests keep the per-attempt hop
              and idle bounds (their headers arrive only with the finished completion).
              retry_delay_ms and backoff are floors for the request knobs. Each planned
              attempt is reserved (at most 8 per request); unused reservation is released at
              settlement. Managed routes only. The stored form is echoed back with defaults
              filled in; null disables retries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/llm_token_gateway/token_groups",
            body=maybe_transform(
                {
                    "allowed_models": allowed_models,
                    "name": name,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "cache_ttl": cache_ttl,
                    "fallbacks": fallbacks,
                    "guardrails": guardrails,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "provider_key_ids": provider_key_ids,
                    "retries": retries,
                    "rpm_limit": rpm_limit,
                    "tpm_limit": tpm_limit,
                },
                token_group_create_params.TokenGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenGroupResponse,
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
    ) -> TokenGroupResponse:
        """Get gateway token group within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/llm_token_gateway/token_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenGroupResponse,
        )

    def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        if_match: str,
        allowed_models: SequenceNotStr[str] | Omit = omit,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        cache_ttl: Optional[int] | Omit = omit,
        fallbacks: Optional[Dict[str, SequenceNotStr[str]]] | Omit = omit,
        guardrails: Optional[token_group_update_params.Guardrails] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        provider_key_ids: SequenceNotStr[str] | Omit = omit,
        retries: Optional[token_group_update_params.Retries] | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenGroupResponse:
        """Update gateway token group within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response. Omitted fields are preserved.
        Null clears the optional concurrency, fallback and retry settings. A stale
        If-Match returns 412; read the resource again before updating.

        Args:
          fallbacks: Per-group model fallbacks: primary alias -> ordered list of 1..3 other aliases.
              Every key and listed alias must be in allowed_models (a PATCH removing a
              referenced alias is 400); a chain never lists its own key; wildcards are
              rejected. Chains are one level deep (a step's own chain is not expanded).
              Fallback is attempted only for managed routes, only before the first provider
              event is forwarded, and only to steps the key may use; each attempt is reserved
              and recorded. {} and null both disable fallbacks.

          guardrails: Per-group guardrail policy. Missing actions default to ignore. profiles may be
              listed with both dlp actions ignore (staged, inactive) but a non-ignore dlp
              action requires at least one profile. streaming defaults to buffered when any
              response action is block and passthrough otherwise; passthrough with a response
              block is 400. Findings are codes and counts only; content is never stored. The
              stored form is echoed back canonicalised (all actions explicit, profiles
              sorted); {} is stored as an all-ignore policy, null disables.

          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          retries: Per-group same-route retries. max_attempts counts the first try of each step
              (the primary and each fallback) and is the ceiling for the x-ltg-max-attempts
              request header. A step is retried only when its attempt definitely did no
              provider work (connection failure before dispatch, or 429/529) before the first
              provider event; an uncertain failure (timeout, 408/500/502/503/504) moves to the
              next fallback step instead. max_attempts x (1 + the longest fallback chain) must
              not exceed 8, else 400. The n-th retry waits retry_delay_ms (constant),
              retry_delay_ms*n (linear) or retry_delay_ms*2^(n-1) (exponential), at most 5 s
              and never past the request deadline, then jittered uniformly down to half that
              value so concurrent retries spread out; a provider Retry-After of at most 5 s is
              honoured and a longer one moves to the next step. request_timeout_ms applies to
              streaming requests only: it bounds each attempt's time to its first provider
              event and never applies after it. Non-stream requests keep the per-attempt hop
              and idle bounds (their headers arrive only with the finished completion).
              retry_delay_ms and backoff are floors for the request knobs. Each planned
              attempt is reserved (at most 8 per request); unused reservation is released at
              settlement. Managed routes only. The stored form is echoed back with defaults
              filled in; null disables retries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, "If-Match": if_match, **(extra_headers or {})}
        return self._patch(
            path_template("/llm_token_gateway/token_groups/{id}", id=id),
            body=maybe_transform(
                {
                    "allowed_models": allowed_models,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "cache_ttl": cache_ttl,
                    "fallbacks": fallbacks,
                    "guardrails": guardrails,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "name": name,
                    "provider_key_ids": provider_key_ids,
                    "retries": retries,
                    "rpm_limit": rpm_limit,
                    "tpm_limit": tpm_limit,
                },
                token_group_update_params.TokenGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenGroupResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[TokenGroup]:
        """List gateway token groups within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response.

        Args:
          page_snapshot: Required after page 1; account/filter-bound 15-minute stable snapshot;
              expired/mismatch 409.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/llm_token_gateway/token_groups",
            page=SyncDefaultFlatPagination[TokenGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "page_snapshot": page_snapshot,
                    },
                    token_group_list_params.TokenGroupListParams,
                ),
            ),
            model=TokenGroup,
        )

    def delete(
        self,
        id: str,
        *,
        idempotency_key: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revoke resource and its keys atomically; retain historical attribution, never
        detach into an ungoverned service key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Idempotency-Key": idempotency_key, "If-Match": if_match})
        return self._delete(
            path_template("/llm_token_gateway/token_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTokenGroupsResource(AsyncAPIResource):
    """Manage and report AI Gateway usage."""

    @cached_property
    def with_raw_response(self) -> AsyncTokenGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTokenGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allowed_models: SequenceNotStr[str],
        name: str,
        idempotency_key: str,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        cache_ttl: Optional[int] | Omit = omit,
        fallbacks: Optional[Dict[str, SequenceNotStr[str]]] | Omit = omit,
        guardrails: Optional[token_group_create_params.Guardrails] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        provider_key_ids: SequenceNotStr[str] | Omit = omit,
        retries: Optional[token_group_create_params.Retries] | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenGroupResponse:
        """Create gateway token group within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response.

        Args:
          fallbacks: Per-group model fallbacks: primary alias -> ordered list of 1..3 other aliases.
              Every key and listed alias must be in allowed_models (a PATCH removing a
              referenced alias is 400); a chain never lists its own key; wildcards are
              rejected. Chains are one level deep (a step's own chain is not expanded).
              Fallback is attempted only for managed routes, only before the first provider
              event is forwarded, and only to steps the key may use; each attempt is reserved
              and recorded. {} and null both disable fallbacks.

          guardrails: Per-group guardrail policy. Missing actions default to ignore. profiles may be
              listed with both dlp actions ignore (staged, inactive) but a non-ignore dlp
              action requires at least one profile. streaming defaults to buffered when any
              response action is block and passthrough otherwise; passthrough with a response
              block is 400. Findings are codes and counts only; content is never stored. The
              stored form is echoed back canonicalised (all actions explicit, profiles
              sorted); {} is stored as an all-ignore policy, null disables.

          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          retries: Per-group same-route retries. max_attempts counts the first try of each step
              (the primary and each fallback) and is the ceiling for the x-ltg-max-attempts
              request header. A step is retried only when its attempt definitely did no
              provider work (connection failure before dispatch, or 429/529) before the first
              provider event; an uncertain failure (timeout, 408/500/502/503/504) moves to the
              next fallback step instead. max_attempts x (1 + the longest fallback chain) must
              not exceed 8, else 400. The n-th retry waits retry_delay_ms (constant),
              retry_delay_ms*n (linear) or retry_delay_ms*2^(n-1) (exponential), at most 5 s
              and never past the request deadline, then jittered uniformly down to half that
              value so concurrent retries spread out; a provider Retry-After of at most 5 s is
              honoured and a longer one moves to the next step. request_timeout_ms applies to
              streaming requests only: it bounds each attempt's time to its first provider
              event and never applies after it. Non-stream requests keep the per-attempt hop
              and idle bounds (their headers arrive only with the finished completion).
              retry_delay_ms and backoff are floors for the request knobs. Each planned
              attempt is reserved (at most 8 per request); unused reservation is released at
              settlement. Managed routes only. The stored form is echoed back with defaults
              filled in; null disables retries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/llm_token_gateway/token_groups",
            body=await async_maybe_transform(
                {
                    "allowed_models": allowed_models,
                    "name": name,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "cache_ttl": cache_ttl,
                    "fallbacks": fallbacks,
                    "guardrails": guardrails,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "provider_key_ids": provider_key_ids,
                    "retries": retries,
                    "rpm_limit": rpm_limit,
                    "tpm_limit": tpm_limit,
                },
                token_group_create_params.TokenGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenGroupResponse,
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
    ) -> TokenGroupResponse:
        """Get gateway token group within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/llm_token_gateway/token_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenGroupResponse,
        )

    async def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        if_match: str,
        allowed_models: SequenceNotStr[str] | Omit = omit,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        cache_ttl: Optional[int] | Omit = omit,
        fallbacks: Optional[Dict[str, SequenceNotStr[str]]] | Omit = omit,
        guardrails: Optional[token_group_update_params.Guardrails] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        provider_key_ids: SequenceNotStr[str] | Omit = omit,
        retries: Optional[token_group_update_params.Retries] | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenGroupResponse:
        """Update gateway token group within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response. Omitted fields are preserved.
        Null clears the optional concurrency, fallback and retry settings. A stale
        If-Match returns 412; read the resource again before updating.

        Args:
          fallbacks: Per-group model fallbacks: primary alias -> ordered list of 1..3 other aliases.
              Every key and listed alias must be in allowed_models (a PATCH removing a
              referenced alias is 400); a chain never lists its own key; wildcards are
              rejected. Chains are one level deep (a step's own chain is not expanded).
              Fallback is attempted only for managed routes, only before the first provider
              event is forwarded, and only to steps the key may use; each attempt is reserved
              and recorded. {} and null both disable fallbacks.

          guardrails: Per-group guardrail policy. Missing actions default to ignore. profiles may be
              listed with both dlp actions ignore (staged, inactive) but a non-ignore dlp
              action requires at least one profile. streaming defaults to buffered when any
              response action is block and passthrough otherwise; passthrough with a response
              block is 400. Findings are codes and counts only; content is never stored. The
              stored form is echoed back canonicalised (all actions explicit, profiles
              sorted); {} is stored as an all-ignore policy, null disables.

          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          retries: Per-group same-route retries. max_attempts counts the first try of each step
              (the primary and each fallback) and is the ceiling for the x-ltg-max-attempts
              request header. A step is retried only when its attempt definitely did no
              provider work (connection failure before dispatch, or 429/529) before the first
              provider event; an uncertain failure (timeout, 408/500/502/503/504) moves to the
              next fallback step instead. max_attempts x (1 + the longest fallback chain) must
              not exceed 8, else 400. The n-th retry waits retry_delay_ms (constant),
              retry_delay_ms*n (linear) or retry_delay_ms*2^(n-1) (exponential), at most 5 s
              and never past the request deadline, then jittered uniformly down to half that
              value so concurrent retries spread out; a provider Retry-After of at most 5 s is
              honoured and a longer one moves to the next step. request_timeout_ms applies to
              streaming requests only: it bounds each attempt's time to its first provider
              event and never applies after it. Non-stream requests keep the per-attempt hop
              and idle bounds (their headers arrive only with the finished completion).
              retry_delay_ms and backoff are floors for the request knobs. Each planned
              attempt is reserved (at most 8 per request); unused reservation is released at
              settlement. Managed routes only. The stored form is echoed back with defaults
              filled in; null disables retries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, "If-Match": if_match, **(extra_headers or {})}
        return await self._patch(
            path_template("/llm_token_gateway/token_groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "allowed_models": allowed_models,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "cache_ttl": cache_ttl,
                    "fallbacks": fallbacks,
                    "guardrails": guardrails,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "name": name,
                    "provider_key_ids": provider_key_ids,
                    "retries": retries,
                    "rpm_limit": rpm_limit,
                    "tpm_limit": tpm_limit,
                },
                token_group_update_params.TokenGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenGroupResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TokenGroup, AsyncDefaultFlatPagination[TokenGroup]]:
        """List gateway token groups within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response.

        Args:
          page_snapshot: Required after page 1; account/filter-bound 15-minute stable snapshot;
              expired/mismatch 409.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/llm_token_gateway/token_groups",
            page=AsyncDefaultFlatPagination[TokenGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "page_snapshot": page_snapshot,
                    },
                    token_group_list_params.TokenGroupListParams,
                ),
            ),
            model=TokenGroup,
        )

    async def delete(
        self,
        id: str,
        *,
        idempotency_key: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revoke resource and its keys atomically; retain historical attribution, never
        detach into an ungoverned service key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"Idempotency-Key": idempotency_key, "If-Match": if_match})
        return await self._delete(
            path_template("/llm_token_gateway/token_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TokenGroupsResourceWithRawResponse:
    def __init__(self, token_groups: TokenGroupsResource) -> None:
        self._token_groups = token_groups

        self.create = to_raw_response_wrapper(
            token_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            token_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            token_groups.update,
        )
        self.list = to_raw_response_wrapper(
            token_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            token_groups.delete,
        )


class AsyncTokenGroupsResourceWithRawResponse:
    def __init__(self, token_groups: AsyncTokenGroupsResource) -> None:
        self._token_groups = token_groups

        self.create = async_to_raw_response_wrapper(
            token_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            token_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            token_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            token_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            token_groups.delete,
        )


class TokenGroupsResourceWithStreamingResponse:
    def __init__(self, token_groups: TokenGroupsResource) -> None:
        self._token_groups = token_groups

        self.create = to_streamed_response_wrapper(
            token_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            token_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            token_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            token_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            token_groups.delete,
        )


class AsyncTokenGroupsResourceWithStreamingResponse:
    def __init__(self, token_groups: AsyncTokenGroupsResource) -> None:
        self._token_groups = token_groups

        self.create = async_to_streamed_response_wrapper(
            token_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            token_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            token_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            token_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            token_groups.delete,
        )
