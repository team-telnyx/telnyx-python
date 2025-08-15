# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    messaging_profile_list_params,
    messaging_profile_create_params,
    messaging_profile_update_params,
    messaging_profile_list_short_codes_params,
    messaging_profile_list_phone_numbers_params,
)
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
from .autoresp_configs import (
    AutorespConfigsResource,
    AsyncAutorespConfigsResource,
    AutorespConfigsResourceWithRawResponse,
    AsyncAutorespConfigsResourceWithRawResponse,
    AutorespConfigsResourceWithStreamingResponse,
    AsyncAutorespConfigsResourceWithStreamingResponse,
)
from ...types.number_pool_settings_param import NumberPoolSettingsParam
from ...types.url_shortener_settings_param import URLShortenerSettingsParam
from ...types.messaging_profile_list_response import MessagingProfileListResponse
from ...types.messaging_profile_create_response import MessagingProfileCreateResponse
from ...types.messaging_profile_delete_response import MessagingProfileDeleteResponse
from ...types.messaging_profile_update_response import MessagingProfileUpdateResponse
from ...types.messaging_profile_retrieve_response import MessagingProfileRetrieveResponse
from ...types.messaging_profile_list_short_codes_response import MessagingProfileListShortCodesResponse
from ...types.messaging_profile_list_phone_numbers_response import MessagingProfileListPhoneNumbersResponse

__all__ = ["MessagingProfilesResource", "AsyncMessagingProfilesResource"]


