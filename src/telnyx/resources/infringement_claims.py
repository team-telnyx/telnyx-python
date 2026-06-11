# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import infringement_claim_contest_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.infringement_claim_contest_response import InfringementClaimContestResponse
from ..types.infringement_claim_retrieve_response import InfringementClaimRetrieveResponse

__all__ = ["InfringementClaimsResource", "AsyncInfringementClaimsResource"]


class InfringementClaimsResource(SyncAPIResource):
    """Trademark or impersonation claims filed against your DIR.

    Customers may contest a claim with supporting evidence.
    """

    @cached_property
    def with_raw_response(self) -> InfringementClaimsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InfringementClaimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfringementClaimsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InfringementClaimsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        claim_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InfringementClaimRetrieveResponse:
        """Retrieve a single claim by id.

        Returns `404` if the claim does not exist or is
        not against a DIR you own.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not claim_id:
            raise ValueError(f"Expected a non-empty value for `claim_id` but received {claim_id!r}")
        return self._get(
            path_template("/infringement_claims/{claim_id}", claim_id=claim_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfringementClaimRetrieveResponse,
        )

    def contest(
        self,
        claim_id: str,
        *,
        contest_notes: str,
        documents: Iterable[infringement_claim_contest_params.Document] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InfringementClaimContestResponse:
        """Submit a written response and supporting documents disputing the claim.

        The
        first call moves the claim from `pending` to `contested`; subsequent calls
        append supplementary evidence without changing status. The `documents[]` you
        attach are aggregated across rounds in the claim's `contest_documents` field.

        Only `pending` and `contested` claims accept new evidence. A `resolved` claim
        returns `400`.

        Failure modes:

        - `400` - the claim is `resolved` (terminal); cannot be contested further.
        - `404` - the claim does not exist or is not against a DIR you own.
        - `422` - `contest_notes` is too short (< 10 chars), too long (> 2000 chars),
          `documents` is > 20 entries, or a `document_id` is duplicated within the same
          submission.

        Args:
          contest_notes: Customer's response to the claim. 10–2000 characters.

          documents: Up to 20 supporting documents per submission. `document_id` must be unique
              within this submission. Documents are aggregated into the claim's
              `contest_documents` across all submissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not claim_id:
            raise ValueError(f"Expected a non-empty value for `claim_id` but received {claim_id!r}")
        return self._post(
            path_template("/infringement_claims/{claim_id}/contest", claim_id=claim_id),
            body=maybe_transform(
                {
                    "contest_notes": contest_notes,
                    "documents": documents,
                },
                infringement_claim_contest_params.InfringementClaimContestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfringementClaimContestResponse,
        )


class AsyncInfringementClaimsResource(AsyncAPIResource):
    """Trademark or impersonation claims filed against your DIR.

    Customers may contest a claim with supporting evidence.
    """

    @cached_property
    def with_raw_response(self) -> AsyncInfringementClaimsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfringementClaimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfringementClaimsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInfringementClaimsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        claim_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InfringementClaimRetrieveResponse:
        """Retrieve a single claim by id.

        Returns `404` if the claim does not exist or is
        not against a DIR you own.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not claim_id:
            raise ValueError(f"Expected a non-empty value for `claim_id` but received {claim_id!r}")
        return await self._get(
            path_template("/infringement_claims/{claim_id}", claim_id=claim_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfringementClaimRetrieveResponse,
        )

    async def contest(
        self,
        claim_id: str,
        *,
        contest_notes: str,
        documents: Iterable[infringement_claim_contest_params.Document] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InfringementClaimContestResponse:
        """Submit a written response and supporting documents disputing the claim.

        The
        first call moves the claim from `pending` to `contested`; subsequent calls
        append supplementary evidence without changing status. The `documents[]` you
        attach are aggregated across rounds in the claim's `contest_documents` field.

        Only `pending` and `contested` claims accept new evidence. A `resolved` claim
        returns `400`.

        Failure modes:

        - `400` - the claim is `resolved` (terminal); cannot be contested further.
        - `404` - the claim does not exist or is not against a DIR you own.
        - `422` - `contest_notes` is too short (< 10 chars), too long (> 2000 chars),
          `documents` is > 20 entries, or a `document_id` is duplicated within the same
          submission.

        Args:
          contest_notes: Customer's response to the claim. 10–2000 characters.

          documents: Up to 20 supporting documents per submission. `document_id` must be unique
              within this submission. Documents are aggregated into the claim's
              `contest_documents` across all submissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not claim_id:
            raise ValueError(f"Expected a non-empty value for `claim_id` but received {claim_id!r}")
        return await self._post(
            path_template("/infringement_claims/{claim_id}/contest", claim_id=claim_id),
            body=await async_maybe_transform(
                {
                    "contest_notes": contest_notes,
                    "documents": documents,
                },
                infringement_claim_contest_params.InfringementClaimContestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfringementClaimContestResponse,
        )


class InfringementClaimsResourceWithRawResponse:
    def __init__(self, infringement_claims: InfringementClaimsResource) -> None:
        self._infringement_claims = infringement_claims

        self.retrieve = to_raw_response_wrapper(
            infringement_claims.retrieve,
        )
        self.contest = to_raw_response_wrapper(
            infringement_claims.contest,
        )


class AsyncInfringementClaimsResourceWithRawResponse:
    def __init__(self, infringement_claims: AsyncInfringementClaimsResource) -> None:
        self._infringement_claims = infringement_claims

        self.retrieve = async_to_raw_response_wrapper(
            infringement_claims.retrieve,
        )
        self.contest = async_to_raw_response_wrapper(
            infringement_claims.contest,
        )


class InfringementClaimsResourceWithStreamingResponse:
    def __init__(self, infringement_claims: InfringementClaimsResource) -> None:
        self._infringement_claims = infringement_claims

        self.retrieve = to_streamed_response_wrapper(
            infringement_claims.retrieve,
        )
        self.contest = to_streamed_response_wrapper(
            infringement_claims.contest,
        )


class AsyncInfringementClaimsResourceWithStreamingResponse:
    def __init__(self, infringement_claims: AsyncInfringementClaimsResource) -> None:
        self._infringement_claims = infringement_claims

        self.retrieve = async_to_streamed_response_wrapper(
            infringement_claims.retrieve,
        )
        self.contest = async_to_streamed_response_wrapper(
            infringement_claims.contest,
        )
