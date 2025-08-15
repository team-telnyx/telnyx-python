# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ai.conversations import (
    insight_group_update_params,
    insight_group_insight_groups_params,
    insight_group_retrieve_insight_groups_params,
)
from .....types.ai.conversations.insight_template_group_detail import InsightTemplateGroupDetail
from .....types.ai.conversations.insight_group_retrieve_insight_groups_response import (
    InsightGroupRetrieveInsightGroupsResponse,
)

__all__ = ["InsightGroupsResource", "AsyncInsightGroupsResource"]


class InsightGroupsResource(SyncAPIResource):
    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InsightGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InsightGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InsightGroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightTemplateGroupDetail:
        """
        Get insight group by ID

        Args:
          group_id: The ID of the insight group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            f"/ai/conversations/insight-groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateGroupDetail,
        )

    def update(
        self,
        group_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        webhook: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightTemplateGroupDetail:
        """
        Update an insight template group

        Args:
          group_id: The ID of the insight group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._put(
            f"/ai/conversations/insight-groups/{group_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "webhook": webhook,
                },
                insight_group_update_params.InsightGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateGroupDetail,
        )

    def delete(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete insight group by ID

        Args:
          group_id: The ID of the insight group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            f"/ai/conversations/insight-groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def insight_groups(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        webhook: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightTemplateGroupDetail:
        """
        Create a new insight group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/conversations/insight-groups",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "webhook": webhook,
                },
                insight_group_insight_groups_params.InsightGroupInsightGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateGroupDetail,
        )

    def retrieve_insight_groups(
        self,
        *,
        page: insight_group_retrieve_insight_groups_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightGroupRetrieveInsightGroupsResponse:
        """
        Get all insight groups

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/conversations/insight-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page}, insight_group_retrieve_insight_groups_params.InsightGroupRetrieveInsightGroupsParams
                ),
            ),
            cast_to=InsightGroupRetrieveInsightGroupsResponse,
        )


class AsyncInsightGroupsResource(AsyncAPIResource):
    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInsightGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInsightGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightTemplateGroupDetail:
        """
        Get insight group by ID

        Args:
          group_id: The ID of the insight group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            f"/ai/conversations/insight-groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateGroupDetail,
        )

    async def update(
        self,
        group_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        webhook: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightTemplateGroupDetail:
        """
        Update an insight template group

        Args:
          group_id: The ID of the insight group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._put(
            f"/ai/conversations/insight-groups/{group_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "webhook": webhook,
                },
                insight_group_update_params.InsightGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateGroupDetail,
        )

    async def delete(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete insight group by ID

        Args:
          group_id: The ID of the insight group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            f"/ai/conversations/insight-groups/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def insight_groups(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        webhook: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightTemplateGroupDetail:
        """
        Create a new insight group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/conversations/insight-groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "webhook": webhook,
                },
                insight_group_insight_groups_params.InsightGroupInsightGroupsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsightTemplateGroupDetail,
        )

    async def retrieve_insight_groups(
        self,
        *,
        page: insight_group_retrieve_insight_groups_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightGroupRetrieveInsightGroupsResponse:
        """
        Get all insight groups

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/conversations/insight-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, insight_group_retrieve_insight_groups_params.InsightGroupRetrieveInsightGroupsParams
                ),
            ),
            cast_to=InsightGroupRetrieveInsightGroupsResponse,
        )


class InsightGroupsResourceWithRawResponse:
    def __init__(self, insight_groups: InsightGroupsResource) -> None:
        self._insight_groups = insight_groups

        self.retrieve = to_raw_response_wrapper(
            insight_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            insight_groups.update,
        )
        self.delete = to_raw_response_wrapper(
            insight_groups.delete,
        )
        self.insight_groups = to_raw_response_wrapper(
            insight_groups.insight_groups,
        )
        self.retrieve_insight_groups = to_raw_response_wrapper(
            insight_groups.retrieve_insight_groups,
        )

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._insight_groups.insights)


class AsyncInsightGroupsResourceWithRawResponse:
    def __init__(self, insight_groups: AsyncInsightGroupsResource) -> None:
        self._insight_groups = insight_groups

        self.retrieve = async_to_raw_response_wrapper(
            insight_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            insight_groups.update,
        )
        self.delete = async_to_raw_response_wrapper(
            insight_groups.delete,
        )
        self.insight_groups = async_to_raw_response_wrapper(
            insight_groups.insight_groups,
        )
        self.retrieve_insight_groups = async_to_raw_response_wrapper(
            insight_groups.retrieve_insight_groups,
        )

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._insight_groups.insights)


class InsightGroupsResourceWithStreamingResponse:
    def __init__(self, insight_groups: InsightGroupsResource) -> None:
        self._insight_groups = insight_groups

        self.retrieve = to_streamed_response_wrapper(
            insight_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            insight_groups.update,
        )
        self.delete = to_streamed_response_wrapper(
            insight_groups.delete,
        )
        self.insight_groups = to_streamed_response_wrapper(
            insight_groups.insight_groups,
        )
        self.retrieve_insight_groups = to_streamed_response_wrapper(
            insight_groups.retrieve_insight_groups,
        )

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._insight_groups.insights)


class AsyncInsightGroupsResourceWithStreamingResponse:
    def __init__(self, insight_groups: AsyncInsightGroupsResource) -> None:
        self._insight_groups = insight_groups

        self.retrieve = async_to_streamed_response_wrapper(
            insight_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            insight_groups.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            insight_groups.delete,
        )
        self.insight_groups = async_to_streamed_response_wrapper(
            insight_groups.insight_groups,
        )
        self.retrieve_insight_groups = async_to_streamed_response_wrapper(
            insight_groups.retrieve_insight_groups,
        )

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._insight_groups.insights)
