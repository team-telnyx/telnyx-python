# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.fqdn_connections import fqdn_authentication_patch_all_params
from ...types.fqdn_connections.fqdn_authentication_list_response import FqdnAuthenticationListResponse
from ...types.fqdn_connections.fqdn_authentication_patch_all_response import FqdnAuthenticationPatchAllResponse

__all__ = ["FqdnAuthenticationResource", "AsyncFqdnAuthenticationResource"]


class FqdnAuthenticationResource(SyncAPIResource):
    """FQDN connection operations"""

    @cached_property
    def with_raw_response(self) -> FqdnAuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FqdnAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FqdnAuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FqdnAuthenticationResourceWithStreamingResponse(self)

    def list(
        self,
        fqdn_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnAuthenticationListResponse:
        """
        Retrieves the details of an existing FQDN authentication strategy for a specific
        FQDN connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fqdn_connection_id:
            raise ValueError(f"Expected a non-empty value for `fqdn_connection_id` but received {fqdn_connection_id!r}")
        return self._get(
            path_template(
                "/fqdn_connections/{fqdn_connection_id}/fqdn_authentication", fqdn_connection_id=fqdn_connection_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnAuthenticationListResponse,
        )

    def patch_all(
        self,
        fqdn_connection_id: str,
        *,
        failover_url: str | Omit = omit,
        fqdn_outbound_authentication: Literal["ip-authentication", "credential-authentication"] | Omit = omit,
        ip_authentication_method: Literal["token", "p-charge-info"] | Omit = omit,
        password: str | Omit = omit,
        txt_name: str | Omit = omit,
        txt_ttl: int | Omit = omit,
        txt_value: str | Omit = omit,
        user_name: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnAuthenticationPatchAllResponse:
        """
        Updates the FQDN authentication strategy for a specific FQDN connection.

        Args:
          failover_url: The failover webhook URL.

          fqdn_outbound_authentication: The outbound authentication type.

          ip_authentication_method: The IP authentication method.

          password: The password for authentication.

          txt_name: The TXT record name for Microsoft Teams SBC DNS verification.

          txt_ttl: The TTL for the TXT record.

          txt_value: The TXT record value for Microsoft Teams SBC DNS verification.

          user_name: The username for authentication.

          webhook_url: The webhook URL for authentication events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fqdn_connection_id:
            raise ValueError(f"Expected a non-empty value for `fqdn_connection_id` but received {fqdn_connection_id!r}")
        return self._patch(
            path_template(
                "/fqdn_connections/{fqdn_connection_id}/fqdn_authentication", fqdn_connection_id=fqdn_connection_id
            ),
            body=maybe_transform(
                {
                    "failover_url": failover_url,
                    "fqdn_outbound_authentication": fqdn_outbound_authentication,
                    "ip_authentication_method": ip_authentication_method,
                    "password": password,
                    "txt_name": txt_name,
                    "txt_ttl": txt_ttl,
                    "txt_value": txt_value,
                    "user_name": user_name,
                    "webhook_url": webhook_url,
                },
                fqdn_authentication_patch_all_params.FqdnAuthenticationPatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnAuthenticationPatchAllResponse,
        )


class AsyncFqdnAuthenticationResource(AsyncAPIResource):
    """FQDN connection operations"""

    @cached_property
    def with_raw_response(self) -> AsyncFqdnAuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFqdnAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFqdnAuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFqdnAuthenticationResourceWithStreamingResponse(self)

    async def list(
        self,
        fqdn_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnAuthenticationListResponse:
        """
        Retrieves the details of an existing FQDN authentication strategy for a specific
        FQDN connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fqdn_connection_id:
            raise ValueError(f"Expected a non-empty value for `fqdn_connection_id` but received {fqdn_connection_id!r}")
        return await self._get(
            path_template(
                "/fqdn_connections/{fqdn_connection_id}/fqdn_authentication", fqdn_connection_id=fqdn_connection_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnAuthenticationListResponse,
        )

    async def patch_all(
        self,
        fqdn_connection_id: str,
        *,
        failover_url: str | Omit = omit,
        fqdn_outbound_authentication: Literal["ip-authentication", "credential-authentication"] | Omit = omit,
        ip_authentication_method: Literal["token", "p-charge-info"] | Omit = omit,
        password: str | Omit = omit,
        txt_name: str | Omit = omit,
        txt_ttl: int | Omit = omit,
        txt_value: str | Omit = omit,
        user_name: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FqdnAuthenticationPatchAllResponse:
        """
        Updates the FQDN authentication strategy for a specific FQDN connection.

        Args:
          failover_url: The failover webhook URL.

          fqdn_outbound_authentication: The outbound authentication type.

          ip_authentication_method: The IP authentication method.

          password: The password for authentication.

          txt_name: The TXT record name for Microsoft Teams SBC DNS verification.

          txt_ttl: The TTL for the TXT record.

          txt_value: The TXT record value for Microsoft Teams SBC DNS verification.

          user_name: The username for authentication.

          webhook_url: The webhook URL for authentication events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fqdn_connection_id:
            raise ValueError(f"Expected a non-empty value for `fqdn_connection_id` but received {fqdn_connection_id!r}")
        return await self._patch(
            path_template(
                "/fqdn_connections/{fqdn_connection_id}/fqdn_authentication", fqdn_connection_id=fqdn_connection_id
            ),
            body=await async_maybe_transform(
                {
                    "failover_url": failover_url,
                    "fqdn_outbound_authentication": fqdn_outbound_authentication,
                    "ip_authentication_method": ip_authentication_method,
                    "password": password,
                    "txt_name": txt_name,
                    "txt_ttl": txt_ttl,
                    "txt_value": txt_value,
                    "user_name": user_name,
                    "webhook_url": webhook_url,
                },
                fqdn_authentication_patch_all_params.FqdnAuthenticationPatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnAuthenticationPatchAllResponse,
        )


class FqdnAuthenticationResourceWithRawResponse:
    def __init__(self, fqdn_authentication: FqdnAuthenticationResource) -> None:
        self._fqdn_authentication = fqdn_authentication

        self.list = to_raw_response_wrapper(
            fqdn_authentication.list,
        )
        self.patch_all = to_raw_response_wrapper(
            fqdn_authentication.patch_all,
        )


class AsyncFqdnAuthenticationResourceWithRawResponse:
    def __init__(self, fqdn_authentication: AsyncFqdnAuthenticationResource) -> None:
        self._fqdn_authentication = fqdn_authentication

        self.list = async_to_raw_response_wrapper(
            fqdn_authentication.list,
        )
        self.patch_all = async_to_raw_response_wrapper(
            fqdn_authentication.patch_all,
        )


class FqdnAuthenticationResourceWithStreamingResponse:
    def __init__(self, fqdn_authentication: FqdnAuthenticationResource) -> None:
        self._fqdn_authentication = fqdn_authentication

        self.list = to_streamed_response_wrapper(
            fqdn_authentication.list,
        )
        self.patch_all = to_streamed_response_wrapper(
            fqdn_authentication.patch_all,
        )


class AsyncFqdnAuthenticationResourceWithStreamingResponse:
    def __init__(self, fqdn_authentication: AsyncFqdnAuthenticationResource) -> None:
        self._fqdn_authentication = fqdn_authentication

        self.list = async_to_streamed_response_wrapper(
            fqdn_authentication.list,
        )
        self.patch_all = async_to_streamed_response_wrapper(
            fqdn_authentication.patch_all,
        )
