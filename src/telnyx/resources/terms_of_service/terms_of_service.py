# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .number_reputation import (
    NumberReputationResource,
    AsyncNumberReputationResource,
    NumberReputationResourceWithRawResponse,
    AsyncNumberReputationResourceWithRawResponse,
    NumberReputationResourceWithStreamingResponse,
    AsyncNumberReputationResourceWithStreamingResponse,
)

__all__ = ["TermsOfServiceResource", "AsyncTermsOfServiceResource"]


class TermsOfServiceResource(SyncAPIResource):
    @cached_property
    def number_reputation(self) -> NumberReputationResource:
        """Terms of Service agreement endpoints"""
        return NumberReputationResource(self._client)

    @cached_property
    def with_raw_response(self) -> TermsOfServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TermsOfServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TermsOfServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TermsOfServiceResourceWithStreamingResponse(self)


class AsyncTermsOfServiceResource(AsyncAPIResource):
    @cached_property
    def number_reputation(self) -> AsyncNumberReputationResource:
        """Terms of Service agreement endpoints"""
        return AsyncNumberReputationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTermsOfServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTermsOfServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTermsOfServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTermsOfServiceResourceWithStreamingResponse(self)


class TermsOfServiceResourceWithRawResponse:
    def __init__(self, terms_of_service: TermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

    @cached_property
    def number_reputation(self) -> NumberReputationResourceWithRawResponse:
        """Terms of Service agreement endpoints"""
        return NumberReputationResourceWithRawResponse(self._terms_of_service.number_reputation)


class AsyncTermsOfServiceResourceWithRawResponse:
    def __init__(self, terms_of_service: AsyncTermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

    @cached_property
    def number_reputation(self) -> AsyncNumberReputationResourceWithRawResponse:
        """Terms of Service agreement endpoints"""
        return AsyncNumberReputationResourceWithRawResponse(self._terms_of_service.number_reputation)


class TermsOfServiceResourceWithStreamingResponse:
    def __init__(self, terms_of_service: TermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

    @cached_property
    def number_reputation(self) -> NumberReputationResourceWithStreamingResponse:
        """Terms of Service agreement endpoints"""
        return NumberReputationResourceWithStreamingResponse(self._terms_of_service.number_reputation)


class AsyncTermsOfServiceResourceWithStreamingResponse:
    def __init__(self, terms_of_service: AsyncTermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

    @cached_property
    def number_reputation(self) -> AsyncNumberReputationResourceWithStreamingResponse:
        """Terms of Service agreement endpoints"""
        return AsyncNumberReputationResourceWithStreamingResponse(self._terms_of_service.number_reputation)
