# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TestFrameworkResource", "AsyncTestFrameworkResource"]


class TestFrameworkResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def v1(self) -> V1Resource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> TestFrameworkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TestFrameworkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestFrameworkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TestFrameworkResourceWithStreamingResponse(self)


class AsyncTestFrameworkResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestFrameworkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestFrameworkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestFrameworkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTestFrameworkResourceWithStreamingResponse(self)


class TestFrameworkResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_framework: TestFrameworkResource) -> None:
        self._test_framework = test_framework

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return V1ResourceWithRawResponse(self._test_framework.v1)


class AsyncTestFrameworkResourceWithRawResponse:
    def __init__(self, test_framework: AsyncTestFrameworkResource) -> None:
        self._test_framework = test_framework

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncV1ResourceWithRawResponse(self._test_framework.v1)


class TestFrameworkResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_framework: TestFrameworkResource) -> None:
        self._test_framework = test_framework

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return V1ResourceWithStreamingResponse(self._test_framework.v1)


class AsyncTestFrameworkResourceWithStreamingResponse:
    def __init__(self, test_framework: AsyncTestFrameworkResource) -> None:
        self._test_framework = test_framework

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncV1ResourceWithStreamingResponse(self._test_framework.v1)
