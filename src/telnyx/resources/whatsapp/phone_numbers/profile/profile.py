# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .photo import (
    PhotoResource,
    AsyncPhotoResource,
    PhotoResourceWithRawResponse,
    AsyncPhotoResourceWithRawResponse,
    PhotoResourceWithStreamingResponse,
    AsyncPhotoResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.whatsapp.phone_numbers import profile_update_params
from .....types.whatsapp.phone_numbers.profile_update_response import ProfileUpdateResponse
from .....types.whatsapp.phone_numbers.profile_retrieve_response import ProfileRetrieveResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def photo(self) -> PhotoResource:
        """Manage Whatsapp phone numbers"""
        return PhotoResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """
        Get phone number business profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/profile", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def update(
        self,
        phone_number: str,
        *,
        about: str | Omit = omit,
        address: str | Omit = omit,
        category: str | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        email: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Update phone number business profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._patch(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/profile", phone_number=phone_number),
            body=maybe_transform(
                {
                    "about": about,
                    "address": address,
                    "category": category,
                    "description": description,
                    "display_name": display_name,
                    "email": email,
                    "website": website,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def photo(self) -> AsyncPhotoResource:
        """Manage Whatsapp phone numbers"""
        return AsyncPhotoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """
        Get phone number business profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/profile", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def update(
        self,
        phone_number: str,
        *,
        about: str | Omit = omit,
        address: str | Omit = omit,
        category: str | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        email: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Update phone number business profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._patch(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/profile", phone_number=phone_number),
            body=await async_maybe_transform(
                {
                    "about": about,
                    "address": address,
                    "category": category,
                    "description": description,
                    "display_name": display_name,
                    "email": email,
                    "website": website,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profile.update,
        )

    @cached_property
    def photo(self) -> PhotoResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return PhotoResourceWithRawResponse(self._profile.photo)


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profile.update,
        )

    @cached_property
    def photo(self) -> AsyncPhotoResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncPhotoResourceWithRawResponse(self._profile.photo)


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profile.update,
        )

    @cached_property
    def photo(self) -> PhotoResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return PhotoResourceWithStreamingResponse(self._profile.photo)


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )

    @cached_property
    def photo(self) -> AsyncPhotoResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncPhotoResourceWithStreamingResponse(self._profile.photo)
