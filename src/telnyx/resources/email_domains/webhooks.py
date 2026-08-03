# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.email_domains import webhook_list_params, webhook_create_params, webhook_update_params
from ...types.email_domains.email_webhook import EmailWebhook
from ...types.email_domains.email_webhook_event import EmailWebhookEvent
from ...types.email_domains.email_webhook_response import EmailWebhookResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    """Per-domain webhook endpoints with event subscriptions"""

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        domain_id: str,
        *,
        events: List[EmailWebhookEvent],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """
        Creates a webhook endpoint subscribed to a specific allowlist of event types.
        Both `email.*` events (published by email-api) and `email_domain.*` events
        (published by this service) flow through the same webhooks.

        Args:
          events: At least one event type is required.

          url: HTTPS endpoint to deliver subscribed events to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._post(
            path_template("/email_domains/{domain_id}/webhooks", domain_id=domain_id),
            body=maybe_transform(
                {
                    "events": events,
                    "url": url,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        domain_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """
        Retrieve a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_domains/{domain_id}/webhooks/{id}", domain_id=domain_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )

    def update(
        self,
        id: str,
        *,
        domain_id: str,
        events: List[EmailWebhookEvent] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """Update a webhook's URL and/or event subscription.

        A webhook is bound to its
        domain — `domain_id` is not mutable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/email_domains/{domain_id}/webhooks/{id}", domain_id=domain_id, id=id),
            body=maybe_transform(
                {
                    "events": events,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )

    def list(
        self,
        domain_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EmailWebhook]:
        """
        List webhooks for an email domain

        Args:
          page_number: Page number to return (offset pagination)

          page_size: Number of records per page

          sort: Field to sort by. Prefix with `-` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get_api_list(
            path_template("/email_domains/{domain_id}/webhooks", domain_id=domain_id),
            page=SyncDefaultFlatPagination[EmailWebhook],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    webhook_list_params.WebhookListParams,
                ),
            ),
            model=EmailWebhook,
        )

    def delete(
        self,
        id: str,
        *,
        domain_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """
        Delete a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/email_domains/{domain_id}/webhooks/{id}", domain_id=domain_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    """Per-domain webhook endpoints with event subscriptions"""

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        domain_id: str,
        *,
        events: List[EmailWebhookEvent],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """
        Creates a webhook endpoint subscribed to a specific allowlist of event types.
        Both `email.*` events (published by email-api) and `email_domain.*` events
        (published by this service) flow through the same webhooks.

        Args:
          events: At least one event type is required.

          url: HTTPS endpoint to deliver subscribed events to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._post(
            path_template("/email_domains/{domain_id}/webhooks", domain_id=domain_id),
            body=await async_maybe_transform(
                {
                    "events": events,
                    "url": url,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        domain_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """
        Retrieve a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_domains/{domain_id}/webhooks/{id}", domain_id=domain_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )

    async def update(
        self,
        id: str,
        *,
        domain_id: str,
        events: List[EmailWebhookEvent] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """Update a webhook's URL and/or event subscription.

        A webhook is bound to its
        domain — `domain_id` is not mutable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/email_domains/{domain_id}/webhooks/{id}", domain_id=domain_id, id=id),
            body=await async_maybe_transform(
                {
                    "events": events,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )

    def list(
        self,
        domain_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailWebhook, AsyncDefaultFlatPagination[EmailWebhook]]:
        """
        List webhooks for an email domain

        Args:
          page_number: Page number to return (offset pagination)

          page_size: Number of records per page

          sort: Field to sort by. Prefix with `-` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get_api_list(
            path_template("/email_domains/{domain_id}/webhooks", domain_id=domain_id),
            page=AsyncDefaultFlatPagination[EmailWebhook],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    webhook_list_params.WebhookListParams,
                ),
            ),
            model=EmailWebhook,
        )

    async def delete(
        self,
        id: str,
        *,
        domain_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailWebhookResponse:
        """
        Delete a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/email_domains/{domain_id}/webhooks/{id}", domain_id=domain_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailWebhookResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
