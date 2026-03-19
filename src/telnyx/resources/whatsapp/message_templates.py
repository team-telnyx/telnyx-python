# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.whatsapp import message_template_list_params, message_template_create_params
from ...types.whatsapp.message_template_list_response import MessageTemplateListResponse
from ...types.whatsapp.message_template_create_response import MessageTemplateCreateResponse

__all__ = ["MessageTemplatesResource", "AsyncMessageTemplatesResource"]


class MessageTemplatesResource(SyncAPIResource):
    """Manage Whatsapp message templates"""

    @cached_property
    def with_raw_response(self) -> MessageTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessageTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessageTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"],
        components: Iterable[object],
        language: str,
        name: str,
        waba_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTemplateCreateResponse:
        """
        Create a Whatsapp message template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/whatsapp/message_templates",
            body=maybe_transform(
                {
                    "category": category,
                    "components": components,
                    "language": language,
                    "name": name,
                    "waba_id": waba_id,
                },
                message_template_create_params.MessageTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageTemplateCreateResponse,
        )

    def list(
        self,
        *,
        filter_category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"] | Omit = omit,
        filter_search: str | Omit = omit,
        filter_status: str | Omit = omit,
        filter_waba_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[MessageTemplateListResponse]:
        """
        List Whatsapp message templates

        Args:
          filter_category: Filter by category

          filter_search: Search templates by name

          filter_status: Filter by template status

          filter_waba_id: Filter by WABA ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/whatsapp/message_templates",
            page=SyncDefaultFlatPagination[MessageTemplateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_category": filter_category,
                        "filter_search": filter_search,
                        "filter_status": filter_status,
                        "filter_waba_id": filter_waba_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    message_template_list_params.MessageTemplateListParams,
                ),
            ),
            model=MessageTemplateListResponse,
        )


class AsyncMessageTemplatesResource(AsyncAPIResource):
    """Manage Whatsapp message templates"""

    @cached_property
    def with_raw_response(self) -> AsyncMessageTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessageTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessageTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"],
        components: Iterable[object],
        language: str,
        name: str,
        waba_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTemplateCreateResponse:
        """
        Create a Whatsapp message template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/whatsapp/message_templates",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "components": components,
                    "language": language,
                    "name": name,
                    "waba_id": waba_id,
                },
                message_template_create_params.MessageTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageTemplateCreateResponse,
        )

    def list(
        self,
        *,
        filter_category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"] | Omit = omit,
        filter_search: str | Omit = omit,
        filter_status: str | Omit = omit,
        filter_waba_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MessageTemplateListResponse, AsyncDefaultFlatPagination[MessageTemplateListResponse]]:
        """
        List Whatsapp message templates

        Args:
          filter_category: Filter by category

          filter_search: Search templates by name

          filter_status: Filter by template status

          filter_waba_id: Filter by WABA ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/whatsapp/message_templates",
            page=AsyncDefaultFlatPagination[MessageTemplateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_category": filter_category,
                        "filter_search": filter_search,
                        "filter_status": filter_status,
                        "filter_waba_id": filter_waba_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    message_template_list_params.MessageTemplateListParams,
                ),
            ),
            model=MessageTemplateListResponse,
        )


class MessageTemplatesResourceWithRawResponse:
    def __init__(self, message_templates: MessageTemplatesResource) -> None:
        self._message_templates = message_templates

        self.create = to_raw_response_wrapper(
            message_templates.create,
        )
        self.list = to_raw_response_wrapper(
            message_templates.list,
        )


class AsyncMessageTemplatesResourceWithRawResponse:
    def __init__(self, message_templates: AsyncMessageTemplatesResource) -> None:
        self._message_templates = message_templates

        self.create = async_to_raw_response_wrapper(
            message_templates.create,
        )
        self.list = async_to_raw_response_wrapper(
            message_templates.list,
        )


class MessageTemplatesResourceWithStreamingResponse:
    def __init__(self, message_templates: MessageTemplatesResource) -> None:
        self._message_templates = message_templates

        self.create = to_streamed_response_wrapper(
            message_templates.create,
        )
        self.list = to_streamed_response_wrapper(
            message_templates.list,
        )


class AsyncMessageTemplatesResourceWithStreamingResponse:
    def __init__(self, message_templates: AsyncMessageTemplatesResource) -> None:
        self._message_templates = message_templates

        self.create = async_to_streamed_response_wrapper(
            message_templates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            message_templates.list,
        )
