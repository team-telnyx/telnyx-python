# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PhoneNumberBlocksResource", "AsyncPhoneNumberBlocksResource"]


class PhoneNumberBlocksResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        """Background jobs performed over a phone-numbers block's phone numbers"""
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhoneNumberBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumberBlocksResourceWithStreamingResponse(self)


class AsyncPhoneNumberBlocksResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        """Background jobs performed over a phone-numbers block's phone numbers"""
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumberBlocksResourceWithStreamingResponse(self)


class PhoneNumberBlocksResourceWithRawResponse:
    def __init__(self, phone_number_blocks: PhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        """Background jobs performed over a phone-numbers block's phone numbers"""
        return JobsResourceWithRawResponse(self._phone_number_blocks.jobs)


class AsyncPhoneNumberBlocksResourceWithRawResponse:
    def __init__(self, phone_number_blocks: AsyncPhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        """Background jobs performed over a phone-numbers block's phone numbers"""
        return AsyncJobsResourceWithRawResponse(self._phone_number_blocks.jobs)


class PhoneNumberBlocksResourceWithStreamingResponse:
    def __init__(self, phone_number_blocks: PhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        """Background jobs performed over a phone-numbers block's phone numbers"""
        return JobsResourceWithStreamingResponse(self._phone_number_blocks.jobs)


class AsyncPhoneNumberBlocksResourceWithStreamingResponse:
    def __init__(self, phone_number_blocks: AsyncPhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        """Background jobs performed over a phone-numbers block's phone numbers"""
        return AsyncJobsResourceWithStreamingResponse(self._phone_number_blocks.jobs)
