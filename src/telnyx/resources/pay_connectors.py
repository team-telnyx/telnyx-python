# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    pay_connector_list_params,
    pay_connector_create_params,
    pay_connector_update_params,
)
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
from ..pagination import SyncEmailBracketCursorPagination, AsyncEmailBracketCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.pay_connector import PayConnector
from ..types.pay_connector_response import PayConnectorResponse
from ..types.generic_pay_connector_config_param import GenericPayConnectorConfigParam

__all__ = ["PayConnectorsResource", "AsyncPayConnectorsResource"]


class PayConnectorsResource(SyncAPIResource):
    """Generic payment connector configuration."""

    @cached_property
    def with_raw_response(self) -> PayConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PayConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PayConnectorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: GenericPayConnectorConfigParam,
        name: str,
        mode: Literal["test", "live"] | Omit = omit,
        type: Literal["generic"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayConnectorResponse:
        """Create a generic payment connector in the authenticated organization.

        The name
        must be unique in that organization. Authentication supplies ownership; do not
        send user_id or organization_id. Config is encrypted at rest; passwords and
        tokens are omitted from responses. This operation stores configuration and does
        not initiate a payment. See the
        [processor contract](/docs/voice/programmable-voice/pay#request-sent-to-the-payment-processor).

        Args:
          config: Configuration for a generic connector. A config update replaces the complete
              object, not individual keys. Unknown config keys are discarded. Authentication
              credentials must be nonblank strings when required by the selected auth_type.

          name: Unique within the authenticated organization. Used in resource paths and as
              connector_name in the Call Control Pay request. Cannot be renamed by update.

          mode: Defaults to test on creation. Test restricts collected card numbers but still
              contacts the configured processor; use a processor sandbox URL and sandbox
              credentials. Live removes the test-card restriction. Neither mode locks API
              updates.

          type: Connector type covered by this reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pay_connectors",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "mode": mode,
                    "type": type,
                },
                pay_connector_create_params.PayConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayConnectorResponse,
        )

    def retrieve(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayConnectorResponse:
        """Retrieve a connector by name within the authenticated organization.

        Password and
        token are omitted. A missing name or a connector owned by another organization
        returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/pay_connectors/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayConnectorResponse,
        )

    def update(
        self,
        name: str,
        *,
        config: GenericPayConnectorConfigParam | Omit = omit,
        mode: Literal["test", "live"] | Omit = omit,
        type: Literal["generic"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayConnectorResponse:
        """Update a generic connector by name in the authenticated organization.

        Both test
        and live connectors can be updated through the API. Omitted fields remain
        unchanged. Supplying config replaces the entire config; it does not merge keys.
        Include endpoint_url and the credentials required for the selected auth_type on
        every config replacement. Omitting config preserves existing credentials,
        allowing a mode-only update. The path name cannot be renamed. Public updates use
        PATCH.

        Args:
          config: Configuration for a generic connector. A config update replaces the complete
              object, not individual keys. Unknown config keys are discarded. Authentication
              credentials must be nonblank strings when required by the selected auth_type.

          mode: Omit to preserve the existing mode. Use an explicit test or live value.

          type: Generic connector type. Omit to preserve the existing value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._patch(
            path_template("/pay_connectors/{name}", name=name),
            body=maybe_transform(
                {
                    "config": config,
                    "mode": mode,
                    "type": type,
                },
                pay_connector_update_params.PayConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayConnectorResponse,
        )

    def list(
        self,
        *,
        filter_created_at_eq: str | Omit = omit,
        filter_created_at_gt: str | Omit = omit,
        filter_created_at_gte: str | Omit = omit,
        filter_created_at_lt: str | Omit = omit,
        filter_created_at_lte: str | Omit = omit,
        filter_mode: str | Omit = omit,
        filter_name: str | Omit = omit,
        filter_type: str | Omit = omit,
        filter_updated_at_eq: str | Omit = omit,
        filter_updated_at_gt: str | Omit = omit,
        filter_updated_at_gte: str | Omit = omit,
        filter_updated_at_lt: str | Omit = omit,
        filter_updated_at_lte: str | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_size: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEmailBracketCursorPagination[PayConnector]:
        """
        List connectors belonging to the authenticated organization, including
        connectors created by other users in that organization. Set filter[type]=generic
        to restrict results to the type covered here. Results default to newest
        created_at first. Use meta.end_cursor as page[after] for the next page, or
        meta.start_cursor as page[before] for the preceding page. Omit both cursors for
        the first page; if both are supplied, page[after] takes precedence. Responses
        omit passwords and tokens.

        Args:
          filter_created_at_eq: Equal to this created_at timestamp.

          filter_created_at_gt: After this created_at timestamp.

          filter_created_at_gte: At or after this created_at timestamp.

          filter_created_at_lt: Before this created_at timestamp.

          filter_created_at_lte: At or before this created_at timestamp.

          filter_mode: Exact match on mode.

          filter_name: Exact match on name.

          filter_type: Exact match on type.

          filter_updated_at_eq: Equal to this updated_at timestamp.

          filter_updated_at_gt: After this updated_at timestamp.

          filter_updated_at_gte: At or after this updated_at timestamp.

          filter_updated_at_lt: Before this updated_at timestamp.

          filter_updated_at_lte: At or before this updated_at timestamp.

          page_after: Opaque cursor from meta.end_cursor.

          page_before: Opaque cursor from meta.start_cursor.

          page_size: Number of records per page.

          sort: Comma-separated created_at or updated_at fields, optionally prefixed with - for
              descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pay_connectors",
            page=SyncEmailBracketCursorPagination[PayConnector],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at_eq": filter_created_at_eq,
                        "filter_created_at_gt": filter_created_at_gt,
                        "filter_created_at_gte": filter_created_at_gte,
                        "filter_created_at_lt": filter_created_at_lt,
                        "filter_created_at_lte": filter_created_at_lte,
                        "filter_mode": filter_mode,
                        "filter_name": filter_name,
                        "filter_type": filter_type,
                        "filter_updated_at_eq": filter_updated_at_eq,
                        "filter_updated_at_gt": filter_updated_at_gt,
                        "filter_updated_at_gte": filter_updated_at_gte,
                        "filter_updated_at_lt": filter_updated_at_lt,
                        "filter_updated_at_lte": filter_updated_at_lte,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    pay_connector_list_params.PayConnectorListParams,
                ),
            ),
            model=PayConnector,
        )

    def delete(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a connector by name in the authenticated organization.

        Both test and live
        connectors can be deleted. Returns no response body on success; a missing name
        or a connector in another organization returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/pay_connectors/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPayConnectorsResource(AsyncAPIResource):
    """Generic payment connector configuration."""

    @cached_property
    def with_raw_response(self) -> AsyncPayConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPayConnectorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: GenericPayConnectorConfigParam,
        name: str,
        mode: Literal["test", "live"] | Omit = omit,
        type: Literal["generic"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayConnectorResponse:
        """Create a generic payment connector in the authenticated organization.

        The name
        must be unique in that organization. Authentication supplies ownership; do not
        send user_id or organization_id. Config is encrypted at rest; passwords and
        tokens are omitted from responses. This operation stores configuration and does
        not initiate a payment. See the
        [processor contract](/docs/voice/programmable-voice/pay#request-sent-to-the-payment-processor).

        Args:
          config: Configuration for a generic connector. A config update replaces the complete
              object, not individual keys. Unknown config keys are discarded. Authentication
              credentials must be nonblank strings when required by the selected auth_type.

          name: Unique within the authenticated organization. Used in resource paths and as
              connector_name in the Call Control Pay request. Cannot be renamed by update.

          mode: Defaults to test on creation. Test restricts collected card numbers but still
              contacts the configured processor; use a processor sandbox URL and sandbox
              credentials. Live removes the test-card restriction. Neither mode locks API
              updates.

          type: Connector type covered by this reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pay_connectors",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "mode": mode,
                    "type": type,
                },
                pay_connector_create_params.PayConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayConnectorResponse,
        )

    async def retrieve(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayConnectorResponse:
        """Retrieve a connector by name within the authenticated organization.

        Password and
        token are omitted. A missing name or a connector owned by another organization
        returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/pay_connectors/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayConnectorResponse,
        )

    async def update(
        self,
        name: str,
        *,
        config: GenericPayConnectorConfigParam | Omit = omit,
        mode: Literal["test", "live"] | Omit = omit,
        type: Literal["generic"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayConnectorResponse:
        """Update a generic connector by name in the authenticated organization.

        Both test
        and live connectors can be updated through the API. Omitted fields remain
        unchanged. Supplying config replaces the entire config; it does not merge keys.
        Include endpoint_url and the credentials required for the selected auth_type on
        every config replacement. Omitting config preserves existing credentials,
        allowing a mode-only update. The path name cannot be renamed. Public updates use
        PATCH.

        Args:
          config: Configuration for a generic connector. A config update replaces the complete
              object, not individual keys. Unknown config keys are discarded. Authentication
              credentials must be nonblank strings when required by the selected auth_type.

          mode: Omit to preserve the existing mode. Use an explicit test or live value.

          type: Generic connector type. Omit to preserve the existing value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._patch(
            path_template("/pay_connectors/{name}", name=name),
            body=await async_maybe_transform(
                {
                    "config": config,
                    "mode": mode,
                    "type": type,
                },
                pay_connector_update_params.PayConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayConnectorResponse,
        )

    def list(
        self,
        *,
        filter_created_at_eq: str | Omit = omit,
        filter_created_at_gt: str | Omit = omit,
        filter_created_at_gte: str | Omit = omit,
        filter_created_at_lt: str | Omit = omit,
        filter_created_at_lte: str | Omit = omit,
        filter_mode: str | Omit = omit,
        filter_name: str | Omit = omit,
        filter_type: str | Omit = omit,
        filter_updated_at_eq: str | Omit = omit,
        filter_updated_at_gt: str | Omit = omit,
        filter_updated_at_gte: str | Omit = omit,
        filter_updated_at_lt: str | Omit = omit,
        filter_updated_at_lte: str | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_size: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayConnector, AsyncEmailBracketCursorPagination[PayConnector]]:
        """
        List connectors belonging to the authenticated organization, including
        connectors created by other users in that organization. Set filter[type]=generic
        to restrict results to the type covered here. Results default to newest
        created_at first. Use meta.end_cursor as page[after] for the next page, or
        meta.start_cursor as page[before] for the preceding page. Omit both cursors for
        the first page; if both are supplied, page[after] takes precedence. Responses
        omit passwords and tokens.

        Args:
          filter_created_at_eq: Equal to this created_at timestamp.

          filter_created_at_gt: After this created_at timestamp.

          filter_created_at_gte: At or after this created_at timestamp.

          filter_created_at_lt: Before this created_at timestamp.

          filter_created_at_lte: At or before this created_at timestamp.

          filter_mode: Exact match on mode.

          filter_name: Exact match on name.

          filter_type: Exact match on type.

          filter_updated_at_eq: Equal to this updated_at timestamp.

          filter_updated_at_gt: After this updated_at timestamp.

          filter_updated_at_gte: At or after this updated_at timestamp.

          filter_updated_at_lt: Before this updated_at timestamp.

          filter_updated_at_lte: At or before this updated_at timestamp.

          page_after: Opaque cursor from meta.end_cursor.

          page_before: Opaque cursor from meta.start_cursor.

          page_size: Number of records per page.

          sort: Comma-separated created_at or updated_at fields, optionally prefixed with - for
              descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pay_connectors",
            page=AsyncEmailBracketCursorPagination[PayConnector],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at_eq": filter_created_at_eq,
                        "filter_created_at_gt": filter_created_at_gt,
                        "filter_created_at_gte": filter_created_at_gte,
                        "filter_created_at_lt": filter_created_at_lt,
                        "filter_created_at_lte": filter_created_at_lte,
                        "filter_mode": filter_mode,
                        "filter_name": filter_name,
                        "filter_type": filter_type,
                        "filter_updated_at_eq": filter_updated_at_eq,
                        "filter_updated_at_gt": filter_updated_at_gt,
                        "filter_updated_at_gte": filter_updated_at_gte,
                        "filter_updated_at_lt": filter_updated_at_lt,
                        "filter_updated_at_lte": filter_updated_at_lte,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    pay_connector_list_params.PayConnectorListParams,
                ),
            ),
            model=PayConnector,
        )

    async def delete(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a connector by name in the authenticated organization.

        Both test and live
        connectors can be deleted. Returns no response body on success; a missing name
        or a connector in another organization returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/pay_connectors/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PayConnectorsResourceWithRawResponse:
    def __init__(self, pay_connectors: PayConnectorsResource) -> None:
        self._pay_connectors = pay_connectors

        self.create = to_raw_response_wrapper(
            pay_connectors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pay_connectors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pay_connectors.update,
        )
        self.list = to_raw_response_wrapper(
            pay_connectors.list,
        )
        self.delete = to_raw_response_wrapper(
            pay_connectors.delete,
        )


class AsyncPayConnectorsResourceWithRawResponse:
    def __init__(self, pay_connectors: AsyncPayConnectorsResource) -> None:
        self._pay_connectors = pay_connectors

        self.create = async_to_raw_response_wrapper(
            pay_connectors.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pay_connectors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pay_connectors.update,
        )
        self.list = async_to_raw_response_wrapper(
            pay_connectors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pay_connectors.delete,
        )


class PayConnectorsResourceWithStreamingResponse:
    def __init__(self, pay_connectors: PayConnectorsResource) -> None:
        self._pay_connectors = pay_connectors

        self.create = to_streamed_response_wrapper(
            pay_connectors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pay_connectors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pay_connectors.update,
        )
        self.list = to_streamed_response_wrapper(
            pay_connectors.list,
        )
        self.delete = to_streamed_response_wrapper(
            pay_connectors.delete,
        )


class AsyncPayConnectorsResourceWithStreamingResponse:
    def __init__(self, pay_connectors: AsyncPayConnectorsResource) -> None:
        self._pay_connectors = pay_connectors

        self.create = async_to_streamed_response_wrapper(
            pay_connectors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pay_connectors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pay_connectors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pay_connectors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pay_connectors.delete,
        )
