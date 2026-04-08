# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ...types import texml_secrets_params, texml_initiate_ai_call_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .accounts.accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ...types.texml_secrets_response import TexmlSecretsResponse
from ...types.texml_initiate_ai_call_response import TexmlInitiateAICallResponse

__all__ = ["TexmlResource", "AsyncTexmlResource"]


class TexmlResource(SyncAPIResource):
    """TeXML REST Commands"""

    @cached_property
    def accounts(self) -> AccountsResource:
        """TeXML REST Commands"""
        return AccountsResource(self._client)

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

    def initiate_ai_call(
        self,
        connection_id: str,
        *,
        ai_assistant_id: str,
        from_: str,
        to: str,
        ai_assistant_dynamic_variables: Dict[str, str] | Omit = omit,
        ai_assistant_version: str | Omit = omit,
        async_amd: bool | Omit = omit,
        async_amd_status_callback: str | Omit = omit,
        async_amd_status_callback_method: Literal["GET", "POST"] | Omit = omit,
        caller_id: str | Omit = omit,
        conversation_callback: str | Omit = omit,
        conversation_callback_method: Literal["GET", "POST"] | Omit = omit,
        conversation_callbacks: SequenceNotStr[str] | Omit = omit,
        custom_headers: Iterable[texml_initiate_ai_call_params.CustomHeader] | Omit = omit,
        detection_mode: Literal["Premium", "Regular"] | Omit = omit,
        machine_detection: Literal["Enable", "Disable", "DetectMessageEnd"] | Omit = omit,
        machine_detection_silence_timeout: int | Omit = omit,
        machine_detection_speech_end_threshold: int | Omit = omit,
        machine_detection_speech_threshold: int | Omit = omit,
        machine_detection_timeout: int | Omit = omit,
        passports: str | Omit = omit,
        preferred_codecs: str | Omit = omit,
        record: bool | Omit = omit,
        recording_channels: Literal["mono", "dual"] | Omit = omit,
        recording_status_callback: str | Omit = omit,
        recording_status_callback_event: str | Omit = omit,
        recording_status_callback_method: Literal["GET", "POST"] | Omit = omit,
        recording_timeout: int | Omit = omit,
        recording_track: Literal["inbound", "outbound", "both"] | Omit = omit,
        send_recording_url: bool | Omit = omit,
        sip_auth_password: str | Omit = omit,
        sip_auth_username: str | Omit = omit,
        sip_region: Literal["US", "Europe", "Canada", "Australia", "Middle East"] | Omit = omit,
        status_callback: str | Omit = omit,
        status_callback_event: str | Omit = omit,
        status_callback_method: Literal["GET", "POST"] | Omit = omit,
        status_callbacks: SequenceNotStr[str] | Omit = omit,
        time_limit: int | Omit = omit,
        timeout_seconds: int | Omit = omit,
        trim: Literal["trim-silence", "do-not-trim"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TexmlInitiateAICallResponse:
        """Initiate an outbound AI call with warm-up support.

        Validates parameters, builds
        an internal TeXML with an AI Assistant configuration, encodes instructions into
        client state, and calls the dial API. The Twiml, Texml, and Url parameters are
        not allowed and will result in a 422 error.

        Args:
          ai_assistant_id: The ID of the AI assistant to use for the call.

          from_: The phone number of the party initiating the call. Phone numbers are formatted
              with a `+` and country code.

          to: The phone number of the called party. Phone numbers are formatted with a `+` and
              country code.

          ai_assistant_dynamic_variables: Key-value map of dynamic variables to pass to the AI assistant.

          ai_assistant_version: The version of the AI assistant to use.

          async_amd: Select whether to perform answering machine detection in the background. By
              default execution is blocked until Answering Machine Detection is completed.

          async_amd_status_callback: URL destination for Telnyx to send AMD callback events to for the call.

          async_amd_status_callback_method: HTTP request type used for `AsyncAmdStatusCallback`.

          caller_id: To be used as the caller id name (SIP From Display Name) presented to the
              destination (`To` number). The string should have a maximum of 128 characters,
              containing only letters, numbers, spaces, and `-_~!.+` special characters. If
              omitted, the display name will be the same as the number in the `From` field.

          conversation_callback: URL destination for Telnyx to send conversation callback events to.

          conversation_callback_method: HTTP request type used for `ConversationCallback`.

          conversation_callbacks: An array of URL destinations for conversation callback events.

          custom_headers: Custom HTTP headers to be sent with the call. Each header should be an object
              with 'name' and 'value' properties.

          detection_mode: Allows you to choose between Premium and Standard detections.

          machine_detection: Enables Answering Machine Detection.

          machine_detection_silence_timeout: If initial silence duration is greater than this value, consider it a machine.
              Ignored when `premium` detection is used.

          machine_detection_speech_end_threshold: Silence duration threshold after a greeting message or voice for it be
              considered human. Ignored when `premium` detection is used.

          machine_detection_speech_threshold: Maximum threshold of a human greeting. If greeting longer than this value,
              considered machine. Ignored when `premium` detection is used.

          machine_detection_timeout: Maximum timeout threshold in milliseconds for overall detection.

          passports: A string of passport identifiers to associate with the call.

          preferred_codecs: The list of comma-separated codecs to be offered on a call.

          record: Whether to record the entire participant's call leg. Defaults to `false`.

          recording_channels: The number of channels in the final recording. Defaults to `mono`.

          recording_status_callback: The URL the recording callbacks will be sent to.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecordingStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`.

          recording_timeout: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. The
              minimum value is 0. The default value is 0 (infinite).

          recording_track: The audio track to record for the call. The default is `both`.

          send_recording_url: Whether to send RecordingUrl in webhooks.

          sip_auth_password: The password to use for SIP authentication.

          sip_auth_username: The username to use for SIP authentication.

          sip_region: Defines the SIP region to be used for the call.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_event: The call events for which Telnyx should send a webhook. Multiple events can be
              defined when separated by a space. Valid values: initiated, ringing, answered,
              completed.

          status_callback_method: HTTP request type used for `StatusCallback`.

          status_callbacks: An array of URL destinations for Telnyx to send status callback events to for
              the call.

          time_limit: The maximum duration of the call in seconds. The minimum value is 30 and the
              maximum value is 14400 (4 hours). Default is 14400 seconds.

          timeout_seconds: The number of seconds to wait for the called party to answer the call before the
              call is canceled. The minimum value is 5 and the maximum value is 120. Default
              is 30 seconds.

          trim: Whether to trim any leading and trailing silence from the recording. Defaults to
              `trim-silence`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template("/texml/ai_calls/{connection_id}", connection_id=connection_id),
            body=maybe_transform(
                {
                    "ai_assistant_id": ai_assistant_id,
                    "from_": from_,
                    "to": to,
                    "ai_assistant_dynamic_variables": ai_assistant_dynamic_variables,
                    "ai_assistant_version": ai_assistant_version,
                    "async_amd": async_amd,
                    "async_amd_status_callback": async_amd_status_callback,
                    "async_amd_status_callback_method": async_amd_status_callback_method,
                    "caller_id": caller_id,
                    "conversation_callback": conversation_callback,
                    "conversation_callback_method": conversation_callback_method,
                    "conversation_callbacks": conversation_callbacks,
                    "custom_headers": custom_headers,
                    "detection_mode": detection_mode,
                    "machine_detection": machine_detection,
                    "machine_detection_silence_timeout": machine_detection_silence_timeout,
                    "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,
                    "machine_detection_speech_threshold": machine_detection_speech_threshold,
                    "machine_detection_timeout": machine_detection_timeout,
                    "passports": passports,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_timeout": recording_timeout,
                    "recording_track": recording_track,
                    "send_recording_url": send_recording_url,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_region": sip_region,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "status_callbacks": status_callbacks,
                    "time_limit": time_limit,
                    "timeout_seconds": timeout_seconds,
                    "trim": trim,
                },
                texml_initiate_ai_call_params.TexmlInitiateAICallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlInitiateAICallResponse,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    """TeXML REST Commands"""

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """TeXML REST Commands"""
        return AsyncAccountsResource(self._client)

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

    async def initiate_ai_call(
        self,
        connection_id: str,
        *,
        ai_assistant_id: str,
        from_: str,
        to: str,
        ai_assistant_dynamic_variables: Dict[str, str] | Omit = omit,
        ai_assistant_version: str | Omit = omit,
        async_amd: bool | Omit = omit,
        async_amd_status_callback: str | Omit = omit,
        async_amd_status_callback_method: Literal["GET", "POST"] | Omit = omit,
        caller_id: str | Omit = omit,
        conversation_callback: str | Omit = omit,
        conversation_callback_method: Literal["GET", "POST"] | Omit = omit,
        conversation_callbacks: SequenceNotStr[str] | Omit = omit,
        custom_headers: Iterable[texml_initiate_ai_call_params.CustomHeader] | Omit = omit,
        detection_mode: Literal["Premium", "Regular"] | Omit = omit,
        machine_detection: Literal["Enable", "Disable", "DetectMessageEnd"] | Omit = omit,
        machine_detection_silence_timeout: int | Omit = omit,
        machine_detection_speech_end_threshold: int | Omit = omit,
        machine_detection_speech_threshold: int | Omit = omit,
        machine_detection_timeout: int | Omit = omit,
        passports: str | Omit = omit,
        preferred_codecs: str | Omit = omit,
        record: bool | Omit = omit,
        recording_channels: Literal["mono", "dual"] | Omit = omit,
        recording_status_callback: str | Omit = omit,
        recording_status_callback_event: str | Omit = omit,
        recording_status_callback_method: Literal["GET", "POST"] | Omit = omit,
        recording_timeout: int | Omit = omit,
        recording_track: Literal["inbound", "outbound", "both"] | Omit = omit,
        send_recording_url: bool | Omit = omit,
        sip_auth_password: str | Omit = omit,
        sip_auth_username: str | Omit = omit,
        sip_region: Literal["US", "Europe", "Canada", "Australia", "Middle East"] | Omit = omit,
        status_callback: str | Omit = omit,
        status_callback_event: str | Omit = omit,
        status_callback_method: Literal["GET", "POST"] | Omit = omit,
        status_callbacks: SequenceNotStr[str] | Omit = omit,
        time_limit: int | Omit = omit,
        timeout_seconds: int | Omit = omit,
        trim: Literal["trim-silence", "do-not-trim"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TexmlInitiateAICallResponse:
        """Initiate an outbound AI call with warm-up support.

        Validates parameters, builds
        an internal TeXML with an AI Assistant configuration, encodes instructions into
        client state, and calls the dial API. The Twiml, Texml, and Url parameters are
        not allowed and will result in a 422 error.

        Args:
          ai_assistant_id: The ID of the AI assistant to use for the call.

          from_: The phone number of the party initiating the call. Phone numbers are formatted
              with a `+` and country code.

          to: The phone number of the called party. Phone numbers are formatted with a `+` and
              country code.

          ai_assistant_dynamic_variables: Key-value map of dynamic variables to pass to the AI assistant.

          ai_assistant_version: The version of the AI assistant to use.

          async_amd: Select whether to perform answering machine detection in the background. By
              default execution is blocked until Answering Machine Detection is completed.

          async_amd_status_callback: URL destination for Telnyx to send AMD callback events to for the call.

          async_amd_status_callback_method: HTTP request type used for `AsyncAmdStatusCallback`.

          caller_id: To be used as the caller id name (SIP From Display Name) presented to the
              destination (`To` number). The string should have a maximum of 128 characters,
              containing only letters, numbers, spaces, and `-_~!.+` special characters. If
              omitted, the display name will be the same as the number in the `From` field.

          conversation_callback: URL destination for Telnyx to send conversation callback events to.

          conversation_callback_method: HTTP request type used for `ConversationCallback`.

          conversation_callbacks: An array of URL destinations for conversation callback events.

          custom_headers: Custom HTTP headers to be sent with the call. Each header should be an object
              with 'name' and 'value' properties.

          detection_mode: Allows you to choose between Premium and Standard detections.

          machine_detection: Enables Answering Machine Detection.

          machine_detection_silence_timeout: If initial silence duration is greater than this value, consider it a machine.
              Ignored when `premium` detection is used.

          machine_detection_speech_end_threshold: Silence duration threshold after a greeting message or voice for it be
              considered human. Ignored when `premium` detection is used.

          machine_detection_speech_threshold: Maximum threshold of a human greeting. If greeting longer than this value,
              considered machine. Ignored when `premium` detection is used.

          machine_detection_timeout: Maximum timeout threshold in milliseconds for overall detection.

          passports: A string of passport identifiers to associate with the call.

          preferred_codecs: The list of comma-separated codecs to be offered on a call.

          record: Whether to record the entire participant's call leg. Defaults to `false`.

          recording_channels: The number of channels in the final recording. Defaults to `mono`.

          recording_status_callback: The URL the recording callbacks will be sent to.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecordingStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`.

          recording_timeout: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. The
              minimum value is 0. The default value is 0 (infinite).

          recording_track: The audio track to record for the call. The default is `both`.

          send_recording_url: Whether to send RecordingUrl in webhooks.

          sip_auth_password: The password to use for SIP authentication.

          sip_auth_username: The username to use for SIP authentication.

          sip_region: Defines the SIP region to be used for the call.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_event: The call events for which Telnyx should send a webhook. Multiple events can be
              defined when separated by a space. Valid values: initiated, ringing, answered,
              completed.

          status_callback_method: HTTP request type used for `StatusCallback`.

          status_callbacks: An array of URL destinations for Telnyx to send status callback events to for
              the call.

          time_limit: The maximum duration of the call in seconds. The minimum value is 30 and the
              maximum value is 14400 (4 hours). Default is 14400 seconds.

          timeout_seconds: The number of seconds to wait for the called party to answer the call before the
              call is canceled. The minimum value is 5 and the maximum value is 120. Default
              is 30 seconds.

          trim: Whether to trim any leading and trailing silence from the recording. Defaults to
              `trim-silence`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template("/texml/ai_calls/{connection_id}", connection_id=connection_id),
            body=await async_maybe_transform(
                {
                    "ai_assistant_id": ai_assistant_id,
                    "from_": from_,
                    "to": to,
                    "ai_assistant_dynamic_variables": ai_assistant_dynamic_variables,
                    "ai_assistant_version": ai_assistant_version,
                    "async_amd": async_amd,
                    "async_amd_status_callback": async_amd_status_callback,
                    "async_amd_status_callback_method": async_amd_status_callback_method,
                    "caller_id": caller_id,
                    "conversation_callback": conversation_callback,
                    "conversation_callback_method": conversation_callback_method,
                    "conversation_callbacks": conversation_callbacks,
                    "custom_headers": custom_headers,
                    "detection_mode": detection_mode,
                    "machine_detection": machine_detection,
                    "machine_detection_silence_timeout": machine_detection_silence_timeout,
                    "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,
                    "machine_detection_speech_threshold": machine_detection_speech_threshold,
                    "machine_detection_timeout": machine_detection_timeout,
                    "passports": passports,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_timeout": recording_timeout,
                    "recording_track": recording_track,
                    "send_recording_url": send_recording_url,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_region": sip_region,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "status_callbacks": status_callbacks,
                    "time_limit": time_limit,
                    "timeout_seconds": timeout_seconds,
                    "trim": trim,
                },
                texml_initiate_ai_call_params.TexmlInitiateAICallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TexmlInitiateAICallResponse,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

        self.initiate_ai_call = to_raw_response_wrapper(
            texml.initiate_ai_call,
        )
        self.secrets = to_raw_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """TeXML REST Commands"""
        return AccountsResourceWithRawResponse(self._texml.accounts)


class AsyncTexmlResourceWithRawResponse:
    def __init__(self, texml: AsyncTexmlResource) -> None:
        self._texml = texml

        self.initiate_ai_call = async_to_raw_response_wrapper(
            texml.initiate_ai_call,
        )
        self.secrets = async_to_raw_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """TeXML REST Commands"""
        return AsyncAccountsResourceWithRawResponse(self._texml.accounts)


class TexmlResourceWithStreamingResponse:
    def __init__(self, texml: TexmlResource) -> None:
        self._texml = texml

        self.initiate_ai_call = to_streamed_response_wrapper(
            texml.initiate_ai_call,
        )
        self.secrets = to_streamed_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """TeXML REST Commands"""
        return AccountsResourceWithStreamingResponse(self._texml.accounts)


class AsyncTexmlResourceWithStreamingResponse:
    def __init__(self, texml: AsyncTexmlResource) -> None:
        self._texml = texml

        self.initiate_ai_call = async_to_streamed_response_wrapper(
            texml.initiate_ai_call,
        )
        self.secrets = async_to_streamed_response_wrapper(
            texml.secrets,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """TeXML REST Commands"""
        return AsyncAccountsResourceWithStreamingResponse(self._texml.accounts)
