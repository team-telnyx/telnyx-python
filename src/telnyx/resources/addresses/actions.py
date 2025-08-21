# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.addresses import action_validate_params, action_accept_suggestions_params
from ...types.addresses.action_validate_response import ActionValidateResponse
from ...types.addresses.action_accept_suggestions_response import ActionAcceptSuggestionsResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def accept_suggestions(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionAcceptSuggestionsResponse:
        """
        Accepts this address suggestion as a new emergency address for Operator Connect
        and finishes the uploads of the numbers associated with it to Microsoft.

        Args:
          body_id: The ID of the address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/addresses/{path_id}/actions/accept_suggestions",
            body=maybe_transform({"body_id": body_id}, action_accept_suggestions_params.ActionAcceptSuggestionsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptSuggestionsResponse,
        )

    def validate(
        self,
        *,
        country_code: str,
        postal_code: str,
        street_address: str,
        administrative_area: str | NotGiven = NOT_GIVEN,
        extended_address: str | NotGiven = NOT_GIVEN,
        locality: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionValidateResponse:
        """
        Validates an address for emergency services.

        Args:
          country_code: The two-character (ISO 3166-1 alpha-2) country code of the address.

          postal_code: The postal code of the address.

          street_address: The primary street address information about the address.

          administrative_area: The locality of the address. For US addresses, this corresponds to the state of
              the address.

          extended_address: Additional street address information about the address such as, but not limited
              to, unit number or apartment number.

          locality: The locality of the address. For US addresses, this corresponds to the city of
              the address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/addresses/actions/validate",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "postal_code": postal_code,
                    "street_address": street_address,
                    "administrative_area": administrative_area,
                    "extended_address": extended_address,
                    "locality": locality,
                },
                action_validate_params.ActionValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionValidateResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def accept_suggestions(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionAcceptSuggestionsResponse:
        """
        Accepts this address suggestion as a new emergency address for Operator Connect
        and finishes the uploads of the numbers associated with it to Microsoft.

        Args:
          body_id: The ID of the address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/addresses/{path_id}/actions/accept_suggestions",
            body=await async_maybe_transform(
                {"body_id": body_id}, action_accept_suggestions_params.ActionAcceptSuggestionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAcceptSuggestionsResponse,
        )

    async def validate(
        self,
        *,
        country_code: str,
        postal_code: str,
        street_address: str,
        administrative_area: str | NotGiven = NOT_GIVEN,
        extended_address: str | NotGiven = NOT_GIVEN,
        locality: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionValidateResponse:
        """
        Validates an address for emergency services.

        Args:
          country_code: The two-character (ISO 3166-1 alpha-2) country code of the address.

          postal_code: The postal code of the address.

          street_address: The primary street address information about the address.

          administrative_area: The locality of the address. For US addresses, this corresponds to the state of
              the address.

          extended_address: Additional street address information about the address such as, but not limited
              to, unit number or apartment number.

          locality: The locality of the address. For US addresses, this corresponds to the city of
              the address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/addresses/actions/validate",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "postal_code": postal_code,
                    "street_address": street_address,
                    "administrative_area": administrative_area,
                    "extended_address": extended_address,
                    "locality": locality,
                },
                action_validate_params.ActionValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionValidateResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.accept_suggestions = to_raw_response_wrapper(
            actions.accept_suggestions,
        )
        self.validate = to_raw_response_wrapper(
            actions.validate,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.accept_suggestions = async_to_raw_response_wrapper(
            actions.accept_suggestions,
        )
        self.validate = async_to_raw_response_wrapper(
            actions.validate,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.accept_suggestions = to_streamed_response_wrapper(
            actions.accept_suggestions,
        )
        self.validate = to_streamed_response_wrapper(
            actions.validate,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.accept_suggestions = async_to_streamed_response_wrapper(
            actions.accept_suggestions,
        )
        self.validate = async_to_streamed_response_wrapper(
            actions.validate,
        )
