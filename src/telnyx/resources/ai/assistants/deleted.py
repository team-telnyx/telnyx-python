# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
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
from ....types.ai.assistants import deleted_list_params
from ....types.ai.assistants.deleted_assistant import DeletedAssistant

__all__ = ["DeletedResource", "AsyncDeletedResource"]


class DeletedResource(SyncAPIResource):
    """Configure AI assistant specifications"""

    @cached_property
    def with_raw_response(self) -> DeletedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DeletedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeletedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DeletedResourceWithStreamingResponse(self)

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
    ) -> SyncDefaultFlatPagination[DeletedAssistant]:
        """
        List the organization's soft-deleted assistants in the Recently Deleted list.

        Each entry includes `deleted_at` and `permanently_deleted_at`, the point after
        which the assistant is erased automatically and can no longer be restored.

        Args:
          page_number: Page number to retrieve (1-based).

          page_size: Number of items to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/assistants/deleted",
            page=SyncDefaultFlatPagination[DeletedAssistant],
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
                    deleted_list_params.DeletedListParams,
                ),
            ),
            model=DeletedAssistant,
        )

    def get(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedAssistant:
        """
        Retrieve a soft-deleted assistant from the Recently Deleted list by
        `assistant_id`, including its `deleted_at` and `permanently_deleted_at`
        timestamps. This is a read-only view; the assistant cannot be modified while it
        remains deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            path_template("/ai/assistants/{assistant_id}/deleted", assistant_id=assistant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedAssistant,
        )


class AsyncDeletedResource(AsyncAPIResource):
    """Configure AI assistant specifications"""

    @cached_property
    def with_raw_response(self) -> AsyncDeletedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeletedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeletedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDeletedResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[DeletedAssistant, AsyncDefaultFlatPagination[DeletedAssistant]]:
        """
        List the organization's soft-deleted assistants in the Recently Deleted list.

        Each entry includes `deleted_at` and `permanently_deleted_at`, the point after
        which the assistant is erased automatically and can no longer be restored.

        Args:
          page_number: Page number to retrieve (1-based).

          page_size: Number of items to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/assistants/deleted",
            page=AsyncDefaultFlatPagination[DeletedAssistant],
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
                    deleted_list_params.DeletedListParams,
                ),
            ),
            model=DeletedAssistant,
        )

    async def get(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedAssistant:
        """
        Retrieve a soft-deleted assistant from the Recently Deleted list by
        `assistant_id`, including its `deleted_at` and `permanently_deleted_at`
        timestamps. This is a read-only view; the assistant cannot be modified while it
        remains deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            path_template("/ai/assistants/{assistant_id}/deleted", assistant_id=assistant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedAssistant,
        )


class DeletedResourceWithRawResponse:
    def __init__(self, deleted: DeletedResource) -> None:
        self._deleted = deleted

        self.list = to_raw_response_wrapper(
            deleted.list,
        )
        self.get = to_raw_response_wrapper(
            deleted.get,
        )


class AsyncDeletedResourceWithRawResponse:
    def __init__(self, deleted: AsyncDeletedResource) -> None:
        self._deleted = deleted

        self.list = async_to_raw_response_wrapper(
            deleted.list,
        )
        self.get = async_to_raw_response_wrapper(
            deleted.get,
        )


class DeletedResourceWithStreamingResponse:
    def __init__(self, deleted: DeletedResource) -> None:
        self._deleted = deleted

        self.list = to_streamed_response_wrapper(
            deleted.list,
        )
        self.get = to_streamed_response_wrapper(
            deleted.get,
        )


class AsyncDeletedResourceWithStreamingResponse:
    def __init__(self, deleted: AsyncDeletedResource) -> None:
        self._deleted = deleted

        self.list = async_to_streamed_response_wrapper(
            deleted.list,
        )
        self.get = async_to_streamed_response_wrapper(
            deleted.get,
        )
