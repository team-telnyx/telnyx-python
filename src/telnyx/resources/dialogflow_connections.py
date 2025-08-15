# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import dialogflow_connection_create_params, dialogflow_connection_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.dialogflow_connection_create_response import DialogflowConnectionCreateResponse
from ..types.dialogflow_connection_update_response import DialogflowConnectionUpdateResponse
from ..types.dialogflow_connection_retrieve_response import DialogflowConnectionRetrieveResponse

__all__ = ["DialogflowConnectionsResource", "AsyncDialogflowConnectionsResource"]


class DialogflowConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DialogflowConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DialogflowConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DialogflowConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DialogflowConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        connection_id: str,
        *,
        service_account: Dict[str, object],
        conversation_profile_id: str | NotGiven = NOT_GIVEN,
        dialogflow_api: Literal["cx", "es"] | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialogflowConnectionCreateResponse:
        """
        Save Dialogflow Credentiails to Telnyx, so it can be used with other Telnyx
        services.

        Args:
          service_account: The JSON map to connect your Dialoglow account.

          conversation_profile_id: The id of a configured conversation profile on your Dialogflow account. (If you
              use Dialogflow CX, this param is required)

          dialogflow_api: Determine which Dialogflow will be used.

          environment: Which Dialogflow environment will be used.

          location: The region of your agent is. (If you use Dialogflow CX, this param is required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/dialogflow_connections/{connection_id}",
            body=maybe_transform(
                {
                    "service_account": service_account,
                    "conversation_profile_id": conversation_profile_id,
                    "dialogflow_api": dialogflow_api,
                    "environment": environment,
                    "location": location,
                },
                dialogflow_connection_create_params.DialogflowConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialogflowConnectionCreateResponse,
        )

    def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialogflowConnectionRetrieveResponse:
        """
        Return details of the Dialogflow connection associated with the given
        CallControl connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/dialogflow_connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialogflowConnectionRetrieveResponse,
        )

    def update(
        self,
        connection_id: str,
        *,
        service_account: Dict[str, object],
        conversation_profile_id: str | NotGiven = NOT_GIVEN,
        dialogflow_api: Literal["cx", "es"] | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialogflowConnectionUpdateResponse:
        """
        Updates a stored Dialogflow Connection.

        Args:
          service_account: The JSON map to connect your Dialoglow account.

          conversation_profile_id: The id of a configured conversation profile on your Dialogflow account. (If you
              use Dialogflow CX, this param is required)

          dialogflow_api: Determine which Dialogflow will be used.

          environment: Which Dialogflow environment will be used.

          location: The region of your agent is. (If you use Dialogflow CX, this param is required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._put(
            f"/dialogflow_connections/{connection_id}",
            body=maybe_transform(
                {
                    "service_account": service_account,
                    "conversation_profile_id": conversation_profile_id,
                    "dialogflow_api": dialogflow_api,
                    "environment": environment,
                    "location": location,
                },
                dialogflow_connection_update_params.DialogflowConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialogflowConnectionUpdateResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored Dialogflow Connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/dialogflow_connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDialogflowConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDialogflowConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDialogflowConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDialogflowConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDialogflowConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        connection_id: str,
        *,
        service_account: Dict[str, object],
        conversation_profile_id: str | NotGiven = NOT_GIVEN,
        dialogflow_api: Literal["cx", "es"] | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialogflowConnectionCreateResponse:
        """
        Save Dialogflow Credentiails to Telnyx, so it can be used with other Telnyx
        services.

        Args:
          service_account: The JSON map to connect your Dialoglow account.

          conversation_profile_id: The id of a configured conversation profile on your Dialogflow account. (If you
              use Dialogflow CX, this param is required)

          dialogflow_api: Determine which Dialogflow will be used.

          environment: Which Dialogflow environment will be used.

          location: The region of your agent is. (If you use Dialogflow CX, this param is required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/dialogflow_connections/{connection_id}",
            body=await async_maybe_transform(
                {
                    "service_account": service_account,
                    "conversation_profile_id": conversation_profile_id,
                    "dialogflow_api": dialogflow_api,
                    "environment": environment,
                    "location": location,
                },
                dialogflow_connection_create_params.DialogflowConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialogflowConnectionCreateResponse,
        )

    async def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialogflowConnectionRetrieveResponse:
        """
        Return details of the Dialogflow connection associated with the given
        CallControl connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/dialogflow_connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialogflowConnectionRetrieveResponse,
        )

    async def update(
        self,
        connection_id: str,
        *,
        service_account: Dict[str, object],
        conversation_profile_id: str | NotGiven = NOT_GIVEN,
        dialogflow_api: Literal["cx", "es"] | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DialogflowConnectionUpdateResponse:
        """
        Updates a stored Dialogflow Connection.

        Args:
          service_account: The JSON map to connect your Dialoglow account.

          conversation_profile_id: The id of a configured conversation profile on your Dialogflow account. (If you
              use Dialogflow CX, this param is required)

          dialogflow_api: Determine which Dialogflow will be used.

          environment: Which Dialogflow environment will be used.

          location: The region of your agent is. (If you use Dialogflow CX, this param is required)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._put(
            f"/dialogflow_connections/{connection_id}",
            body=await async_maybe_transform(
                {
                    "service_account": service_account,
                    "conversation_profile_id": conversation_profile_id,
                    "dialogflow_api": dialogflow_api,
                    "environment": environment,
                    "location": location,
                },
                dialogflow_connection_update_params.DialogflowConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DialogflowConnectionUpdateResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored Dialogflow Connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/dialogflow_connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DialogflowConnectionsResourceWithRawResponse:
    def __init__(self, dialogflow_connections: DialogflowConnectionsResource) -> None:
        self._dialogflow_connections = dialogflow_connections

        self.create = to_raw_response_wrapper(
            dialogflow_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dialogflow_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dialogflow_connections.update,
        )
        self.delete = to_raw_response_wrapper(
            dialogflow_connections.delete,
        )


class AsyncDialogflowConnectionsResourceWithRawResponse:
    def __init__(self, dialogflow_connections: AsyncDialogflowConnectionsResource) -> None:
        self._dialogflow_connections = dialogflow_connections

        self.create = async_to_raw_response_wrapper(
            dialogflow_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dialogflow_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dialogflow_connections.update,
        )
        self.delete = async_to_raw_response_wrapper(
            dialogflow_connections.delete,
        )


class DialogflowConnectionsResourceWithStreamingResponse:
    def __init__(self, dialogflow_connections: DialogflowConnectionsResource) -> None:
        self._dialogflow_connections = dialogflow_connections

        self.create = to_streamed_response_wrapper(
            dialogflow_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dialogflow_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dialogflow_connections.update,
        )
        self.delete = to_streamed_response_wrapper(
            dialogflow_connections.delete,
        )


class AsyncDialogflowConnectionsResourceWithStreamingResponse:
    def __init__(self, dialogflow_connections: AsyncDialogflowConnectionsResource) -> None:
        self._dialogflow_connections = dialogflow_connections

        self.create = async_to_streamed_response_wrapper(
            dialogflow_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dialogflow_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dialogflow_connections.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            dialogflow_connections.delete,
        )
