# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ...types import fax_list_params, fax_create_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.fax_list_response import FaxListResponse
from ...types.fax_create_response import FaxCreateResponse
from ...types.fax_retrieve_response import FaxRetrieveResponse

__all__ = ["FaxesResource", "AsyncFaxesResource"]


class FaxesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FaxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FaxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FaxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FaxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_id: str,
        from_: str,
        to: str,
        client_state: str | NotGiven = NOT_GIVEN,
        from_display_name: str | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        media_url: str | NotGiven = NOT_GIVEN,
        monochrome: bool | NotGiven = NOT_GIVEN,
        preview_format: Literal["pdf", "tiff"] | NotGiven = NOT_GIVEN,
        quality: Literal["normal", "high", "very_high", "ultra_light", "ultra_dark"] | NotGiven = NOT_GIVEN,
        store_media: bool | NotGiven = NOT_GIVEN,
        store_preview: bool | NotGiven = NOT_GIVEN,
        t38_enabled: bool | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaxCreateResponse:
        """Send a fax.

        Files have size limits and page count limit validations. If a file
        is bigger than 50MB or has more than 350 pages it will fail with
        `file_size_limit_exceeded` and `page_count_limit_exceeded` respectively.

        **Expected Webhooks:**

        - `fax.queued`
        - `fax.media.processed`
        - `fax.sending.started`
        - `fax.delivered`
        - `fax.failed`

        Args:
          connection_id: The connection ID to send the fax with.

          from_: The phone number, in E.164 format, the fax will be sent from.

          to: The phone number, in E.164 format, the fax will be sent to or SIP URI

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          from_display_name: The `from_display_name` string to be used as the caller id name (SIP From
              Display Name) presented to the destination (`to` number). The string should have
              a maximum of 128 characters, containing only letters, numbers, spaces, and
              -\\__~!.+ special characters. If ommited, the display name will be the same as the
              number in the `from` field.

          media_name: The media_name used for the fax's media. Must point to a file previously
              uploaded to api.telnyx.com/v2/media by the same user/organization. media_name
              and media_url/contents can't be submitted together.

          media_url: The URL (or list of URLs) to the PDF used for the fax's media. media_url and
              media_name/contents can't be submitted together.

          monochrome: The flag to enable monochrome, true black and white fax results.

          preview_format: The format for the preview file in case the `store_preview` is `true`.

          quality: The quality of the fax. The `ultra` settings provides the highest quality
              available, but also present longer fax processing times. `ultra_light` is best
              suited for images, wihle `ultra_dark` is best suited for text.

          store_media: Should fax media be stored on temporary URL. It does not support media_name,
              they can't be submitted together.

          store_preview: Should fax preview be stored on temporary URL.

          t38_enabled: The flag to disable the T.38 protocol.

          webhook_url: Use this field to override the URL to which Telnyx will send subsequent webhooks
              for this fax.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "connection_id": connection_id,
                "from_": from_,
                "to": to,
                "client_state": client_state,
                "from_display_name": from_display_name,
                "media_name": media_name,
                "media_url": media_url,
                "monochrome": monochrome,
                "preview_format": preview_format,
                "quality": quality,
                "store_media": store_media,
                "store_preview": store_preview,
                "t38_enabled": t38_enabled,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["contents"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/faxes",
            body=maybe_transform(body, fax_create_params.FaxCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaxRetrieveResponse:
        """
        View a fax

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/faxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: fax_list_params.Filter | NotGiven = NOT_GIVEN,
        page: fax_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaxListResponse:
        """
        View a list of faxes

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[created_at][gte], filter[created_at][gt], filter[created_at][lte],
              filter[created_at][lt], filter[direction][eq], filter[from][eq], filter[to][eq]

          page: Consolidated pagination parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/faxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    fax_list_params.FaxListParams,
                ),
            ),
            cast_to=FaxListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a fax

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/faxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFaxesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFaxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFaxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFaxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFaxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_id: str,
        from_: str,
        to: str,
        client_state: str | NotGiven = NOT_GIVEN,
        from_display_name: str | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        media_url: str | NotGiven = NOT_GIVEN,
        monochrome: bool | NotGiven = NOT_GIVEN,
        preview_format: Literal["pdf", "tiff"] | NotGiven = NOT_GIVEN,
        quality: Literal["normal", "high", "very_high", "ultra_light", "ultra_dark"] | NotGiven = NOT_GIVEN,
        store_media: bool | NotGiven = NOT_GIVEN,
        store_preview: bool | NotGiven = NOT_GIVEN,
        t38_enabled: bool | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaxCreateResponse:
        """Send a fax.

        Files have size limits and page count limit validations. If a file
        is bigger than 50MB or has more than 350 pages it will fail with
        `file_size_limit_exceeded` and `page_count_limit_exceeded` respectively.

        **Expected Webhooks:**

        - `fax.queued`
        - `fax.media.processed`
        - `fax.sending.started`
        - `fax.delivered`
        - `fax.failed`

        Args:
          connection_id: The connection ID to send the fax with.

          from_: The phone number, in E.164 format, the fax will be sent from.

          to: The phone number, in E.164 format, the fax will be sent to or SIP URI

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          from_display_name: The `from_display_name` string to be used as the caller id name (SIP From
              Display Name) presented to the destination (`to` number). The string should have
              a maximum of 128 characters, containing only letters, numbers, spaces, and
              -\\__~!.+ special characters. If ommited, the display name will be the same as the
              number in the `from` field.

          media_name: The media_name used for the fax's media. Must point to a file previously
              uploaded to api.telnyx.com/v2/media by the same user/organization. media_name
              and media_url/contents can't be submitted together.

          media_url: The URL (or list of URLs) to the PDF used for the fax's media. media_url and
              media_name/contents can't be submitted together.

          monochrome: The flag to enable monochrome, true black and white fax results.

          preview_format: The format for the preview file in case the `store_preview` is `true`.

          quality: The quality of the fax. The `ultra` settings provides the highest quality
              available, but also present longer fax processing times. `ultra_light` is best
              suited for images, wihle `ultra_dark` is best suited for text.

          store_media: Should fax media be stored on temporary URL. It does not support media_name,
              they can't be submitted together.

          store_preview: Should fax preview be stored on temporary URL.

          t38_enabled: The flag to disable the T.38 protocol.

          webhook_url: Use this field to override the URL to which Telnyx will send subsequent webhooks
              for this fax.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "connection_id": connection_id,
                "from_": from_,
                "to": to,
                "client_state": client_state,
                "from_display_name": from_display_name,
                "media_name": media_name,
                "media_url": media_url,
                "monochrome": monochrome,
                "preview_format": preview_format,
                "quality": quality,
                "store_media": store_media,
                "store_preview": store_preview,
                "t38_enabled": t38_enabled,
                "webhook_url": webhook_url,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["contents"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/faxes",
            body=await async_maybe_transform(body, fax_create_params.FaxCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaxRetrieveResponse:
        """
        View a fax

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/faxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: fax_list_params.Filter | NotGiven = NOT_GIVEN,
        page: fax_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaxListResponse:
        """
        View a list of faxes

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[created_at][gte], filter[created_at][gt], filter[created_at][lte],
              filter[created_at][lt], filter[direction][eq], filter[from][eq], filter[to][eq]

          page: Consolidated pagination parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/faxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    fax_list_params.FaxListParams,
                ),
            ),
            cast_to=FaxListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a fax

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/faxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FaxesResourceWithRawResponse:
    def __init__(self, faxes: FaxesResource) -> None:
        self._faxes = faxes

        self.create = to_raw_response_wrapper(
            faxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            faxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            faxes.list,
        )
        self.delete = to_raw_response_wrapper(
            faxes.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._faxes.actions)


class AsyncFaxesResourceWithRawResponse:
    def __init__(self, faxes: AsyncFaxesResource) -> None:
        self._faxes = faxes

        self.create = async_to_raw_response_wrapper(
            faxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            faxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            faxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            faxes.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._faxes.actions)


class FaxesResourceWithStreamingResponse:
    def __init__(self, faxes: FaxesResource) -> None:
        self._faxes = faxes

        self.create = to_streamed_response_wrapper(
            faxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            faxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            faxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            faxes.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._faxes.actions)


class AsyncFaxesResourceWithStreamingResponse:
    def __init__(self, faxes: AsyncFaxesResource) -> None:
        self._faxes = faxes

        self.create = async_to_streamed_response_wrapper(
            faxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            faxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            faxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            faxes.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._faxes.actions)
