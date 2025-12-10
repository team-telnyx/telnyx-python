# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.ai.conversations import insight_list_params, insight_create_params, insight_update_params
from ....types.ai.conversations.insight_template import InsightTemplate
from ....types.ai.conversations.insight_template_detail import InsightTemplateDetail

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        instructions: str,
        name: str,
        json_schema: Union[str, Dict[str, object]] | Omit = omit,
        webhook: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightTemplateDetail:
        """
        Create a new insight

        Args:
          json_schema: If specified, the output will follow the JSON schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/conversations/insights",
            body=maybe_transform(
                {
                    "instructions": instructions,
                    "name": name,
                    "json_schema": json_schema,
                    "webhook": webhook,
                },
                insight_create_params.InsightCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateDetail,
        )

    def retrieve(
        self,
        insight_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightTemplateDetail:
        """
        Get insight by ID

        Args:
          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._get(
            f"/ai/conversations/insights/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateDetail,
        )

    def update(
        self,
        insight_id: str,
        *,
        instructions: str | Omit = omit,
        json_schema: Union[str, Dict[str, object]] | Omit = omit,
        name: str | Omit = omit,
        webhook: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightTemplateDetail:
        """
        Update an insight template

        Args:
          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._put(
            f"/ai/conversations/insights/{insight_id}",
            body=maybe_transform(
                {
                    "instructions": instructions,
                    "json_schema": json_schema,
                    "name": name,
                    "webhook": webhook,
                },
                insight_update_params.InsightUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateDetail,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[InsightTemplate]:
        """
        Get all insights

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/conversations/insights",
            page=SyncDefaultFlatPagination[InsightTemplate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    insight_list_params.InsightListParams,
                ),
            ),
            model=InsightTemplate,
        )

    def delete(
        self,
        insight_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete insight by ID

        Args:
          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/conversations/insights/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        instructions: str,
        name: str,
        json_schema: Union[str, Dict[str, object]] | Omit = omit,
        webhook: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightTemplateDetail:
        """
        Create a new insight

        Args:
          json_schema: If specified, the output will follow the JSON schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/conversations/insights",
            body=await async_maybe_transform(
                {
                    "instructions": instructions,
                    "name": name,
                    "json_schema": json_schema,
                    "webhook": webhook,
                },
                insight_create_params.InsightCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateDetail,
        )

    async def retrieve(
        self,
        insight_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightTemplateDetail:
        """
        Get insight by ID

        Args:
          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._get(
            f"/ai/conversations/insights/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateDetail,
        )

    async def update(
        self,
        insight_id: str,
        *,
        instructions: str | Omit = omit,
        json_schema: Union[str, Dict[str, object]] | Omit = omit,
        name: str | Omit = omit,
        webhook: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightTemplateDetail:
        """
        Update an insight template

        Args:
          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._put(
            f"/ai/conversations/insights/{insight_id}",
            body=await async_maybe_transform(
                {
                    "instructions": instructions,
                    "json_schema": json_schema,
                    "name": name,
                    "webhook": webhook,
                },
                insight_update_params.InsightUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateDetail,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InsightTemplate, AsyncDefaultFlatPagination[InsightTemplate]]:
        """
        Get all insights

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/conversations/insights",
            page=AsyncDefaultFlatPagination[InsightTemplate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    insight_list_params.InsightListParams,
                ),
            ),
            model=InsightTemplate,
        )

    async def delete(
        self,
        insight_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete insight by ID

        Args:
          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/conversations/insights/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.create = to_raw_response_wrapper(
            insights.create,
        )
        self.retrieve = to_raw_response_wrapper(
            insights.retrieve,
        )
        self.update = to_raw_response_wrapper(
            insights.update,
        )
        self.list = to_raw_response_wrapper(
            insights.list,
        )
        self.delete = to_raw_response_wrapper(
            insights.delete,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.create = async_to_raw_response_wrapper(
            insights.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            insights.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            insights.update,
        )
        self.list = async_to_raw_response_wrapper(
            insights.list,
        )
        self.delete = async_to_raw_response_wrapper(
            insights.delete,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.create = to_streamed_response_wrapper(
            insights.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            insights.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            insights.update,
        )
        self.list = to_streamed_response_wrapper(
            insights.list,
        )
        self.delete = to_streamed_response_wrapper(
            insights.delete,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.create = async_to_streamed_response_wrapper(
            insights.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            insights.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            insights.update,
        )
        self.list = async_to_streamed_response_wrapper(
            insights.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            insights.delete,
        )
