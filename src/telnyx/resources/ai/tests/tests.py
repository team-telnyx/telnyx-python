# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .schedules.schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from .test_framework.test_framework import (
    TestFrameworkResource,
    AsyncTestFrameworkResource,
    TestFrameworkResourceWithRawResponse,
    AsyncTestFrameworkResourceWithRawResponse,
    TestFrameworkResourceWithStreamingResponse,
    AsyncTestFrameworkResourceWithStreamingResponse,
)

__all__ = ["TestsResource", "AsyncTestsResource"]


class TestsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def schedules(self) -> SchedulesResource:
        return SchedulesResource(self._client)

    @cached_property
    def test_framework(self) -> TestFrameworkResource:
        return TestFrameworkResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TestsResourceWithStreamingResponse(self)


class AsyncTestsResource(AsyncAPIResource):
    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        return AsyncSchedulesResource(self._client)

    @cached_property
    def test_framework(self) -> AsyncTestFrameworkResource:
        return AsyncTestFrameworkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTestsResourceWithStreamingResponse(self)


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self._tests.schedules)

    @cached_property
    def test_framework(self) -> TestFrameworkResourceWithRawResponse:
        return TestFrameworkResourceWithRawResponse(self._tests.test_framework)


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self._tests.schedules)

    @cached_property
    def test_framework(self) -> AsyncTestFrameworkResourceWithRawResponse:
        return AsyncTestFrameworkResourceWithRawResponse(self._tests.test_framework)


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self._tests.schedules)

    @cached_property
    def test_framework(self) -> TestFrameworkResourceWithStreamingResponse:
        return TestFrameworkResourceWithStreamingResponse(self._tests.test_framework)


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self._tests.schedules)

    @cached_property
    def test_framework(self) -> AsyncTestFrameworkResourceWithStreamingResponse:
        return AsyncTestFrameworkResourceWithStreamingResponse(self._tests.test_framework)
