# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from ...types import texml_secrets_params
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
from .accounts.accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ...types.texml_secrets_response import TexmlSecretsResponse

__all__ = ["TexmlResource", "AsyncTexmlResource"]


class TexmlResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TexmlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TexmlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TexmlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TexmlResourceWithStreamingResponse(self)

    def secrets(
        self,
        *,
        name: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlSecretsResponse:
        """
        Create a TeXML secret which can be later used as a Dynamic Parameter for TeXML
        when using Mustache Templates in your TeXML. In your TeXML you will be able to
        use your secret name, and this name will be replaced by the actual secret value
        when processing the TeXML on Telnyx side. The secrets are not visible in any
        logs.

        Args:
          name: Name used as a reference for the secret, if the name already exists within the
              account its value will be replaced

          value: Secret value which will be used when rendering the TeXML template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/texml/secrets",
            body=maybe_transform(
                {
                    "name": name,
                    "value": value,
                },
                texml_secrets_params.TexmlSecretsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlSecretsResponse,
        )


class AsyncTexmlResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTexmlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTexmlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTexmlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTexmlResourceWithStreamingResponse(self)

    async def secrets(
        self,
        *,
        name: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TexmlSecretsResponse:
        """
        Create a TeXML secret which can be later used as a Dynamic Parameter for TeXML
        when using Mustache Templates in your TeXML. In your TeXML you will be able to
        use your secret name, and this name will be replaced by the actual secret value
        when processing the TeXML on Telnyx side. The secrets are not visible in any
        logs.

        Args:
          name: Name used as a reference for the secret, if the name already exists within the
              account its value will be replaced

          value: Secret value which will be used when rendering the TeXML template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/texml/secrets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "value": value,
                },
                texml_secrets_params.TexmlSecretsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlSecretsResponse,
        )


class TexmlResourceWithRawResponse:
    def __init__(self, texml: TexmlResource) -> None:
        self._texml = texml

        self.secrets = to_raw_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._texml.accounts)

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._texml.calls)


class AsyncTexmlResourceWithRawResponse:
    def __init__(self, texml: AsyncTexmlResource) -> None:
        self._texml = texml

        self.secrets = async_to_raw_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._texml.accounts)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._texml.calls)


class TexmlResourceWithStreamingResponse:
    def __init__(self, texml: TexmlResource) -> None:
        self._texml = texml

        self.secrets = to_streamed_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._texml.accounts)

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._texml.calls)


class AsyncTexmlResourceWithStreamingResponse:
    def __init__(self, texml: AsyncTexmlResource) -> None:
        self._texml = texml

        self.secrets = async_to_streamed_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._texml.accounts)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._texml.calls)
