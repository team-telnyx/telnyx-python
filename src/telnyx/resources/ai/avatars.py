# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import AvatarID, AvatarType, avatar_list_params, avatar_create_params, avatar_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ai.avatar import Avatar
from ...types.ai.avatar_id import AvatarID
from ...types.ai.avatar_type import AvatarType
from ...types.ai.avatar_response import AvatarResponse

__all__ = ["AvatarsResource", "AsyncAvatarsResource"]


class AvatarsResource(SyncAPIResource):
    """Create and manage real-time AI avatars"""

    @cached_property
    def with_raw_response(self) -> AvatarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AvatarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AvatarsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        image_file: FileTypes,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarResponse:
        """
        Uploads an image, validates its file type, size, safe decoding, and resolution,
        stores it in Telnyx-managed private storage, and creates an avatar owned by the
        authenticated organization. Creating an avatar does not update an AI Assistant;
        use the returned ID separately wherever the avatar is consumed. The avatar image
        is stored independently from the rendering model and background, which are
        selected where the avatar is consumed. Supported image types are JPEG, PNG, and
        WebP. Images may be up to 10 MiB, must be between 256 and 8192 pixels on each
        side, and may contain at most 40 megapixels. A per-organization custom-avatar
        quota applies; the create request returns an error when the quota is reached.
        For best results, use a 16:9 landscape image, preferably 1920 by 1080 pixels and
        at least 1280 by 720 pixels. Show one centered, front-facing person from the
        shoulders up, keep the full head and hair visible with space around it, and use
        a sharp, evenly lit image with unobstructed eyes and mouth. Use a transparent
        PNG or WebP when the avatar will be combined with a selectable background. These
        composition recommendations are not enforced in the first release; the first
        release does not validate the number of faces, pose, or image content.

        Args:
          image_file: JPEG, PNG, or WebP image file. The maximum file size is 10 MiB.

          name: Customer-facing name of the custom avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "image_file": image_file,
                "name": name,
            },
            [["image_file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/ai/avatars",
            body=maybe_transform(body, avatar_create_params.AvatarCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarResponse,
        )

    def retrieve(
        self,
        avatar_id: AvatarID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarResponse:
        """
        Returns a Telnyx stock avatar or a custom avatar owned by the authenticated
        organization. A custom avatar belonging to another organization is returned as
        not found.

        Args:
          avatar_id: Stable identifier returned by the Avatars API. Discover available stock IDs with
              GET /v2/ai/avatars and filter[avatar_type]=stock rather than maintaining a fixed
              list. Custom avatar IDs use the `avatar_` prefix and must belong to the
              authenticated organization. The service validates that the selected avatar is
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not avatar_id:
            raise ValueError(f"Expected a non-empty value for `avatar_id` but received {avatar_id!r}")
        return self._get(
            path_template("/ai/avatars/{avatar_id}", avatar_id=avatar_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarResponse,
        )

    def update(
        self,
        avatar_id: AvatarID,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarResponse:
        """
        Updates the customer-facing name of a custom avatar owned by the authenticated
        organization. Stock avatars cannot be modified. To replace the image, create a
        new custom avatar so existing references keep their original content.

        Args:
          avatar_id: Stable identifier returned by the Avatars API. Discover available stock IDs with
              GET /v2/ai/avatars and filter[avatar_type]=stock rather than maintaining a fixed
              list. Custom avatar IDs use the `avatar_` prefix and must belong to the
              authenticated organization. The service validates that the selected avatar is
              available.

          name: New customer-facing name of the custom avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not avatar_id:
            raise ValueError(f"Expected a non-empty value for `avatar_id` but received {avatar_id!r}")
        return self._patch(
            path_template("/ai/avatars/{avatar_id}", avatar_id=avatar_id),
            body=maybe_transform({"name": name}, avatar_update_params.AvatarUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarResponse,
        )

    def list(
        self,
        *,
        filter_avatar_type: AvatarType | Omit = omit,
        filter_id: AvatarID | Omit = omit,
        filter_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[Avatar]:
        """
        Returns a paginated list of the Telnyx stock avatars and custom avatars
        available to the authenticated organization. Custom avatars owned by other
        organizations are never returned. The `image_url` value is suitable for
        displaying a thumbnail and may be refreshed by listing or retrieving the avatar
        again. `suggested_voice_id` recommends a compatible Telnyx voice for stock
        avatars and is an empty string for custom avatars; it does not change an AI
        Assistant's voice automatically.

        Args:
          filter_avatar_type: Return only stock or custom avatars.

          filter_id: Return the avatar with this exact ID.

          filter_name: Return avatars whose names contain this value, using case-insensitive matching.

          page_number: Page number to retrieve, starting at 1.

          page_size: Number of avatars to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/avatars",
            page=SyncDefaultFlatPagination[Avatar],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_avatar_type": filter_avatar_type,
                        "filter_id": filter_id,
                        "filter_name": filter_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    avatar_list_params.AvatarListParams,
                ),
            ),
            model=Avatar,
        )


