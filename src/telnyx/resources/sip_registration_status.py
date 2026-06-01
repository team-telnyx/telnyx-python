# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import sip_registration_status_retrieve_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.sip_registration_status_retrieve_response import SipRegistrationStatusRetrieveResponse

__all__ = ["SipRegistrationStatusResource", "AsyncSipRegistrationStatusResource"]


class SipRegistrationStatusResource(SyncAPIResource):
    """Look up the live SIP registration status of a UAC connection."""

    @cached_property
    def with_raw_response(self) -> SipRegistrationStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SipRegistrationStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SipRegistrationStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SipRegistrationStatusResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        connection_id: str,
        credential_type: Literal["uac_external_credential"],
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipRegistrationStatusRetrieveResponse:
        """
        Returns the live SIP registration state of a UAC connection: whether it is
        currently registered, when it last registered, and the last response Telnyx
        received from the registrar. Only `uac_external_credential` is supported today.

        Args:
          connection_id: Identifier of the UAC connection to look up.

          credential_type: The kind of credential to look up. Only `uac_external_credential` is supported
              today.

          user_id: Owner of the connection. Used to authorize the lookup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sip_registration_status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "credential_type": credential_type,
                        "user_id": user_id,
                    },
                    sip_registration_status_retrieve_params.SipRegistrationStatusRetrieveParams,
                ),
            ),
            cast_to=SipRegistrationStatusRetrieveResponse,
        )


class AsyncSipRegistrationStatusResource(AsyncAPIResource):
    """Look up the live SIP registration status of a UAC connection."""

    @cached_property
    def with_raw_response(self) -> AsyncSipRegistrationStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSipRegistrationStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSipRegistrationStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSipRegistrationStatusResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        connection_id: str,
        credential_type: Literal["uac_external_credential"],
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipRegistrationStatusRetrieveResponse:
        """
        Returns the live SIP registration state of a UAC connection: whether it is
        currently registered, when it last registered, and the last response Telnyx
        received from the registrar. Only `uac_external_credential` is supported today.

        Args:
          connection_id: Identifier of the UAC connection to look up.

          credential_type: The kind of credential to look up. Only `uac_external_credential` is supported
              today.

          user_id: Owner of the connection. Used to authorize the lookup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sip_registration_status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "credential_type": credential_type,
                        "user_id": user_id,
                    },
                    sip_registration_status_retrieve_params.SipRegistrationStatusRetrieveParams,
                ),
            ),
            cast_to=SipRegistrationStatusRetrieveResponse,
        )


class SipRegistrationStatusResourceWithRawResponse:
    def __init__(self, sip_registration_status: SipRegistrationStatusResource) -> None:
        self._sip_registration_status = sip_registration_status

        self.retrieve = to_raw_response_wrapper(
            sip_registration_status.retrieve,
        )


class AsyncSipRegistrationStatusResourceWithRawResponse:
    def __init__(self, sip_registration_status: AsyncSipRegistrationStatusResource) -> None:
        self._sip_registration_status = sip_registration_status

        self.retrieve = async_to_raw_response_wrapper(
            sip_registration_status.retrieve,
        )


class SipRegistrationStatusResourceWithStreamingResponse:
    def __init__(self, sip_registration_status: SipRegistrationStatusResource) -> None:
        self._sip_registration_status = sip_registration_status

        self.retrieve = to_streamed_response_wrapper(
            sip_registration_status.retrieve,
        )


class AsyncSipRegistrationStatusResourceWithStreamingResponse:
    def __init__(self, sip_registration_status: AsyncSipRegistrationStatusResource) -> None:
        self._sip_registration_status = sip_registration_status

        self.retrieve = async_to_streamed_response_wrapper(
            sip_registration_status.retrieve,
        )
