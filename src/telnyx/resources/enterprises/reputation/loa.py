# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.enterprises.reputation import loa_render_params, loa_update_params
from ....types.enterprises.enterprise_reputation_public_wrapped import EnterpriseReputationPublicWrapped

if TYPE_CHECKING:
    from ....types.enterprises.reputation.agent_input_param import AgentInputParam

__all__ = ["LoaResource", "AsyncLoaResource"]


class LoaResource(SyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> LoaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LoaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LoaResourceWithStreamingResponse(self)

    def update(
        self,
        enterprise_id: str,
        *,
        loa_document_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseReputationPublicWrapped:
        """Point the enterprise's reputation settings at a new signed LOA document.

        This
        resets LOA approval to `pending`; the new document must be approved before
        additional phone numbers can be added.

        Args:
          loa_document_id: Id of the new signed LOA document (from the Telnyx Documents API). Changing it
              resets LOA approval; the new document must be approved before more numbers can
              be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._patch(
            path_template("/enterprises/{enterprise_id}/reputation/loa", enterprise_id=enterprise_id),
            body=maybe_transform({"loa_document_id": loa_document_id}, loa_update_params.LoaUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseReputationPublicWrapped,
        )

    def render(
        self,
        enterprise_id: str,
        *,
        agent: AgentInputParam | Omit = omit,
        signature: loa_render_params.Signature | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Render the LOA for this enterprise as a PDF.

        The enterprise identity, address,
        and authorized-representative contact are taken from the enterprise record; the
        optional `agent` block is supplied only when a third-party partner manages the
        numbers. The response is the PDF itself (unsigned unless a `signature` is
        provided). Sign it and upload it to the Telnyx Documents API
        (`POST /v2/documents`, see https://developers.telnyx.com/api/documents) to
        obtain the `loa_document_id` required by `POST .../reputation`.

        Args:
          agent: Third-party reseller / partner managing the enterprise's phone numbers. Omit
              when the enterprise works directly with Telnyx.

          signature: Optional signature embedded in the rendered PDF. When omitted the PDF is
              returned unsigned for the customer to sign and upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation/loa", enterprise_id=enterprise_id),
            body=maybe_transform(
                {
                    "agent": agent,
                    "signature": signature,
                },
                loa_render_params.LoaRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncLoaResource(AsyncAPIResource):
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def with_raw_response(self) -> AsyncLoaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLoaResourceWithStreamingResponse(self)

    async def update(
        self,
        enterprise_id: str,
        *,
        loa_document_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseReputationPublicWrapped:
        """Point the enterprise's reputation settings at a new signed LOA document.

        This
        resets LOA approval to `pending`; the new document must be approved before
        additional phone numbers can be added.

        Args:
          loa_document_id: Id of the new signed LOA document (from the Telnyx Documents API). Changing it
              resets LOA approval; the new document must be approved before more numbers can
              be added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._patch(
            path_template("/enterprises/{enterprise_id}/reputation/loa", enterprise_id=enterprise_id),
            body=await async_maybe_transform({"loa_document_id": loa_document_id}, loa_update_params.LoaUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseReputationPublicWrapped,
        )

    async def render(
        self,
        enterprise_id: str,
        *,
        agent: AgentInputParam | Omit = omit,
        signature: loa_render_params.Signature | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Render the LOA for this enterprise as a PDF.

        The enterprise identity, address,
        and authorized-representative contact are taken from the enterprise record; the
        optional `agent` block is supplied only when a third-party partner manages the
        numbers. The response is the PDF itself (unsigned unless a `signature` is
        provided). Sign it and upload it to the Telnyx Documents API
        (`POST /v2/documents`, see https://developers.telnyx.com/api/documents) to
        obtain the `loa_document_id` required by `POST .../reputation`.

        Args:
          agent: Third-party reseller / partner managing the enterprise's phone numbers. Omit
              when the enterprise works directly with Telnyx.

          signature: Optional signature embedded in the rendered PDF. When omitted the PDF is
              returned unsigned for the customer to sign and upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation/loa", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "signature": signature,
                },
                loa_render_params.LoaRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class LoaResourceWithRawResponse:
    def __init__(self, loa: LoaResource) -> None:
        self._loa = loa

        self.update = to_raw_response_wrapper(
            loa.update,
        )
        self.render = to_custom_raw_response_wrapper(
            loa.render,
            BinaryAPIResponse,
        )


class AsyncLoaResourceWithRawResponse:
    def __init__(self, loa: AsyncLoaResource) -> None:
        self._loa = loa

        self.update = async_to_raw_response_wrapper(
            loa.update,
        )
        self.render = async_to_custom_raw_response_wrapper(
            loa.render,
            AsyncBinaryAPIResponse,
        )


class LoaResourceWithStreamingResponse:
    def __init__(self, loa: LoaResource) -> None:
        self._loa = loa

        self.update = to_streamed_response_wrapper(
            loa.update,
        )
        self.render = to_custom_streamed_response_wrapper(
            loa.render,
            StreamedBinaryAPIResponse,
        )


class AsyncLoaResourceWithStreamingResponse:
    def __init__(self, loa: AsyncLoaResource) -> None:
        self._loa = loa

        self.update = async_to_streamed_response_wrapper(
            loa.update,
        )
        self.render = async_to_custom_streamed_response_wrapper(
            loa.render,
            AsyncStreamedBinaryAPIResponse,
        )
