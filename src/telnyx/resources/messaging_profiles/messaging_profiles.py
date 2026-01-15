# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import (
    messaging_profile_list_params,
    messaging_profile_create_params,
    messaging_profile_update_params,
    messaging_profile_list_short_codes_params,
    messaging_profile_list_phone_numbers_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from .autoresp_configs import (
    AutorespConfigsResource,
    AsyncAutorespConfigsResource,
    AutorespConfigsResourceWithRawResponse,
    AsyncAutorespConfigsResourceWithRawResponse,
    AutorespConfigsResourceWithStreamingResponse,
    AsyncAutorespConfigsResourceWithStreamingResponse,
)
from ...types.messaging_profile import MessagingProfile
from ...types.shared.short_code import ShortCode
from ...types.number_pool_settings_param import NumberPoolSettingsParam
from ...types.url_shortener_settings_param import URLShortenerSettingsParam
from ...types.messaging_profile_create_response import MessagingProfileCreateResponse
from ...types.messaging_profile_delete_response import MessagingProfileDeleteResponse
from ...types.messaging_profile_update_response import MessagingProfileUpdateResponse
from ...types.messaging_profile_retrieve_response import MessagingProfileRetrieveResponse
from ...types.shared.phone_number_with_messaging_settings import PhoneNumberWithMessagingSettings

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
        whitelisted_destinations: SequenceNotStr[str],
        alpha_sender: Optional[str] | Omit = omit,
        daily_spend_limit: str | Omit = omit,
        daily_spend_limit_enabled: bool | Omit = omit,
        enabled: bool | Omit = omit,
        mms_fall_back_to_sms: bool | Omit = omit,
        mms_transcoding: bool | Omit = omit,
        mobile_only: bool | Omit = omit,
        number_pool_settings: Optional[NumberPoolSettingsParam] | Omit = omit,
        smart_encoding: bool | Omit = omit,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | Omit = omit,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | Omit = omit,
        webhook_failover_url: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          mobile_only: Send messages only to mobile phone numbers.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          smart_encoding: Enables automatic character encoding optimization for SMS messages. When
              enabled, the system automatically selects the most efficient encoding (GSM-7 or
              UCS-2) based on message content to maximize character limits and minimize costs.

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
                    "mobile_only": mobile_only,
                    "number_pool_settings": number_pool_settings,
                    "smart_encoding": smart_encoding,
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
        messaging_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingProfileRetrieveResponse:
        """
        Retrieve a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._get(
            f"/messaging_profiles/{messaging_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileRetrieveResponse,
        )

    def update(
        self,
        messaging_profile_id: str,
        *,
        alpha_sender: Optional[str] | Omit = omit,
        daily_spend_limit: str | Omit = omit,
        daily_spend_limit_enabled: bool | Omit = omit,
        enabled: bool | Omit = omit,
        mms_fall_back_to_sms: bool | Omit = omit,
        mms_transcoding: bool | Omit = omit,
        mobile_only: bool | Omit = omit,
        name: str | Omit = omit,
        number_pool_settings: Optional[NumberPoolSettingsParam] | Omit = omit,
        smart_encoding: bool | Omit = omit,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | Omit = omit,
        v1_secret: str | Omit = omit,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | Omit = omit,
        webhook_failover_url: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        whitelisted_destinations: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          mobile_only: Send messages only to mobile phone numbers.

          name: A user friendly name for the messaging profile.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          smart_encoding: Enables automatic character encoding optimization for SMS messages. When
              enabled, the system automatically selects the most efficient encoding (GSM-7 or
              UCS-2) based on message content to maximize character limits and minimize costs.

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
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._patch(
            f"/messaging_profiles/{messaging_profile_id}",
            body=maybe_transform(
                {
                    "alpha_sender": alpha_sender,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "mms_fall_back_to_sms": mms_fall_back_to_sms,
                    "mms_transcoding": mms_transcoding,
                    "mobile_only": mobile_only,
                    "name": name,
                    "number_pool_settings": number_pool_settings,
                    "smart_encoding": smart_encoding,
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
        filter: messaging_profile_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[MessagingProfile]:
        """
        List messaging profiles

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_profiles",
            page=SyncDefaultFlatPagination[MessagingProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    messaging_profile_list_params.MessagingProfileListParams,
                ),
            ),
            model=MessagingProfile,
        )

    def delete(
        self,
        messaging_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingProfileDeleteResponse:
        """
        Delete a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._delete(
            f"/messaging_profiles/{messaging_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileDeleteResponse,
        )

    def list_phone_numbers(
        self,
        messaging_profile_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings]:
        """
        List phone numbers associated with a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._get_api_list(
            f"/messaging_profiles/{messaging_profile_id}/phone_numbers",
            page=SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    messaging_profile_list_phone_numbers_params.MessagingProfileListPhoneNumbersParams,
                ),
            ),
            model=PhoneNumberWithMessagingSettings,
        )

    def list_short_codes(
        self,
        messaging_profile_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ShortCode]:
        """
        List short codes associated with a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._get_api_list(
            f"/messaging_profiles/{messaging_profile_id}/short_codes",
            page=SyncDefaultFlatPagination[ShortCode],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    messaging_profile_list_short_codes_params.MessagingProfileListShortCodesParams,
                ),
            ),
            model=ShortCode,
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
        whitelisted_destinations: SequenceNotStr[str],
        alpha_sender: Optional[str] | Omit = omit,
        daily_spend_limit: str | Omit = omit,
        daily_spend_limit_enabled: bool | Omit = omit,
        enabled: bool | Omit = omit,
        mms_fall_back_to_sms: bool | Omit = omit,
        mms_transcoding: bool | Omit = omit,
        mobile_only: bool | Omit = omit,
        number_pool_settings: Optional[NumberPoolSettingsParam] | Omit = omit,
        smart_encoding: bool | Omit = omit,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | Omit = omit,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | Omit = omit,
        webhook_failover_url: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          mobile_only: Send messages only to mobile phone numbers.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          smart_encoding: Enables automatic character encoding optimization for SMS messages. When
              enabled, the system automatically selects the most efficient encoding (GSM-7 or
              UCS-2) based on message content to maximize character limits and minimize costs.

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
                    "mobile_only": mobile_only,
                    "number_pool_settings": number_pool_settings,
                    "smart_encoding": smart_encoding,
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
        messaging_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingProfileRetrieveResponse:
        """
        Retrieve a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return await self._get(
            f"/messaging_profiles/{messaging_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileRetrieveResponse,
        )

    async def update(
        self,
        messaging_profile_id: str,
        *,
        alpha_sender: Optional[str] | Omit = omit,
        daily_spend_limit: str | Omit = omit,
        daily_spend_limit_enabled: bool | Omit = omit,
        enabled: bool | Omit = omit,
        mms_fall_back_to_sms: bool | Omit = omit,
        mms_transcoding: bool | Omit = omit,
        mobile_only: bool | Omit = omit,
        name: str | Omit = omit,
        number_pool_settings: Optional[NumberPoolSettingsParam] | Omit = omit,
        smart_encoding: bool | Omit = omit,
        url_shortener_settings: Optional[URLShortenerSettingsParam] | Omit = omit,
        v1_secret: str | Omit = omit,
        webhook_api_version: Literal["1", "2", "2010-04-01"] | Omit = omit,
        webhook_failover_url: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        whitelisted_destinations: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          mobile_only: Send messages only to mobile phone numbers.

          name: A user friendly name for the messaging profile.

          number_pool_settings: Number Pool allows you to send messages from a pool of numbers of different
              types, assigning weights to each type. The pool consists of all the long code
              and toll free numbers assigned to the messaging profile.

              To disable this feature, set the object field to `null`.

          smart_encoding: Enables automatic character encoding optimization for SMS messages. When
              enabled, the system automatically selects the most efficient encoding (GSM-7 or
              UCS-2) based on message content to maximize character limits and minimize costs.

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
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return await self._patch(
            f"/messaging_profiles/{messaging_profile_id}",
            body=await async_maybe_transform(
                {
                    "alpha_sender": alpha_sender,
                    "daily_spend_limit": daily_spend_limit,
                    "daily_spend_limit_enabled": daily_spend_limit_enabled,
                    "enabled": enabled,
                    "mms_fall_back_to_sms": mms_fall_back_to_sms,
                    "mms_transcoding": mms_transcoding,
                    "mobile_only": mobile_only,
                    "name": name,
                    "number_pool_settings": number_pool_settings,
                    "smart_encoding": smart_encoding,
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
        filter: messaging_profile_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MessagingProfile, AsyncDefaultFlatPagination[MessagingProfile]]:
        """
        List messaging profiles

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_profiles",
            page=AsyncDefaultFlatPagination[MessagingProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    messaging_profile_list_params.MessagingProfileListParams,
                ),
            ),
            model=MessagingProfile,
        )

    async def delete(
        self,
        messaging_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingProfileDeleteResponse:
        """
        Delete a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return await self._delete(
            f"/messaging_profiles/{messaging_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingProfileDeleteResponse,
        )

    def list_phone_numbers(
        self,
        messaging_profile_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PhoneNumberWithMessagingSettings, AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings]]:
        """
        List phone numbers associated with a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._get_api_list(
            f"/messaging_profiles/{messaging_profile_id}/phone_numbers",
            page=AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    messaging_profile_list_phone_numbers_params.MessagingProfileListPhoneNumbersParams,
                ),
            ),
            model=PhoneNumberWithMessagingSettings,
        )

    def list_short_codes(
        self,
        messaging_profile_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ShortCode, AsyncDefaultFlatPagination[ShortCode]]:
        """
        List short codes associated with a messaging profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not messaging_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `messaging_profile_id` but received {messaging_profile_id!r}"
            )
        return self._get_api_list(
            f"/messaging_profiles/{messaging_profile_id}/short_codes",
            page=AsyncDefaultFlatPagination[ShortCode],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    messaging_profile_list_short_codes_params.MessagingProfileListShortCodesParams,
                ),
            ),
            model=ShortCode,
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
