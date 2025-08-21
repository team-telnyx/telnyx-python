# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import (
    assistant_chat_params,
    assistant_create_params,
    assistant_import_params,
    assistant_update_params,
    assistant_retrieve_params,
)
from .tests.tests import (
    TestsResource,
    AsyncTestsResource,
    TestsResourceWithRawResponse,
    AsyncTestsResourceWithRawResponse,
    TestsResourceWithStreamingResponse,
    AsyncTestsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .canary_deploys import (
    CanaryDeploysResource,
    AsyncCanaryDeploysResource,
    CanaryDeploysResourceWithRawResponse,
    AsyncCanaryDeploysResourceWithRawResponse,
    CanaryDeploysResourceWithStreamingResponse,
    AsyncCanaryDeploysResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .scheduled_events import (
    ScheduledEventsResource,
    AsyncScheduledEventsResource,
    ScheduledEventsResourceWithRawResponse,
    AsyncScheduledEventsResourceWithRawResponse,
    ScheduledEventsResourceWithStreamingResponse,
    AsyncScheduledEventsResourceWithStreamingResponse,
)
from ....types.ai.assistants_list import AssistantsList
from ....types.ai.enabled_features import EnabledFeatures
from ....types.ai.assistant_tool_param import AssistantToolParam
from ....types.ai.voice_settings_param import VoiceSettingsParam
from ....types.ai.insight_settings_param import InsightSettingsParam
from ....types.ai.privacy_settings_param import PrivacySettingsParam
from ....types.ai.assistant_chat_response import AssistantChatResponse
from ....types.ai.assistant_clone_response import AssistantCloneResponse
from ....types.ai.messaging_settings_param import MessagingSettingsParam
from ....types.ai.telephony_settings_param import TelephonySettingsParam
from ....types.ai.assistant_create_response import AssistantCreateResponse
from ....types.ai.assistant_delete_response import AssistantDeleteResponse
from ....types.ai.assistant_retrieve_response import AssistantRetrieveResponse
from ....types.ai.transcription_settings_param import TranscriptionSettingsParam

__all__ = ["AssistantsResource", "AsyncAssistantsResource"]


class AssistantsResource(SyncAPIResource):
    @cached_property
    def tests(self) -> TestsResource:
        return TestsResource(self._client)

    @cached_property
    def canary_deploys(self) -> CanaryDeploysResource:
        return CanaryDeploysResource(self._client)

    @cached_property
    def scheduled_events(self) -> ScheduledEventsResource:
        return ScheduledEventsResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssistantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AssistantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssistantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AssistantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        instructions: str,
        model: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        dynamic_variables_webhook_url: str | NotGiven = NOT_GIVEN,
        enabled_features: List[EnabledFeatures] | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        insight_settings: InsightSettingsParam | NotGiven = NOT_GIVEN,
        llm_api_key_ref: str | NotGiven = NOT_GIVEN,
        messaging_settings: MessagingSettingsParam | NotGiven = NOT_GIVEN,
        privacy_settings: PrivacySettingsParam | NotGiven = NOT_GIVEN,
        telephony_settings: TelephonySettingsParam | NotGiven = NOT_GIVEN,
        tools: Iterable[AssistantToolParam] | NotGiven = NOT_GIVEN,
        transcription: TranscriptionSettingsParam | NotGiven = NOT_GIVEN,
        voice_settings: VoiceSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantCreateResponse:
        """
        Create a new AI Assistant.

        Args:
          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api/inference/inference-embedding/get-models-public-models-get)
              to see all of your available models,

          dynamic_variables: Map of dynamic variables and their default values

          dynamic_variables_webhook_url: If the dynamic_variables_webhook_url is set for the assistant, we will send a
              request at the start of the conversation. See our
              [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
              for more information.

          greeting: Text that the assistant will use to start the conversation. This may be
              templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/assistants",
            body=maybe_transform(
                {
                    "instructions": instructions,
                    "model": model,
                    "name": name,
                    "description": description,
                    "dynamic_variables": dynamic_variables,
                    "dynamic_variables_webhook_url": dynamic_variables_webhook_url,
                    "enabled_features": enabled_features,
                    "greeting": greeting,
                    "insight_settings": insight_settings,
                    "llm_api_key_ref": llm_api_key_ref,
                    "messaging_settings": messaging_settings,
                    "privacy_settings": privacy_settings,
                    "telephony_settings": telephony_settings,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                },
                assistant_create_params.AssistantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantCreateResponse,
        )

    def retrieve(
        self,
        assistant_id: str,
        *,
        call_control_id: str | NotGiven = NOT_GIVEN,
        fetch_dynamic_variables_from_webhook: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantRetrieveResponse:
        """
        Retrieve an AI Assistant configuration by `assistant_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/ai/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "call_control_id": call_control_id,
                        "fetch_dynamic_variables_from_webhook": fetch_dynamic_variables_from_webhook,
                        "from_": from_,
                        "to": to,
                    },
                    assistant_retrieve_params.AssistantRetrieveParams,
                ),
            ),
            cast_to=AssistantRetrieveResponse,
        )

    def update(
        self,
        assistant_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        dynamic_variables_webhook_url: str | NotGiven = NOT_GIVEN,
        enabled_features: List[EnabledFeatures] | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        insight_settings: InsightSettingsParam | NotGiven = NOT_GIVEN,
        instructions: str | NotGiven = NOT_GIVEN,
        llm_api_key_ref: str | NotGiven = NOT_GIVEN,
        messaging_settings: MessagingSettingsParam | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        privacy_settings: PrivacySettingsParam | NotGiven = NOT_GIVEN,
        promote_to_main: bool | NotGiven = NOT_GIVEN,
        telephony_settings: TelephonySettingsParam | NotGiven = NOT_GIVEN,
        tools: Iterable[AssistantToolParam] | NotGiven = NOT_GIVEN,
        transcription: TranscriptionSettingsParam | NotGiven = NOT_GIVEN,
        voice_settings: VoiceSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update an AI Assistant's attributes.

        Args:
          dynamic_variables: Map of dynamic variables and their default values

          dynamic_variables_webhook_url: If the dynamic_variables_webhook_url is set for the assistant, we will send a
              request at the start of the conversation. See our
              [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
              for more information.

          greeting: Text that the assistant will use to start the conversation. This may be
              templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api/inference/inference-embedding/get-models-public-models-get)
              to see all of your available models,

          promote_to_main: Indicates whether the assistant should be promoted to the main version. Defaults
              to true.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            f"/ai/assistants/{assistant_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "dynamic_variables": dynamic_variables,
                    "dynamic_variables_webhook_url": dynamic_variables_webhook_url,
                    "enabled_features": enabled_features,
                    "greeting": greeting,
                    "insight_settings": insight_settings,
                    "instructions": instructions,
                    "llm_api_key_ref": llm_api_key_ref,
                    "messaging_settings": messaging_settings,
                    "model": model,
                    "name": name,
                    "privacy_settings": privacy_settings,
                    "promote_to_main": promote_to_main,
                    "telephony_settings": telephony_settings,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                },
                assistant_update_params.AssistantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantsList:
        """Retrieve a list of all AI Assistants configured by the user."""
        return self._get(
            "/ai/assistants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )

    def delete(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantDeleteResponse:
        """
        Delete an AI Assistant by `assistant_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._delete(
            f"/ai/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantDeleteResponse,
        )

    def chat(
        self,
        assistant_id: str,
        *,
        content: str,
        conversation_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantChatResponse:
        """
        This endpoint allows a client to send a chat message to a specific AI Assistant.
        The assistant processes the message and returns a relevant reply based on the
        current conversation context. Refer to the Conversation API to
        [create a conversation](https://developers.telnyx.com/api/inference/inference-embedding/create-new-conversation-public-conversations-post),
        [filter existing conversations](https://developers.telnyx.com/api/inference/inference-embedding/get-conversations-public-conversations-get),
        [fetch messages for a conversation](https://developers.telnyx.com/api/inference/inference-embedding/get-conversations-public-conversation-id-messages-get),
        and
        [manually add messages to a conversation](https://developers.telnyx.com/api/inference/inference-embedding/add-new-message).

        Args:
          content: The message content sent by the client to the assistant

          conversation_id: A unique identifier for the conversation thread, used to maintain context

          name: The optional display name of the user sending the message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            f"/ai/assistants/{assistant_id}/chat",
            body=maybe_transform(
                {
                    "content": content,
                    "conversation_id": conversation_id,
                    "name": name,
                },
                assistant_chat_params.AssistantChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantChatResponse,
        )

    def clone(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantCloneResponse:
        """
        Clone an existing assistant, excluding telephony and messaging settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            f"/ai/assistants/{assistant_id}/clone",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantCloneResponse,
        )

    def get_texml(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get an assistant texml by `assistant_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/ai/assistants/{assistant_id}/texml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def import_(
        self,
        *,
        api_key_ref: str,
        provider: Literal["elevenlabs", "vapi"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantsList:
        """Import assistants from external providers.

        Any assistant that has already been
        imported will be overwritten with its latest version from the importing
        provider.

        Args:
          api_key_ref: Integration secret pointer that refers to the API key for the external provider.
              This should be an identifier for an integration secret created via
              /v2/integration_secrets.

          provider: The external provider to import assistants from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/assistants/import",
            body=maybe_transform(
                {
                    "api_key_ref": api_key_ref,
                    "provider": provider,
                },
                assistant_import_params.AssistantImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )


class AsyncAssistantsResource(AsyncAPIResource):
    @cached_property
    def tests(self) -> AsyncTestsResource:
        return AsyncTestsResource(self._client)

    @cached_property
    def canary_deploys(self) -> AsyncCanaryDeploysResource:
        return AsyncCanaryDeploysResource(self._client)

    @cached_property
    def scheduled_events(self) -> AsyncScheduledEventsResource:
        return AsyncScheduledEventsResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssistantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssistantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssistantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAssistantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        instructions: str,
        model: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        dynamic_variables_webhook_url: str | NotGiven = NOT_GIVEN,
        enabled_features: List[EnabledFeatures] | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        insight_settings: InsightSettingsParam | NotGiven = NOT_GIVEN,
        llm_api_key_ref: str | NotGiven = NOT_GIVEN,
        messaging_settings: MessagingSettingsParam | NotGiven = NOT_GIVEN,
        privacy_settings: PrivacySettingsParam | NotGiven = NOT_GIVEN,
        telephony_settings: TelephonySettingsParam | NotGiven = NOT_GIVEN,
        tools: Iterable[AssistantToolParam] | NotGiven = NOT_GIVEN,
        transcription: TranscriptionSettingsParam | NotGiven = NOT_GIVEN,
        voice_settings: VoiceSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantCreateResponse:
        """
        Create a new AI Assistant.

        Args:
          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api/inference/inference-embedding/get-models-public-models-get)
              to see all of your available models,

          dynamic_variables: Map of dynamic variables and their default values

          dynamic_variables_webhook_url: If the dynamic_variables_webhook_url is set for the assistant, we will send a
              request at the start of the conversation. See our
              [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
              for more information.

          greeting: Text that the assistant will use to start the conversation. This may be
              templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/assistants",
            body=await async_maybe_transform(
                {
                    "instructions": instructions,
                    "model": model,
                    "name": name,
                    "description": description,
                    "dynamic_variables": dynamic_variables,
                    "dynamic_variables_webhook_url": dynamic_variables_webhook_url,
                    "enabled_features": enabled_features,
                    "greeting": greeting,
                    "insight_settings": insight_settings,
                    "llm_api_key_ref": llm_api_key_ref,
                    "messaging_settings": messaging_settings,
                    "privacy_settings": privacy_settings,
                    "telephony_settings": telephony_settings,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                },
                assistant_create_params.AssistantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantCreateResponse,
        )

    async def retrieve(
        self,
        assistant_id: str,
        *,
        call_control_id: str | NotGiven = NOT_GIVEN,
        fetch_dynamic_variables_from_webhook: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantRetrieveResponse:
        """
        Retrieve an AI Assistant configuration by `assistant_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/ai/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "call_control_id": call_control_id,
                        "fetch_dynamic_variables_from_webhook": fetch_dynamic_variables_from_webhook,
                        "from_": from_,
                        "to": to,
                    },
                    assistant_retrieve_params.AssistantRetrieveParams,
                ),
            ),
            cast_to=AssistantRetrieveResponse,
        )

    async def update(
        self,
        assistant_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        dynamic_variables_webhook_url: str | NotGiven = NOT_GIVEN,
        enabled_features: List[EnabledFeatures] | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        insight_settings: InsightSettingsParam | NotGiven = NOT_GIVEN,
        instructions: str | NotGiven = NOT_GIVEN,
        llm_api_key_ref: str | NotGiven = NOT_GIVEN,
        messaging_settings: MessagingSettingsParam | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        privacy_settings: PrivacySettingsParam | NotGiven = NOT_GIVEN,
        promote_to_main: bool | NotGiven = NOT_GIVEN,
        telephony_settings: TelephonySettingsParam | NotGiven = NOT_GIVEN,
        tools: Iterable[AssistantToolParam] | NotGiven = NOT_GIVEN,
        transcription: TranscriptionSettingsParam | NotGiven = NOT_GIVEN,
        voice_settings: VoiceSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Update an AI Assistant's attributes.

        Args:
          dynamic_variables: Map of dynamic variables and their default values

          dynamic_variables_webhook_url: If the dynamic_variables_webhook_url is set for the assistant, we will send a
              request at the start of the conversation. See our
              [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
              for more information.

          greeting: Text that the assistant will use to start the conversation. This may be
              templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api/inference/inference-embedding/get-models-public-models-get)
              to see all of your available models,

          promote_to_main: Indicates whether the assistant should be promoted to the main version. Defaults
              to true.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            f"/ai/assistants/{assistant_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "dynamic_variables": dynamic_variables,
                    "dynamic_variables_webhook_url": dynamic_variables_webhook_url,
                    "enabled_features": enabled_features,
                    "greeting": greeting,
                    "insight_settings": insight_settings,
                    "instructions": instructions,
                    "llm_api_key_ref": llm_api_key_ref,
                    "messaging_settings": messaging_settings,
                    "model": model,
                    "name": name,
                    "privacy_settings": privacy_settings,
                    "promote_to_main": promote_to_main,
                    "telephony_settings": telephony_settings,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                },
                assistant_update_params.AssistantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantsList:
        """Retrieve a list of all AI Assistants configured by the user."""
        return await self._get(
            "/ai/assistants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )

    async def delete(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantDeleteResponse:
        """
        Delete an AI Assistant by `assistant_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._delete(
            f"/ai/assistants/{assistant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantDeleteResponse,
        )

    async def chat(
        self,
        assistant_id: str,
        *,
        content: str,
        conversation_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantChatResponse:
        """
        This endpoint allows a client to send a chat message to a specific AI Assistant.
        The assistant processes the message and returns a relevant reply based on the
        current conversation context. Refer to the Conversation API to
        [create a conversation](https://developers.telnyx.com/api/inference/inference-embedding/create-new-conversation-public-conversations-post),
        [filter existing conversations](https://developers.telnyx.com/api/inference/inference-embedding/get-conversations-public-conversations-get),
        [fetch messages for a conversation](https://developers.telnyx.com/api/inference/inference-embedding/get-conversations-public-conversation-id-messages-get),
        and
        [manually add messages to a conversation](https://developers.telnyx.com/api/inference/inference-embedding/add-new-message).

        Args:
          content: The message content sent by the client to the assistant

          conversation_id: A unique identifier for the conversation thread, used to maintain context

          name: The optional display name of the user sending the message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            f"/ai/assistants/{assistant_id}/chat",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "conversation_id": conversation_id,
                    "name": name,
                },
                assistant_chat_params.AssistantChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantChatResponse,
        )

    async def clone(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantCloneResponse:
        """
        Clone an existing assistant, excluding telephony and messaging settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            f"/ai/assistants/{assistant_id}/clone",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantCloneResponse,
        )

    async def get_texml(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get an assistant texml by `assistant_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/ai/assistants/{assistant_id}/texml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def import_(
        self,
        *,
        api_key_ref: str,
        provider: Literal["elevenlabs", "vapi"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantsList:
        """Import assistants from external providers.

        Any assistant that has already been
        imported will be overwritten with its latest version from the importing
        provider.

        Args:
          api_key_ref: Integration secret pointer that refers to the API key for the external provider.
              This should be an identifier for an integration secret created via
              /v2/integration_secrets.

          provider: The external provider to import assistants from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/assistants/import",
            body=await async_maybe_transform(
                {
                    "api_key_ref": api_key_ref,
                    "provider": provider,
                },
                assistant_import_params.AssistantImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )


class AssistantsResourceWithRawResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.create = to_raw_response_wrapper(
            assistants.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assistants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assistants.update,
        )
        self.list = to_raw_response_wrapper(
            assistants.list,
        )
        self.delete = to_raw_response_wrapper(
            assistants.delete,
        )
        self.chat = to_raw_response_wrapper(
            assistants.chat,
        )
        self.clone = to_raw_response_wrapper(
            assistants.clone,
        )
        self.get_texml = to_raw_response_wrapper(
            assistants.get_texml,
        )
        self.import_ = to_raw_response_wrapper(
            assistants.import_,
        )

    @cached_property
    def tests(self) -> TestsResourceWithRawResponse:
        return TestsResourceWithRawResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> CanaryDeploysResourceWithRawResponse:
        return CanaryDeploysResourceWithRawResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> ScheduledEventsResourceWithRawResponse:
        return ScheduledEventsResourceWithRawResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._assistants.versions)


class AsyncAssistantsResourceWithRawResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.create = async_to_raw_response_wrapper(
            assistants.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assistants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assistants.update,
        )
        self.list = async_to_raw_response_wrapper(
            assistants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assistants.delete,
        )
        self.chat = async_to_raw_response_wrapper(
            assistants.chat,
        )
        self.clone = async_to_raw_response_wrapper(
            assistants.clone,
        )
        self.get_texml = async_to_raw_response_wrapper(
            assistants.get_texml,
        )
        self.import_ = async_to_raw_response_wrapper(
            assistants.import_,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithRawResponse:
        return AsyncTestsResourceWithRawResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> AsyncCanaryDeploysResourceWithRawResponse:
        return AsyncCanaryDeploysResourceWithRawResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> AsyncScheduledEventsResourceWithRawResponse:
        return AsyncScheduledEventsResourceWithRawResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._assistants.versions)


class AssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AssistantsResource) -> None:
        self._assistants = assistants

        self.create = to_streamed_response_wrapper(
            assistants.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assistants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assistants.update,
        )
        self.list = to_streamed_response_wrapper(
            assistants.list,
        )
        self.delete = to_streamed_response_wrapper(
            assistants.delete,
        )
        self.chat = to_streamed_response_wrapper(
            assistants.chat,
        )
        self.clone = to_streamed_response_wrapper(
            assistants.clone,
        )
        self.get_texml = to_streamed_response_wrapper(
            assistants.get_texml,
        )
        self.import_ = to_streamed_response_wrapper(
            assistants.import_,
        )

    @cached_property
    def tests(self) -> TestsResourceWithStreamingResponse:
        return TestsResourceWithStreamingResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> CanaryDeploysResourceWithStreamingResponse:
        return CanaryDeploysResourceWithStreamingResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> ScheduledEventsResourceWithStreamingResponse:
        return ScheduledEventsResourceWithStreamingResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._assistants.versions)


class AsyncAssistantsResourceWithStreamingResponse:
    def __init__(self, assistants: AsyncAssistantsResource) -> None:
        self._assistants = assistants

        self.create = async_to_streamed_response_wrapper(
            assistants.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assistants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assistants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assistants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assistants.delete,
        )
        self.chat = async_to_streamed_response_wrapper(
            assistants.chat,
        )
        self.clone = async_to_streamed_response_wrapper(
            assistants.clone,
        )
        self.get_texml = async_to_streamed_response_wrapper(
            assistants.get_texml,
        )
        self.import_ = async_to_streamed_response_wrapper(
            assistants.import_,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithStreamingResponse:
        return AsyncTestsResourceWithStreamingResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> AsyncCanaryDeploysResourceWithStreamingResponse:
        return AsyncCanaryDeploysResourceWithStreamingResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> AsyncScheduledEventsResourceWithStreamingResponse:
        return AsyncScheduledEventsResourceWithStreamingResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._assistants.versions)
