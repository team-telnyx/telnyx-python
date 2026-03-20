# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import whatsapp_message_template_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.whatsapp_message_template_update_response import WhatsappMessageTemplateUpdateResponse
from ..types.whatsapp_message_template_retrieve_response import WhatsappMessageTemplateRetrieveResponse

__all__ = ["WhatsappMessageTemplatesResource", "AsyncWhatsappMessageTemplatesResource"]


class WhatsappMessageTemplatesResource(SyncAPIResource):
    """Manage Whatsapp message templates"""

    @cached_property
    def with_raw_response(self) -> WhatsappMessageTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WhatsappMessageTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhatsappMessageTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WhatsappMessageTemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappMessageTemplateRetrieveResponse:
        """
        Get a Whatsapp message template by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v2/whatsapp_message_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappMessageTemplateRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"] | Omit = omit,
        components: Iterable[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappMessageTemplateUpdateResponse:
        """
        Update a Whatsapp message template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v2/whatsapp_message_templates/{id}", id=id),
            body=maybe_transform(
                {
                    "category": category,
                    "components": components,
                },
                whatsapp_message_template_update_params.WhatsappMessageTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappMessageTemplateUpdateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Whatsapp message template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/whatsapp_message_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWhatsappMessageTemplatesResource(AsyncAPIResource):
    """Manage Whatsapp message templates"""

    @cached_property
    def with_raw_response(self) -> AsyncWhatsappMessageTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhatsappMessageTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhatsappMessageTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWhatsappMessageTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappMessageTemplateRetrieveResponse:
        """
        Get a Whatsapp message template by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v2/whatsapp_message_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappMessageTemplateRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"] | Omit = omit,
        components: Iterable[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WhatsappMessageTemplateUpdateResponse:
        """
        Update a Whatsapp message template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v2/whatsapp_message_templates/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "category": category,
                    "components": components,
                },
                whatsapp_message_template_update_params.WhatsappMessageTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhatsappMessageTemplateUpdateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Whatsapp message template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/whatsapp_message_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WhatsappMessageTemplatesResourceWithRawResponse:
    def __init__(self, whatsapp_message_templates: WhatsappMessageTemplatesResource) -> None:
        self._whatsapp_message_templates = whatsapp_message_templates

        self.retrieve = to_raw_response_wrapper(
            whatsapp_message_templates.retrieve,
        )
        self.update = to_raw_response_wrapper(
            whatsapp_message_templates.update,
        )
        self.delete = to_raw_response_wrapper(
            whatsapp_message_templates.delete,
        )


class AsyncWhatsappMessageTemplatesResourceWithRawResponse:
    def __init__(self, whatsapp_message_templates: AsyncWhatsappMessageTemplatesResource) -> None:
        self._whatsapp_message_templates = whatsapp_message_templates

        self.retrieve = async_to_raw_response_wrapper(
            whatsapp_message_templates.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            whatsapp_message_templates.update,
        )
        self.delete = async_to_raw_response_wrapper(
            whatsapp_message_templates.delete,
        )


class WhatsappMessageTemplatesResourceWithStreamingResponse:
    def __init__(self, whatsapp_message_templates: WhatsappMessageTemplatesResource) -> None:
        self._whatsapp_message_templates = whatsapp_message_templates

        self.retrieve = to_streamed_response_wrapper(
            whatsapp_message_templates.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            whatsapp_message_templates.update,
        )
        self.delete = to_streamed_response_wrapper(
            whatsapp_message_templates.delete,
        )


class AsyncWhatsappMessageTemplatesResourceWithStreamingResponse:
    def __init__(self, whatsapp_message_templates: AsyncWhatsappMessageTemplatesResource) -> None:
        self._whatsapp_message_templates = whatsapp_message_templates

        self.retrieve = async_to_streamed_response_wrapper(
            whatsapp_message_templates.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            whatsapp_message_templates.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            whatsapp_message_templates.delete,
        )
