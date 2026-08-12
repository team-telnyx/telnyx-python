# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .brands import (
    BrandsResource,
    AsyncBrandsResource,
    BrandsResourceWithRawResponse,
    AsyncBrandsResourceWithRawResponse,
    BrandsResourceWithStreamingResponse,
    AsyncBrandsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .agents.agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)

__all__ = ["RcsResource", "AsyncRcsResource"]


class RcsResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AgentsResource(self._client)

    @cached_property
    def brands(self) -> BrandsResource:
        """Manage the legal business entities that operate RCS agents."""
        return BrandsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RcsResourceWithStreamingResponse(self)


class AsyncRcsResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AsyncAgentsResource(self._client)

    @cached_property
    def brands(self) -> AsyncBrandsResource:
        """Manage the legal business entities that operate RCS agents."""
        return AsyncBrandsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRcsResourceWithStreamingResponse(self)


class RcsResourceWithRawResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AgentsResourceWithRawResponse(self._rcs.agents)

    @cached_property
    def brands(self) -> BrandsResourceWithRawResponse:
        """Manage the legal business entities that operate RCS agents."""
        return BrandsResourceWithRawResponse(self._rcs.brands)


class AsyncRcsResourceWithRawResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AsyncAgentsResourceWithRawResponse(self._rcs.agents)

    @cached_property
    def brands(self) -> AsyncBrandsResourceWithRawResponse:
        """Manage the legal business entities that operate RCS agents."""
        return AsyncBrandsResourceWithRawResponse(self._rcs.brands)


class RcsResourceWithStreamingResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AgentsResourceWithStreamingResponse(self._rcs.agents)

    @cached_property
    def brands(self) -> BrandsResourceWithStreamingResponse:
        """Manage the legal business entities that operate RCS agents."""
        return BrandsResourceWithStreamingResponse(self._rcs.brands)


class AsyncRcsResourceWithStreamingResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AsyncAgentsResourceWithStreamingResponse(self._rcs.agents)

    @cached_property
    def brands(self) -> AsyncBrandsResourceWithStreamingResponse:
        """Manage the legal business entities that operate RCS agents."""
        return AsyncBrandsResourceWithStreamingResponse(self._rcs.brands)