class MessagingProfilesResource(SyncAPIResource):
    @cached_property
    def autoresp_configs(self) -> AutorespConfigsResource:
        return AutorespConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagingProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        whitelisted_destinations: List[str],
        alpha_sender: Optional[str] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        mms_fall_back_to_sms: bool | NotGiven = NOT_GIVEN,
        mms_transcoding: bool | NotGiven = NOT_GIVEN,
        number_pool_settings: Optional[NumberPoolSettingsParam] | NotGiven = NOT_GIVEN,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | NotGiven = NOT_GIVEN,
        webhook_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileCreateResponse:
        """
        Create a messaging profile

        Args:
          name: A user friendly name for the messaging profile.

          whitelisted_destinations: Destinations to which the messaging profile is allowed to send. The elements in
              the list must be valid ISO 3166-1 alpha-2 country codes. If set to `["*"]` all
              destinations will be allowed.

          alpha_sender: The alphanumeric sender ID to use when sending to destinations that require an
              alphanumeric sender ID.

          daily_spend_limit: The maximum amount of money (in USD) that can be spent by this profile before
              midnight UTC.

          daily_spend_limit_enabled: Whether to enforce the value configured by `daily_spend_limit`.

          enabled: Specifies whether the messaging profile is enabled or not.

          mms_fall_back_to_sms: enables SMS fallback for MMS messages.

          mms_transcoding: enables automated resizing of MMS media.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          url_shortener_settings: The URL shortener feature allows automatic replacement of URLs that were
              generated using a public URL shortener service. Some examples include bit.do,
              bit.ly, goo.gl, ht.ly, is.gd, ow.ly, rebrand.ly, t.co, tiny.cc, and tinyurl.com.
              Such URLs are replaced with with links generated by Telnyx. The use of custom
              links can improve branding and message deliverability.

              To disable this feature, set the object field to `null`.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1, v2, or a legacy
              2010-04-01 format.

          webhook_failover_url: The failover URL where webhooks related to this messaging profile will be sent
              if sending to the primary URL fails.

          webhook_url: The URL where webhooks related to this messaging profile will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messaging_profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "whitelisted_destinations": whitelisted_destinations,
                    "alpha_sender": alpha_sender,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "mms_fall_back_to_sms": mms_fall_back_to_sms,
                    "mms_transcoding": mms_transcoding,
                    "number_pool_settings": number_pool_settings,
                    "url_shortener_settings": url_shortener_settings,
                    "webhook_api_version": webhook_api_version,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                messaging_profile_create_params.MessagingProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileCreateResponse,
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
    ) -> MessagingProfileRetrieveResponse:
        """
        Retrieve a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/messaging_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        alpha_sender: Optional[str] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        mms_fall_back_to_sms: bool | NotGiven = NOT_GIVEN,
        mms_transcoding: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number_pool_settings: Optional[NumberPoolSettingsParam] | NotGiven = NOT_GIVEN,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | NotGiven = NOT_GIVEN,
        v1_secret: str | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | NotGiven = NOT_GIVEN,
        webhook_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        whitelisted_destinations: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileUpdateResponse:
        """
        Update a messaging profile

        Args:
          alpha_sender: The alphanumeric sender ID to use when sending to destinations that require an
              alphanumeric sender ID.

          daily_spend_limit: The maximum amount of money (in USD) that can be spent by this profile before
              midnight UTC.

          daily_spend_limit_enabled: Whether to enforce the value configured by `daily_spend_limit`.

          enabled: Specifies whether the messaging profile is enabled or not.

          mms_fall_back_to_sms: enables SMS fallback for MMS messages.

          mms_transcoding: enables automated resizing of MMS media.

          name: A user friendly name for the messaging profile.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          url_shortener_settings: The URL shortener feature allows automatic replacement of URLs that were
              generated using a public URL shortener service. Some examples include bit.do,
              bit.ly, goo.gl, ht.ly, is.gd, ow.ly, rebrand.ly, t.co, tiny.cc, and tinyurl.com.
              Such URLs are replaced with with links generated by Telnyx. The use of custom
              links can improve branding and message deliverability.

              To disable this feature, set the object field to `null`.

          v1_secret: Secret used to authenticate with v1 endpoints.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1, v2, or a legacy
              2010-04-01 format.

          webhook_failover_url: The failover URL where webhooks related to this messaging profile will be sent
              if sending to the primary URL fails.

          webhook_url: The URL where webhooks related to this messaging profile will be sent.

          whitelisted_destinations: Destinations to which the messaging profile is allowed to send. The elements in
              the list must be valid ISO 3166-1 alpha-2 country codes. If set to `["*"]`, all
              destinations will be allowed.

              This field is required if the messaging profile doesn't have it defined yet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/messaging_profiles/{id}",
            body=maybe_transform(
                {
                    "alpha_sender": alpha_sender,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "mms_fall_back_to_sms": mms_fall_back_to_sms,
                    "mms_transcoding": mms_transcoding,
                    "name": name,
                    "number_pool_settings": number_pool_settings,
                    "url_shortener_settings": url_shortener_settings,
                    "v1_secret": v1_secret,
                    "webhook_api_version": webhook_api_version,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                    "whitelisted_destinations": whitelisted_destinations,
                },
                messaging_profile_update_params.MessagingProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileUpdateResponse,
        )

    def list(
        self,
        *,
        filter: messaging_profile_list_params.Filter | NotGiven = NOT_GIVEN,
        page: messaging_profile_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileListResponse:
        """
        List messaging profiles

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/messaging_profiles",
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
                    messaging_profile_list_params.MessagingProfileListParams,
                ),
            ),
            cast_to=MessagingProfileListResponse,
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
    ) -> MessagingProfileDeleteResponse:
        """
        Delete a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/messaging_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileDeleteResponse,
        )

    def list_phone_numbers(
        self,
        id: str,
        *,
        page: messaging_profile_list_phone_numbers_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileListPhoneNumbersResponse:
        """
        List phone numbers associated with a messaging profile

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/messaging_profiles/{id}/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page}, messaging_profile_list_phone_numbers_params.MessagingProfileListPhoneNumbersParams
                ),
            ),
            cast_to=MessagingProfileListPhoneNumbersResponse,
        )

    def list_short_codes(
        self,
        id: str,
        *,
        page: messaging_profile_list_short_codes_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileListShortCodesResponse:
        """
        List short codes associated with a messaging profile

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/messaging_profiles/{id}/short_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page}, messaging_profile_list_short_codes_params.MessagingProfileListShortCodesParams
                ),
            ),
            cast_to=MessagingProfileListShortCodesResponse,
        )


class AsyncMessagingProfilesResource(AsyncAPIResource):
    @cached_property
    def autoresp_configs(self) -> AsyncAutorespConfigsResource:
        return AsyncAutorespConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagingProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        whitelisted_destinations: List[str],
        alpha_sender: Optional[str] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        mms_fall_back_to_sms: bool | NotGiven = NOT_GIVEN,
        mms_transcoding: bool | NotGiven = NOT_GIVEN,
        number_pool_settings: Optional[NumberPoolSettingsParam] | NotGiven = NOT_GIVEN,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | NotGiven = NOT_GIVEN,
        webhook_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileCreateResponse:
        """
        Create a messaging profile

        Args:
          name: A user friendly name for the messaging profile.

          whitelisted_destinations: Destinations to which the messaging profile is allowed to send. The elements in
              the list must be valid ISO 3166-1 alpha-2 country codes. If set to `["*"]` all
              destinations will be allowed.

          alpha_sender: The alphanumeric sender ID to use when sending to destinations that require an
              alphanumeric sender ID.

          daily_spend_limit: The maximum amount of money (in USD) that can be spent by this profile before
              midnight UTC.

          daily_spend_limit_enabled: Whether to enforce the value configured by `daily_spend_limit`.

          enabled: Specifies whether the messaging profile is enabled or not.

          mms_fall_back_to_sms: enables SMS fallback for MMS messages.

          mms_transcoding: enables automated resizing of MMS media.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          url_shortener_settings: The URL shortener feature allows automatic replacement of URLs that were
              generated using a public URL shortener service. Some examples include bit.do,
              bit.ly, goo.gl, ht.ly, is.gd, ow.ly, rebrand.ly, t.co, tiny.cc, and tinyurl.com.
              Such URLs are replaced with with links generated by Telnyx. The use of custom
              links can improve branding and message deliverability.

              To disable this feature, set the object field to `null`.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1, v2, or a legacy
              2010-04-01 format.

          webhook_failover_url: The failover URL where webhooks related to this messaging profile will be sent
              if sending to the primary URL fails.

          webhook_url: The URL where webhooks related to this messaging profile will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messaging_profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "whitelisted_destinations": whitelisted_destinations,
                    "alpha_sender": alpha_sender,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "mms_fall_back_to_sms": mms_fall_back_to_sms,
                    "mms_transcoding": mms_transcoding,
                    "number_pool_settings": number_pool_settings,
                    "url_shortener_settings": url_shortener_settings,
                    "webhook_api_version": webhook_api_version,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                messaging_profile_create_params.MessagingProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileCreateResponse,
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
    ) -> MessagingProfileRetrieveResponse:
        """
        Retrieve a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/messaging_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        alpha_sender: Optional[str] | NotGiven = NOT_GIVEN,
        daily_spend_limit: str | NotGiven = NOT_GIVEN,
        daily_spend_limit_enabled: bool | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        mms_fall_back_to_sms: bool | NotGiven = NOT_GIVEN,
        mms_transcoding: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        number_pool_settings: Optional[NumberPoolSettingsParam] | NotGiven = NOT_GIVEN,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | NotGiven = NOT_GIVEN,
        v1_secret: str | NotGiven = NOT_GIVEN,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | NotGiven = NOT_GIVEN,
        webhook_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        whitelisted_destinations: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileUpdateResponse:
        """
        Update a messaging profile

        Args:
          alpha_sender: The alphanumeric sender ID to use when sending to destinations that require an
              alphanumeric sender ID.

          daily_spend_limit: The maximum amount of money (in USD) that can be spent by this profile before
              midnight UTC.

          daily_spend_limit_enabled: Whether to enforce the value configured by `daily_spend_limit`.

          enabled: Specifies whether the messaging profile is enabled or not.

          mms_fall_back_to_sms: enables SMS fallback for MMS messages.

          mms_transcoding: enables automated resizing of MMS media.

          name: A user friendly name for the messaging profile.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          url_shortener_settings: The URL shortener feature allows automatic replacement of URLs that were
              generated using a public URL shortener service. Some examples include bit.do,
              bit.ly, goo.gl, ht.ly, is.gd, ow.ly, rebrand.ly, t.co, tiny.cc, and tinyurl.com.
              Such URLs are replaced with with links generated by Telnyx. The use of custom
              links can improve branding and message deliverability.

              To disable this feature, set the object field to `null`.

          v1_secret: Secret used to authenticate with v1 endpoints.

          webhook_api_version: Determines which webhook format will be used, Telnyx API v1, v2, or a legacy
              2010-04-01 format.

          webhook_failover_url: The failover URL where webhooks related to this messaging profile will be sent
              if sending to the primary URL fails.

          webhook_url: The URL where webhooks related to this messaging profile will be sent.

          whitelisted_destinations: Destinations to which the messaging profile is allowed to send. The elements in
              the list must be valid ISO 3166-1 alpha-2 country codes. If set to `["*"]`, all
              destinations will be allowed.

              This field is required if the messaging profile doesn't have it defined yet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/messaging_profiles/{id}",
            body=await async_maybe_transform(
                {
                    "alpha_sender": alpha_sender,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "mms_fall_back_to_sms": mms_fall_back_to_sms,
                    "mms_transcoding": mms_transcoding,
                    "name": name,
                    "number_pool_settings": number_pool_settings,
                    "url_shortener_settings": url_shortener_settings,
                    "v1_secret": v1_secret,
                    "webhook_api_version": webhook_api_version,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                    "whitelisted_destinations": whitelisted_destinations,
                },
                messaging_profile_update_params.MessagingProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: messaging_profile_list_params.Filter | NotGiven = NOT_GIVEN,
        page: messaging_profile_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileListResponse:
        """
        List messaging profiles

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/messaging_profiles",
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
                    messaging_profile_list_params.MessagingProfileListParams,
                ),
            ),
            cast_to=MessagingProfileListResponse,
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
    ) -> MessagingProfileDeleteResponse:
        """
        Delete a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/messaging_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileDeleteResponse,
        )

    async def list_phone_numbers(
        self,
        id: str,
        *,
        page: messaging_profile_list_phone_numbers_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileListPhoneNumbersResponse:
        """
        List phone numbers associated with a messaging profile

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/messaging_profiles/{id}/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, messaging_profile_list_phone_numbers_params.MessagingProfileListPhoneNumbersParams
                ),
            ),
            cast_to=MessagingProfileListPhoneNumbersResponse,
        )

    async def list_short_codes(
        self,
        id: str,
        *,
        page: messaging_profile_list_short_codes_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingProfileListShortCodesResponse:
        """
        List short codes associated with a messaging profile

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/messaging_profiles/{id}/short_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, messaging_profile_list_short_codes_params.MessagingProfileListShortCodesParams
                ),
            ),
            cast_to=MessagingProfileListShortCodesResponse,
        )


