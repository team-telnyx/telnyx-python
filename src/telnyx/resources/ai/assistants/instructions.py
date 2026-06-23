# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.assistants import instruction_enhance_params

__all__ = ["InstructionsResource", "AsyncInstructionsResource"]


class InstructionsResource(SyncAPIResource):
    """Configure AI assistant specifications"""

    @cached_property
    def with_raw_response(self) -> InstructionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstructionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return InstructionsResourceWithStreamingResponse(self)

    def enhance(
        self,
        assistant_id: str,
        *,
        enhancement_prompt: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Enhance an assistant's instructions using an LLM.

        The endpoint reads the
        assistant's current instructions and tools, then streams back improved
        instructions as they are generated.

        Optionally provide an `enhancement_prompt` to steer the changes (for example,
        "make the instructions more concise" or "add error handling guidance"). When
        omitted, the assistant's existing instructions are used as the basis for the
        enhancement.

        The enhancement focuses on tool-calling reliability, clarity and precision,
        completeness and error handling, tool schema alignment, and conversation flow
        structure.

        The response is streamed as `text/plain` using chunked transfer encoding;
        consume the body incrementally to render the enhanced instructions as they
        arrive.

        Args:
          enhancement_prompt: Optional guidance describing how the instructions should be enhanced. When
              provided, the LLM applies these requested changes in addition to fixing any
              identified issues.

          instructions: The instructions to enhance. When omitted, the assistant's existing instructions
              are used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            path_template("/ai/assistants/{assistant_id}/instructions/enhance", assistant_id=assistant_id),
            body=maybe_transform(
                {
                    "enhancement_prompt": enhancement_prompt,
                    "instructions": instructions,
                },
                instruction_enhance_params.InstructionEnhanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncInstructionsResource(AsyncAPIResource):
    """Configure AI assistant specifications"""

    @cached_property
    def with_raw_response(self) -> AsyncInstructionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstructionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncInstructionsResourceWithStreamingResponse(self)

    async def enhance(
        self,
        assistant_id: str,
        *,
        enhancement_prompt: Optional[str] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Enhance an assistant's instructions using an LLM.

        The endpoint reads the
        assistant's current instructions and tools, then streams back improved
        instructions as they are generated.

        Optionally provide an `enhancement_prompt` to steer the changes (for example,
        "make the instructions more concise" or "add error handling guidance"). When
        omitted, the assistant's existing instructions are used as the basis for the
        enhancement.

        The enhancement focuses on tool-calling reliability, clarity and precision,
        completeness and error handling, tool schema alignment, and conversation flow
        structure.

        The response is streamed as `text/plain` using chunked transfer encoding;
        consume the body incrementally to render the enhanced instructions as they
        arrive.

        Args:
          enhancement_prompt: Optional guidance describing how the instructions should be enhanced. When
              provided, the LLM applies these requested changes in addition to fixing any
              identified issues.

          instructions: The instructions to enhance. When omitted, the assistant's existing instructions
              are used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            path_template("/ai/assistants/{assistant_id}/instructions/enhance", assistant_id=assistant_id),
            body=await async_maybe_transform(
                {
                    "enhancement_prompt": enhancement_prompt,
                    "instructions": instructions,
                },
                instruction_enhance_params.InstructionEnhanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class InstructionsResourceWithRawResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

        self.enhance = to_raw_response_wrapper(
            instructions.enhance,
        )


class AsyncInstructionsResourceWithRawResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

        self.enhance = async_to_raw_response_wrapper(
            instructions.enhance,
        )


class InstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

        self.enhance = to_streamed_response_wrapper(
            instructions.enhance,
        )


class AsyncInstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

        self.enhance = async_to_streamed_response_wrapper(
            instructions.enhance,
        )
