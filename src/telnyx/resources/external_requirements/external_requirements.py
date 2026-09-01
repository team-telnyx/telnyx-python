# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .sub_number_orders import (
    SubNumberOrdersResource,
    AsyncSubNumberOrdersResource,
    SubNumberOrdersResourceWithRawResponse,
    AsyncSubNumberOrdersResourceWithRawResponse,
    SubNumberOrdersResourceWithStreamingResponse,
    AsyncSubNumberOrdersResourceWithStreamingResponse,
)

__all__ = ["ExternalRequirementsResource", "AsyncExternalRequirementsResource"]


class ExternalRequirementsResource(SyncAPIResource):
    @cached_property
    def sub_number_orders(self) -> SubNumberOrdersResource:
        """Requirement Groups"""
        return SubNumberOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExternalRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ExternalRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ExternalRequirementsResourceWithStreamingResponse(self)


class AsyncExternalRequirementsResource(AsyncAPIResource):
    @cached_property
    def sub_number_orders(self) -> AsyncSubNumberOrdersResource:
        """Requirement Groups"""
        return AsyncSubNumberOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExternalRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncExternalRequirementsResourceWithStreamingResponse(self)


class ExternalRequirementsResourceWithRawResponse:
    def __init__(self, external_requirements: ExternalRequirementsResource) -> None:
        self._external_requirements = external_requirements

    @cached_property
    def sub_number_orders(self) -> SubNumberOrdersResourceWithRawResponse:
        """Requirement Groups"""
        return SubNumberOrdersResourceWithRawResponse(self._external_requirements.sub_number_orders)


class AsyncExternalRequirementsResourceWithRawResponse:
    def __init__(self, external_requirements: AsyncExternalRequirementsResource) -> None:
        self._external_requirements = external_requirements

    @cached_property
    def sub_number_orders(self) -> AsyncSubNumberOrdersResourceWithRawResponse:
        """Requirement Groups"""
        return AsyncSubNumberOrdersResourceWithRawResponse(self._external_requirements.sub_number_orders)


class ExternalRequirementsResourceWithStreamingResponse:
    def __init__(self, external_requirements: ExternalRequirementsResource) -> None:
        self._external_requirements = external_requirements

    @cached_property
    def sub_number_orders(self) -> SubNumberOrdersResourceWithStreamingResponse:
        """Requirement Groups"""
        return SubNumberOrdersResourceWithStreamingResponse(self._external_requirements.sub_number_orders)


class AsyncExternalRequirementsResourceWithStreamingResponse:
    def __init__(self, external_requirements: AsyncExternalRequirementsResource) -> None:
        self._external_requirements = external_requirements

    @cached_property
    def sub_number_orders(self) -> AsyncSubNumberOrdersResourceWithStreamingResponse:
        """Requirement Groups"""
        return AsyncSubNumberOrdersResourceWithStreamingResponse(self._external_requirements.sub_number_orders)
