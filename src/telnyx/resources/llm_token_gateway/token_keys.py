# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

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
    token_key_list_params,
    token_key_create_params,
    token_key_update_params,
)
from ...types.llm_token_gateway.token_key import TokenKey
from ...types.llm_token_gateway.budget_duration import BudgetDuration
from ...types.llm_token_gateway.token_key_response import TokenKeyResponse

__all__ = ["TokenKeysResource", "AsyncTokenKeysResource"]


class TokenKeysResource(SyncAPIResource):
    """Manage and report AI Gateway usage."""

    @cached_property
    def with_raw_response(self) -> TokenKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TokenKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TokenKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        token_group_id: str,
        idempotency_key: str,
        allowed_models: Optional[SequenceNotStr[str]] | Omit = omit,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        required_end_user_id: bool | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        token_user_id: Optional[str] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenKeyResponse:
        """Create gateway token key within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response. The token secret is returned
        only on the original create response. A replay returns metadata without the
        secret. Provisioning is advisory; ready is not a guarantee of inference
        availability.

        Args:
          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          required_end_user_id: Require a nonempty caller-asserted end-user ID; not proof of identity.

          rpm_limit: Omitted or null defaults to the maximum (6000) (on a blocked key, null is kept
              until the key is unblocked); a value below the minimum (1) or above the maximum
              is rejected with 400 limit_out_of_range; a malformed value (negative, wrong type
              or precision) is 400 invalid_request. Block the key (blocked: true) to deny it;
              blocking is always accepted.

          tpm_limit: Omitted or null defaults to the maximum (10000000) (on a blocked key, null is
              kept until the key is unblocked); a value below the minimum (1) or above the
              maximum is rejected with 400 limit_out_of_range; a malformed value (negative,
              wrong type or precision) is 400 invalid_request. Block the key (blocked: true)
              to deny it; blocking is always accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/llm_token_gateway/token_keys",
            body=maybe_transform(
                {
                    "name": name,
                    "token_group_id": token_group_id,
                    "allowed_models": allowed_models,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "expires_at": expires_at,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "required_end_user_id": required_end_user_id,
                    "rpm_limit": rpm_limit,
                    "token_user_id": token_user_id,
                    "tpm_limit": tpm_limit,
                },
                token_key_create_params.TokenKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenKeyResponse,
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
    ) -> TokenKeyResponse:
        """Get gateway token key within the authenticated Telnyx account.

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
            path_template("/llm_token_gateway/token_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenKeyResponse,
        )

    def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        if_match: str,
        allowed_models: Optional[SequenceNotStr[str]] | Omit = omit,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        required_end_user_id: bool | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenKeyResponse:
        """Update gateway token key within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response. Omitted fields are preserved.
        Null clears max_parallel_requests; null resets budget and rate limits to their
        maximum. A stale If-Match returns 412.

        Args:
          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          required_end_user_id: Require a nonempty caller-asserted end-user ID; not proof of identity. Omission
              preserves the current requirement.

          rpm_limit: Omitted or null defaults to the maximum (6000) (on a blocked key, null is kept
              until the key is unblocked); a value below the minimum (1) or above the maximum
              is rejected with 400 limit_out_of_range; a malformed value (negative, wrong type
              or precision) is 400 invalid_request. Block the key (blocked: true) to deny it;
              blocking is always accepted.

          tpm_limit: Omitted or null defaults to the maximum (10000000) (on a blocked key, null is
              kept until the key is unblocked); a value below the minimum (1) or above the
              maximum is rejected with 400 limit_out_of_range; a malformed value (negative,
              wrong type or precision) is 400 invalid_request. Block the key (blocked: true)
              to deny it; blocking is always accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, "If-Match": if_match, **(extra_headers or {})}
        return self._patch(
            path_template("/llm_token_gateway/token_keys/{id}", id=id),
            body=maybe_transform(
                {
                    "allowed_models": allowed_models,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "expires_at": expires_at,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "name": name,
                    "required_end_user_id": required_end_user_id,
                    "rpm_limit": rpm_limit,
                    "tpm_limit": tpm_limit,
                },
                token_key_update_params.TokenKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenKeyResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        token_group_id: str | Omit = omit,
        token_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[TokenKey]:
        """List gateway token keys within the authenticated Telnyx account.

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
            "/llm_token_gateway/token_keys",
            page=SyncDefaultFlatPagination[TokenKey],
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
                        "token_group_id": token_group_id,
                        "token_user_id": token_user_id,
                    },
                    token_key_list_params.TokenKeyListParams,
                ),
            ),
            model=TokenKey,
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
        """Revoke this token key.

        Acknowledged revocation blocks new admissions with the
        key; requests already admitted may complete. Historical usage attribution is
        retained. Other keys in the group are unchanged.

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
            path_template("/llm_token_gateway/token_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTokenKeysResource(AsyncAPIResource):
    """Manage and report AI Gateway usage."""

    @cached_property
    def with_raw_response(self) -> AsyncTokenKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTokenKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        token_group_id: str,
        idempotency_key: str,
        allowed_models: Optional[SequenceNotStr[str]] | Omit = omit,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        required_end_user_id: bool | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        token_user_id: Optional[str] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenKeyResponse:
        """Create gateway token key within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response. The token secret is returned
        only on the original create response. A replay returns metadata without the
        secret. Provisioning is advisory; ready is not a guarantee of inference
        availability.

        Args:
          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          required_end_user_id: Require a nonempty caller-asserted end-user ID; not proof of identity.

          rpm_limit: Omitted or null defaults to the maximum (6000) (on a blocked key, null is kept
              until the key is unblocked); a value below the minimum (1) or above the maximum
              is rejected with 400 limit_out_of_range; a malformed value (negative, wrong type
              or precision) is 400 invalid_request. Block the key (blocked: true) to deny it;
              blocking is always accepted.

          tpm_limit: Omitted or null defaults to the maximum (10000000) (on a blocked key, null is
              kept until the key is unblocked); a value below the minimum (1) or above the
              maximum is rejected with 400 limit_out_of_range; a malformed value (negative,
              wrong type or precision) is 400 invalid_request. Block the key (blocked: true)
              to deny it; blocking is always accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/llm_token_gateway/token_keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "token_group_id": token_group_id,
                    "allowed_models": allowed_models,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "expires_at": expires_at,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "required_end_user_id": required_end_user_id,
                    "rpm_limit": rpm_limit,
                    "token_user_id": token_user_id,
                    "tpm_limit": tpm_limit,
                },
                token_key_create_params.TokenKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenKeyResponse,
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
    ) -> TokenKeyResponse:
        """Get gateway token key within the authenticated Telnyx account.

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
            path_template("/llm_token_gateway/token_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenKeyResponse,
        )

    async def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        if_match: str,
        allowed_models: Optional[SequenceNotStr[str]] | Omit = omit,
        blocked: bool | Omit = omit,
        budget_duration: Optional[BudgetDuration] | Omit = omit,
        expires_at: Union[str, datetime, None] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        name: str | Omit = omit,
        required_end_user_id: bool | Omit = omit,
        rpm_limit: Optional[int] | Omit = omit,
        tpm_limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenKeyResponse:
        """Update gateway token key within the authenticated Telnyx account.

        Foreign and
        unknown resource IDs return the same 404 response. Omitted fields are preserved.
        Null clears max_parallel_requests; null resets budget and rate limits to their
        maximum. A stale If-Match returns 412.

        Args:
          max_budget: USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
              never binary float accounting.

          max_parallel_requests: Optional maximum concurrent reserved/dispatched cache misses across replicas.
              Null means no concurrency cap. Cache hits do not consume slots; unknown usage
              retains its budget hold without a slot.

          required_end_user_id: Require a nonempty caller-asserted end-user ID; not proof of identity. Omission
              preserves the current requirement.

          rpm_limit: Omitted or null defaults to the maximum (6000) (on a blocked key, null is kept
              until the key is unblocked); a value below the minimum (1) or above the maximum
              is rejected with 400 limit_out_of_range; a malformed value (negative, wrong type
              or precision) is 400 invalid_request. Block the key (blocked: true) to deny it;
              blocking is always accepted.

          tpm_limit: Omitted or null defaults to the maximum (10000000) (on a blocked key, null is
              kept until the key is unblocked); a value below the minimum (1) or above the
              maximum is rejected with 400 limit_out_of_range; a malformed value (negative,
              wrong type or precision) is 400 invalid_request. Block the key (blocked: true)
              to deny it; blocking is always accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, "If-Match": if_match, **(extra_headers or {})}
        return await self._patch(
            path_template("/llm_token_gateway/token_keys/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "allowed_models": allowed_models,
                    "blocked": blocked,
                    "budget_duration": budget_duration,
                    "expires_at": expires_at,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "name": name,
                    "required_end_user_id": required_end_user_id,
                    "rpm_limit": rpm_limit,
                    "tpm_limit": tpm_limit,
                },
                token_key_update_params.TokenKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenKeyResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        token_group_id: str | Omit = omit,
        token_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TokenKey, AsyncDefaultFlatPagination[TokenKey]]:
        """List gateway token keys within the authenticated Telnyx account.

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
            "/llm_token_gateway/token_keys",
            page=AsyncDefaultFlatPagination[TokenKey],
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
                        "token_group_id": token_group_id,
                        "token_user_id": token_user_id,
                    },
                    token_key_list_params.TokenKeyListParams,
                ),
            ),
            model=TokenKey,
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
        """Revoke this token key.

        Acknowledged revocation blocks new admissions with the
        key; requests already admitted may complete. Historical usage attribution is
        retained. Other keys in the group are unchanged.

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
            path_template("/llm_token_gateway/token_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TokenKeysResourceWithRawResponse:
    def __init__(self, token_keys: TokenKeysResource) -> None:
        self._token_keys = token_keys

        self.create = to_raw_response_wrapper(
            token_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            token_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            token_keys.update,
        )
        self.list = to_raw_response_wrapper(
            token_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            token_keys.delete,
        )


class AsyncTokenKeysResourceWithRawResponse:
    def __init__(self, token_keys: AsyncTokenKeysResource) -> None:
        self._token_keys = token_keys

        self.create = async_to_raw_response_wrapper(
            token_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            token_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            token_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            token_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            token_keys.delete,
        )


class TokenKeysResourceWithStreamingResponse:
    def __init__(self, token_keys: TokenKeysResource) -> None:
        self._token_keys = token_keys

        self.create = to_streamed_response_wrapper(
            token_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            token_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            token_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            token_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            token_keys.delete,
        )


class AsyncTokenKeysResourceWithStreamingResponse:
    def __init__(self, token_keys: AsyncTokenKeysResource) -> None:
        self._token_keys = token_keys

        self.create = async_to_streamed_response_wrapper(
            token_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            token_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            token_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            token_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            token_keys.delete,
        )