class AsyncAvatarsResource(AsyncAPIResource):
    """Create and manage real-time AI avatars"""

    @cached_property
    def with_raw_response(self) -> AsyncAvatarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvatarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAvatarsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        image_file: FileTypes,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarResponse:
        """
        Uploads an image, validates its file type, size, safe decoding, and resolution,
        stores it in Telnyx-managed private storage, and creates an avatar owned by the
        authenticated organization. Creating an avatar does not update an AI Assistant;
        use the returned ID separately wherever the avatar is consumed. The avatar image
        is stored independently from the rendering model and background, which are
        selected where the avatar is consumed. Supported image types are JPEG, PNG, and
        WebP. Images may be up to 10 MiB, must be between 256 and 8192 pixels on each
        side, and may contain at most 40 megapixels. A per-organization custom-avatar
        quota applies; the create request returns an error when the quota is reached.
        For best results, use a 16:9 landscape image, preferably 1920 by 1080 pixels and
        at least 1280 by 720 pixels. Show one centered, front-facing person from the
        shoulders up, keep the full head and hair visible with space around it, and use
        a sharp, evenly lit image with unobstructed eyes and mouth. Use a transparent
        PNG or WebP when the avatar will be combined with a selectable background. These
        composition recommendations are not enforced in the first release; the first
        release does not validate the number of faces, pose, or image content.

        Args:
          image_file: JPEG, PNG, or WebP image file. The maximum file size is 10 MiB.

          name: Customer-facing name of the custom avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "image_file": image_file,
                "name": name,
            },
            [["image_file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/ai/avatars",
            body=await async_maybe_transform(body, avatar_create_params.AvatarCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarResponse,
        )

    async def retrieve(
        self,
        avatar_id: AvatarID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarResponse:
        """
        Returns a Telnyx stock avatar or a custom avatar owned by the authenticated
        organization. A custom avatar belonging to another organization is returned as
        not found.

        Args:
          avatar_id: Stable identifier returned by the Avatars API. Discover available stock IDs with
              GET /v2/ai/avatars and filter[avatar_type]=stock rather than maintaining a fixed
              list. Custom avatar IDs use the `avatar_` prefix and must belong to the
              authenticated organization. The service validates that the selected avatar is
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not avatar_id:
            raise ValueError(f"Expected a non-empty value for `avatar_id` but received {avatar_id!r}")
        return await self._get(
            path_template("/ai/avatars/{avatar_id}", avatar_id=avatar_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarResponse,
        )

    async def update(
        self,
        avatar_id: AvatarID,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarResponse:
        """
        Updates the customer-facing name of a custom avatar owned by the authenticated
        organization. Stock avatars cannot be modified. To replace the image, create a
        new custom avatar so existing references keep their original content.

        Args:
          avatar_id: Stable identifier returned by the Avatars API. Discover available stock IDs with
              GET /v2/ai/avatars and filter[avatar_type]=stock rather than maintaining a fixed
              list. Custom avatar IDs use the `avatar_` prefix and must belong to the
              authenticated organization. The service validates that the selected avatar is
              available.

          name: New customer-facing name of the custom avatar.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not avatar_id:
            raise ValueError(f"Expected a non-empty value for `avatar_id` but received {avatar_id!r}")
        return await self._patch(
            path_template("/ai/avatars/{avatar_id}", avatar_id=avatar_id),
            body=await async_maybe_transform({"name": name}, avatar_update_params.AvatarUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarResponse,
        )

    def list(
        self,
        *,
        filter_avatar_type: AvatarType | Omit = omit,
        filter_id: AvatarID | Omit = omit,
        filter_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Avatar, AsyncDefaultFlatPagination[Avatar]]:
        """
        Returns a paginated list of the Telnyx stock avatars and custom avatars
        available to the authenticated organization. Custom avatars owned by other
        organizations are never returned. The `image_url` value is suitable for
        displaying a thumbnail and may be refreshed by listing or retrieving the avatar
        again. `suggested_voice_id` recommends a compatible Telnyx voice for stock
        avatars and is an empty string for custom avatars; it does not change an AI
        Assistant's voice automatically.

        Args:
          filter_avatar_type: Return only stock or custom avatars.

          filter_id: Return the avatar with this exact ID.

          filter_name: Return avatars whose names contain this value, using case-insensitive matching.

          page_number: Page number to retrieve, starting at 1.

          page_size: Number of avatars to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/avatars",
            page=AsyncDefaultFlatPagination[Avatar],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_avatar_type": filter_avatar_type,
                        "filter_id": filter_id,
                        "filter_name": filter_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    avatar_list_params.AvatarListParams,
                ),
            ),
            model=Avatar,
        )


class AvatarsResourceWithRawResponse:
    def __init__(self, avatars: AvatarsResource) -> None:
        self._avatars = avatars

        self.create = to_raw_response_wrapper(
            avatars.create,
        )
        self.retrieve = to_raw_response_wrapper(
            avatars.retrieve,
        )
        self.update = to_raw_response_wrapper(
            avatars.update,
        )
        self.list = to_raw_response_wrapper(
            avatars.list,
        )


class AsyncAvatarsResourceWithRawResponse:
    def __init__(self, avatars: AsyncAvatarsResource) -> None:
        self._avatars = avatars

        self.create = async_to_raw_response_wrapper(
            avatars.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            avatars.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            avatars.update,
        )
        self.list = async_to_raw_response_wrapper(
            avatars.list,
        )


class AvatarsResourceWithStreamingResponse:
    def __init__(self, avatars: AvatarsResource) -> None:
        self._avatars = avatars

        self.create = to_streamed_response_wrapper(
            avatars.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            avatars.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            avatars.update,
        )
        self.list = to_streamed_response_wrapper(
            avatars.list,
        )


class AsyncAvatarsResourceWithStreamingResponse:
    def __init__(self, avatars: AsyncAvatarsResource) -> None:
        self._avatars = avatars

        self.create = async_to_streamed_response_wrapper(
            avatars.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            avatars.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            avatars.update,
        )
        self.list = async_to_streamed_response_wrapper(
            avatars.list,
        )