class MessagingProfilesResourceWithRawResponse:
    def __init__(self, messaging_profiles: MessagingProfilesResource) -> None:
        self._messaging_profiles = messaging_profiles

        self.create = to_raw_response_wrapper(
            messaging_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messaging_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messaging_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            messaging_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            messaging_profiles.delete,
        )
        self.list_phone_numbers = to_raw_response_wrapper(
            messaging_profiles.list_phone_numbers,
        )
        self.list_short_codes = to_raw_response_wrapper(
            messaging_profiles.list_short_codes,
        )

    @cached_property
    def autoresp_configs(self) -> AutorespConfigsResourceWithRawResponse:
        return AutorespConfigsResourceWithRawResponse(self._messaging_profiles.autoresp_configs)


class AsyncMessagingProfilesResourceWithRawResponse:
    def __init__(self, messaging_profiles: AsyncMessagingProfilesResource) -> None:
        self._messaging_profiles = messaging_profiles

        self.create = async_to_raw_response_wrapper(
            messaging_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messaging_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messaging_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            messaging_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messaging_profiles.delete,
        )
        self.list_phone_numbers = async_to_raw_response_wrapper(
            messaging_profiles.list_phone_numbers,
        )
        self.list_short_codes = async_to_raw_response_wrapper(
            messaging_profiles.list_short_codes,
        )

    @cached_property
    def autoresp_configs(self) -> AsyncAutorespConfigsResourceWithRawResponse:
        return AsyncAutorespConfigsResourceWithRawResponse(self._messaging_profiles.autoresp_configs)


