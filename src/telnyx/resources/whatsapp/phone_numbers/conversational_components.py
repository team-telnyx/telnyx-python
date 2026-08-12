# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.whatsapp.phone_numbers import conversational_component_patch_all_params
from ....types.whatsapp.phone_numbers.conversational_component_list_response import ConversationalComponentListResponse
from ....types.whatsapp.phone_numbers.conversational_component_patch_all_response import (
    ConversationalComponentPatchAllResponse,
)

__all__ = ["ConversationalComponentsResource", "AsyncConversationalComponentsResource"]


class ConversationalComponentsResource(SyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> ConversationalComponentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ConversationalComponentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationalComponentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ConversationalComponentsResourceWithStreamingResponse(self)

    def list(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationalComponentListResponse:
        """
        Returns the conversational components configured for the specified WhatsApp
        phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template(
                "/v2/whatsapp/phone_numbers/{phone_number}/conversational_components", phone_number=phone_number
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationalComponentListResponse,
        )

    def patch_all(
        self,
        phone_number: str,
        *,
        commands: Iterable[conversational_component_patch_all_params.Command] | Omit = omit,
        ice_breakers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationalComponentPatchAllResponse:
        """
        Updates the conversational components configured for the specified WhatsApp
        phone number.

        Args:
          commands: List of commands

          ice_breakers: List of ice breakers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._patch(
            path_template(
                "/v2/whatsapp/phone_numbers/{phone_number}/conversational_components", phone_number=phone_number
            ),
            body=maybe_transform(
                {
                    "commands": commands,
                    "ice_breakers": ice_breakers,
                },
                conversational_component_patch_all_params.ConversationalComponentPatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationalComponentPatchAllResponse,
        )


class AsyncConversationalComponentsResource(AsyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> AsyncConversationalComponentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationalComponentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationalComponentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncConversationalComponentsResourceWithStreamingResponse(self)

    async def list(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationalComponentListResponse:
        """
        Returns the conversational components configured for the specified WhatsApp
        phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template(
                "/v2/whatsapp/phone_numbers/{phone_number}/conversational_components", phone_number=phone_number
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationalComponentListResponse,
        )

    async def patch_all(
        self,
        phone_number: str,
        *,
        commands: Iterable[conversational_component_patch_all_params.Command] | Omit = omit,
        ice_breakers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationalComponentPatchAllResponse:
        """
        Updates the conversational components configured for the specified WhatsApp
        phone number.

        Args:
          commands: List of commands

          ice_breakers: List of ice breakers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._patch(
            path_template(
                "/v2/whatsapp/phone_numbers/{phone_number}/conversational_components", phone_number=phone_number
            ),
            body=await async_maybe_transform(
                {
                    "commands": commands,
                    "ice_breakers": ice_breakers,
                },
                conversational_component_patch_all_params.ConversationalComponentPatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationalComponentPatchAllResponse,
        )


class ConversationalComponentsResourceWithRawResponse:
    def __init__(self, conversational_components: ConversationalComponentsResource) -> None:
        self._conversational_components = conversational_components

        self.list = to_raw_response_wrapper(
            conversational_components.list,
        )
        self.patch_all = to_raw_response_wrapper(
            conversational_components.patch_all,
        )


class AsyncConversationalComponentsResourceWithRawResponse:
    def __init__(self, conversational_components: AsyncConversationalComponentsResource) -> None:
        self._conversational_components = conversational_components

        self.list = async_to_raw_response_wrapper(
            conversational_components.list,
        )
        self.patch_all = async_to_raw_response_wrapper(
            conversational_components.patch_all,
        )


class ConversationalComponentsResourceWithStreamingResponse:
    def __init__(self, conversational_components: ConversationalComponentsResource) -> None:
        self._conversational_components = conversational_components

        self.list = to_streamed_response_wrapper(
            conversational_components.list,
        )
        self.patch_all = to_streamed_response_wrapper(
            conversational_components.patch_all,
        )


class AsyncConversationalComponentsResourceWithStreamingResponse:
    def __init__(self, conversational_components: AsyncConversationalComponentsResource) -> None:
        self._conversational_components = conversational_components

        self.list = async_to_streamed_response_wrapper(
            conversational_components.list,
        )
        self.patch_all = async_to_streamed_response_wrapper(
            conversational_components.patch_all,
        )
