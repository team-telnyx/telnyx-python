# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TypesafeResource", "AsyncTypesafeResource"]


class TypesafeResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        """
        Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
        """
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> TypesafeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TypesafeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesafeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TypesafeResourceWithStreamingResponse(self)


class AsyncTypesafeResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        """
        Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
        """
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTypesafeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypesafeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesafeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTypesafeResourceWithStreamingResponse(self)


class TypesafeResourceWithRawResponse:
    def __init__(self, typesafe: TypesafeResource) -> None:
        self._typesafe = typesafe

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        """
        Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
        """
        return V1ResourceWithRawResponse(self._typesafe.v1)


class AsyncTypesafeResourceWithRawResponse:
    def __init__(self, typesafe: AsyncTypesafeResource) -> None:
        self._typesafe = typesafe

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        """
        Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
        """
        return AsyncV1ResourceWithRawResponse(self._typesafe.v1)


class TypesafeResourceWithStreamingResponse:
    def __init__(self, typesafe: TypesafeResource) -> None:
        self._typesafe = typesafe

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        """
        Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
        """
        return V1ResourceWithStreamingResponse(self._typesafe.v1)


class AsyncTypesafeResourceWithStreamingResponse:
    def __init__(self, typesafe: AsyncTypesafeResource) -> None:
        self._typesafe = typesafe

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
        """
        return AsyncV1ResourceWithStreamingResponse(self._typesafe.v1)