class MessagingProfilesResourceWithStreamingResponse:
    def __init__(self, messaging_profiles: MessagingProfilesResource) -> None:
        self._messaging_profiles = messaging_profiles

        self.create = to_streamed_response_wrapper(
            messaging_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messaging_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messaging_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            messaging_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            messaging_profiles.delete,
        )
        self.list_phone_numbers = to_streamed_response_wrapper(
            messaging_profiles.list_phone_numbers,
        )
        self.list_short_codes = to_streamed_response_wrapper(
            messaging_profiles.list_short_codes,
        )

    @cached_property
    def autoresp_configs(self) -> AutorespConfigsResourceWithStreamingResponse:
        return AutorespConfigsResourceWithStreamingResponse(self._messaging_profiles.autoresp_configs)


class AsyncMessagingProfilesResourceWithStreamingResponse:
    def __init__(self, messaging_profiles: AsyncMessagingProfilesResource) -> None:
        self._messaging_profiles = messaging_profiles

        self.create = async_to_streamed_response_wrapper(
            messaging_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messaging_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messaging_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messaging_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messaging_profiles.delete,
        )
        self.list_phone_numbers = async_to_streamed_response_wrapper(
            messaging_profiles.list_phone_numbers,
        )
        self.list_short_codes = async_to_streamed_response_wrapper(
            messaging_profiles.list_short_codes,
        )

    @cached_property
    def autoresp_configs(self) -> AsyncAutorespConfigsResourceWithStreamingResponse:
        return AsyncAutorespConfigsResourceWithStreamingResponse(self._messaging_profiles.autoresp_configs)
