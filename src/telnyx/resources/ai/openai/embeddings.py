# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.openai import embedding_create_params
from ....types.ai.openai.embedding_create_response import EmbeddingCreateResponse
from ....types.ai.openai.embedding_list_models_response import EmbeddingListModelsResponse

__all__ = ["EmbeddingsResource", "AsyncEmbeddingsResource"]


class EmbeddingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmbeddingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        model: str,
        dimensions: int | Omit = omit,
        encoding_format: Literal["float", "base64"] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingCreateResponse:
        """Creates an embedding vector representing the input text.

        This endpoint is
        compatible with the
        [OpenAI Embeddings API](https://platform.openai.com/docs/api-reference/embeddings)
        and may be used with the OpenAI JS or Python SDK by setting the base URL to
        `https://api.telnyx.com/v2/ai/openai`.

        Args:
          input: Input text to embed. Can be a string or array of strings.

          model: ID of the model to use. Use the List embedding models endpoint to see available
              models.

          dimensions: The number of dimensions the resulting output embeddings should have. Only
              supported in some models.

          encoding_format: The format to return the embeddings in.

          user: A unique identifier representing your end-user for monitoring and abuse
              detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/openai/embeddings",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "user": user,
                },
                embedding_create_params.EmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingCreateResponse,
        )

    def list_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingListModelsResponse:
        """Returns a list of available embedding models.

        This endpoint is compatible with
        the OpenAI Models API format.
        """
        return self._get(
            "/ai/openai/embeddings/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingListModelsResponse,
        )


class AsyncEmbeddingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmbeddingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        model: str,
        dimensions: int | Omit = omit,
        encoding_format: Literal["float", "base64"] | Omit = omit,
        user: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingCreateResponse:
        """Creates an embedding vector representing the input text.

        This endpoint is
        compatible with the
        [OpenAI Embeddings API](https://platform.openai.com/docs/api-reference/embeddings)
        and may be used with the OpenAI JS or Python SDK by setting the base URL to
        `https://api.telnyx.com/v2/ai/openai`.

        Args:
          input: Input text to embed. Can be a string or array of strings.

          model: ID of the model to use. Use the List embedding models endpoint to see available
              models.

          dimensions: The number of dimensions the resulting output embeddings should have. Only
              supported in some models.

          encoding_format: The format to return the embeddings in.

          user: A unique identifier representing your end-user for monitoring and abuse
              detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/openai/embeddings",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "user": user,
                },
                embedding_create_params.EmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingCreateResponse,
        )

    async def list_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmbeddingListModelsResponse:
        """Returns a list of available embedding models.

        This endpoint is compatible with
        the OpenAI Models API format.
        """
        return await self._get(
            "/ai/openai/embeddings/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingListModelsResponse,
        )


class EmbeddingsResourceWithRawResponse:
    def __init__(self, embeddings: EmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = to_raw_response_wrapper(
            embeddings.create,
        )
        self.list_models = to_raw_response_wrapper(
            embeddings.list_models,
        )


class AsyncEmbeddingsResourceWithRawResponse:
    def __init__(self, embeddings: AsyncEmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = async_to_raw_response_wrapper(
            embeddings.create,
        )
        self.list_models = async_to_raw_response_wrapper(
            embeddings.list_models,
        )


class EmbeddingsResourceWithStreamingResponse:
    def __init__(self, embeddings: EmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = to_streamed_response_wrapper(
            embeddings.create,
        )
        self.list_models = to_streamed_response_wrapper(
            embeddings.list_models,
        )


class AsyncEmbeddingsResourceWithStreamingResponse:
    def __init__(self, embeddings: AsyncEmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = async_to_streamed_response_wrapper(
            embeddings.create,
        )
        self.list_models = async_to_streamed_response_wrapper(
            embeddings.list_models,
        )
