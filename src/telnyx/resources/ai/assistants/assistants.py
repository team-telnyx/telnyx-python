# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
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
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import (
    assistant_chat_params,
    assistant_create_params,
    assistant_update_params,
    assistant_imports_params,
    assistant_retrieve_params,
    assistant_send_sms_params,
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
from ....types.ai.inference_embedding import InferenceEmbedding
from ....types.ai.assistant_tool_param import AssistantToolParam
from ....types.ai.voice_settings_param import VoiceSettingsParam
from ....types.ai.widget_settings_param import WidgetSettingsParam
from ....types.ai.insight_settings_param import InsightSettingsParam
from ....types.ai.privacy_settings_param import PrivacySettingsParam
from ....types.ai.assistant_chat_response import AssistantChatResponse
from ....types.ai.messaging_settings_param import MessagingSettingsParam
from ....types.ai.telephony_settings_param import TelephonySettingsParam
from ....types.ai.assistant_delete_response import AssistantDeleteResponse
from ....types.ai.assistant_send_sms_response import AssistantSendSMSResponse
from ....types.ai.transcription_settings_param import TranscriptionSettingsParam

__all__ = ["AssistantsResource", "AsyncAssistantsResource"]


class AssistantsResource(SyncAPIResource):
    """Configure AI assistant specifications"""

    @cached_property
    def tests(self) -> TestsResource:
        """Configure AI assistant specifications"""
        return TestsResource(self._client)

    @cached_property
    def canary_deploys(self) -> CanaryDeploysResource:
        """Configure AI assistant specifications"""
        return CanaryDeploysResource(self._client)

    @cached_property
    def scheduled_events(self) -> ScheduledEventsResource:
        """Configure AI assistant specifications"""
        return ScheduledEventsResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        """Configure AI assistant specifications"""
        return ToolsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        """Configure AI assistant specifications"""
        return VersionsResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        """Configure AI assistant specifications"""
        return TagsResource(self._client)

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
        description: str | Omit = omit,
        dynamic_variables: Dict[str, object] | Omit = omit,
        dynamic_variables_webhook_url: str | Omit = omit,
        enabled_features: List[EnabledFeatures] | Omit = omit,
        greeting: str | Omit = omit,
        insight_settings: InsightSettingsParam | Omit = omit,
        llm_api_key_ref: str | Omit = omit,
        messaging_settings: MessagingSettingsParam | Omit = omit,
        observability_settings: assistant_create_params.ObservabilitySettings | Omit = omit,
        privacy_settings: PrivacySettingsParam | Omit = omit,
        telephony_settings: TelephonySettingsParam | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        tools: Iterable[AssistantToolParam] | Omit = omit,
        transcription: TranscriptionSettingsParam | Omit = omit,
        voice_settings: VoiceSettingsParam | Omit = omit,
        widget_settings: WidgetSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
        """
        Create a new AI Assistant.

        Args:
          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
              to see all of your available models,

          dynamic_variables: Map of dynamic variables and their default values

          dynamic_variables_webhook_url: If the dynamic_variables_webhook_url is set for the assistant, we will send a
              request at the start of the conversation. See our
              [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
              for more information.

          greeting: Text that the assistant will use to start the conversation. This may be
              templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
              Use an empty string to have the assistant wait for the user to speak first. Use
              the special value `<assistant-speaks-first-with-model-generated-message>` to
              have the assistant generate the greeting based on the system instructions.

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          widget_settings: Configuration settings for the assistant's web widget.

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
                    "observability_settings": observability_settings,
                    "privacy_settings": privacy_settings,
                    "telephony_settings": telephony_settings,
                    "tool_ids": tool_ids,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                    "widget_settings": widget_settings,
                },
                assistant_create_params.AssistantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceEmbedding,
        )

    def retrieve(
        self,
        assistant_id: str,
        *,
        call_control_id: str | Omit = omit,
        fetch_dynamic_variables_from_webhook: bool | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
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
            path_template("/ai/assistants/{assistant_id}", assistant_id=assistant_id),
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
            cast_to=InferenceEmbedding,
        )

    def update(
        self,
        assistant_id: str,
        *,
        description: str | Omit = omit,
        dynamic_variables: Dict[str, object] | Omit = omit,
        dynamic_variables_webhook_url: str | Omit = omit,
        enabled_features: List[EnabledFeatures] | Omit = omit,
        greeting: str | Omit = omit,
        insight_settings: InsightSettingsParam | Omit = omit,
        instructions: str | Omit = omit,
        llm_api_key_ref: str | Omit = omit,
        messaging_settings: MessagingSettingsParam | Omit = omit,
        model: str | Omit = omit,
        name: str | Omit = omit,
        observability_settings: assistant_update_params.ObservabilitySettings | Omit = omit,
        privacy_settings: PrivacySettingsParam | Omit = omit,
        promote_to_main: bool | Omit = omit,
        telephony_settings: TelephonySettingsParam | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        tools: Iterable[AssistantToolParam] | Omit = omit,
        transcription: TranscriptionSettingsParam | Omit = omit,
        voice_settings: VoiceSettingsParam | Omit = omit,
        widget_settings: WidgetSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
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
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
              Use an empty string to have the assistant wait for the user to speak first. Use
              the special value `<assistant-speaks-first-with-model-generated-message>` to
              have the assistant generate the greeting based on the system instructions.

          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
              to see all of your available models,

          promote_to_main: Indicates whether the assistant should be promoted to the main version. Defaults
              to true.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          widget_settings: Configuration settings for the assistant's web widget.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            path_template("/ai/assistants/{assistant_id}", assistant_id=assistant_id),
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
                    "observability_settings": observability_settings,
                    "privacy_settings": privacy_settings,
                    "promote_to_main": promote_to_main,
                    "telephony_settings": telephony_settings,
                    "tool_ids": tool_ids,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                    "widget_settings": widget_settings,
                },
                assistant_update_params.AssistantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceEmbedding,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ai/assistants/{assistant_id}", assistant_id=assistant_id),
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
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantChatResponse:
        """
        This endpoint allows a client to send a chat message to a specific AI Assistant.
        The assistant processes the message and returns a relevant reply based on the
        current conversation context. Refer to the Conversation API to
        [create a conversation](https://developers.telnyx.com/api-reference/conversations/create-a-conversation),
        [filter existing conversations](https://developers.telnyx.com/api-reference/conversations/list-conversations),
        [fetch messages for a conversation](https://developers.telnyx.com/api-reference/conversations/get-conversation-messages),
        and
        [manually add messages to a conversation](https://developers.telnyx.com/api-reference/conversations/create-message).

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
            path_template("/ai/assistants/{assistant_id}/chat", assistant_id=assistant_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
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
            path_template("/ai/assistants/{assistant_id}/clone", assistant_id=assistant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceEmbedding,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ai/assistants/{assistant_id}/texml", assistant_id=assistant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def imports(
        self,
        *,
        api_key_ref: str,
        provider: Literal["elevenlabs", "vapi", "retell"],
        import_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          import_ids: Optional list of assistant IDs to import from the external provider. If not
              provided, all assistants will be imported.

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
                    "import_ids": import_ids,
                },
                assistant_imports_params.AssistantImportsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )

    def send_sms(
        self,
        assistant_id: str,
        *,
        from_: str,
        to: str,
        conversation_metadata: Dict[str, Union[str, int, bool]] | Omit = omit,
        should_create_conversation: bool | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantSendSMSResponse:
        """Send an SMS message for an assistant.

        This endpoint:

        1. Validates the assistant exists and has messaging profile configured
        2. If should_create_conversation is true, creates a new conversation with
           metadata
        3. Sends the SMS message (If `text` is set, this will be sent. Otherwise, if
           this is the first message in the conversation and the assistant has a
           `greeting` configured, this will be sent. Otherwise the assistant will
           generate the text to send.)
        4. Updates conversation metadata if provided
        5. Returns the conversation ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            path_template("/ai/assistants/{assistant_id}/chat/sms", assistant_id=assistant_id),
            body=maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "conversation_metadata": conversation_metadata,
                    "should_create_conversation": should_create_conversation,
                    "text": text,
                },
                assistant_send_sms_params.AssistantSendSMSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantSendSMSResponse,
        )


class AsyncAssistantsResource(AsyncAPIResource):
    """Configure AI assistant specifications"""

    @cached_property
    def tests(self) -> AsyncTestsResource:
        """Configure AI assistant specifications"""
        return AsyncTestsResource(self._client)

    @cached_property
    def canary_deploys(self) -> AsyncCanaryDeploysResource:
        """Configure AI assistant specifications"""
        return AsyncCanaryDeploysResource(self._client)

    @cached_property
    def scheduled_events(self) -> AsyncScheduledEventsResource:
        """Configure AI assistant specifications"""
        return AsyncScheduledEventsResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        """Configure AI assistant specifications"""
        return AsyncToolsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Configure AI assistant specifications"""
        return AsyncVersionsResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        """Configure AI assistant specifications"""
        return AsyncTagsResource(self._client)

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
        description: str | Omit = omit,
        dynamic_variables: Dict[str, object] | Omit = omit,
        dynamic_variables_webhook_url: str | Omit = omit,
        enabled_features: List[EnabledFeatures] | Omit = omit,
        greeting: str | Omit = omit,
        insight_settings: InsightSettingsParam | Omit = omit,
        llm_api_key_ref: str | Omit = omit,
        messaging_settings: MessagingSettingsParam | Omit = omit,
        observability_settings: assistant_create_params.ObservabilitySettings | Omit = omit,
        privacy_settings: PrivacySettingsParam | Omit = omit,
        telephony_settings: TelephonySettingsParam | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        tools: Iterable[AssistantToolParam] | Omit = omit,
        transcription: TranscriptionSettingsParam | Omit = omit,
        voice_settings: VoiceSettingsParam | Omit = omit,
        widget_settings: WidgetSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
        """
        Create a new AI Assistant.

        Args:
          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
              to see all of your available models,

          dynamic_variables: Map of dynamic variables and their default values

          dynamic_variables_webhook_url: If the dynamic_variables_webhook_url is set for the assistant, we will send a
              request at the start of the conversation. See our
              [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
              for more information.

          greeting: Text that the assistant will use to start the conversation. This may be
              templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
              Use an empty string to have the assistant wait for the user to speak first. Use
              the special value `<assistant-speaks-first-with-model-generated-message>` to
              have the assistant generate the greeting based on the system instructions.

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          widget_settings: Configuration settings for the assistant's web widget.

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
                    "observability_settings": observability_settings,
                    "privacy_settings": privacy_settings,
                    "telephony_settings": telephony_settings,
                    "tool_ids": tool_ids,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                    "widget_settings": widget_settings,
                },
                assistant_create_params.AssistantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceEmbedding,
        )

    async def retrieve(
        self,
        assistant_id: str,
        *,
        call_control_id: str | Omit = omit,
        fetch_dynamic_variables_from_webhook: bool | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
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
            path_template("/ai/assistants/{assistant_id}", assistant_id=assistant_id),
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
            cast_to=InferenceEmbedding,
        )

    async def update(
        self,
        assistant_id: str,
        *,
        description: str | Omit = omit,
        dynamic_variables: Dict[str, object] | Omit = omit,
        dynamic_variables_webhook_url: str | Omit = omit,
        enabled_features: List[EnabledFeatures] | Omit = omit,
        greeting: str | Omit = omit,
        insight_settings: InsightSettingsParam | Omit = omit,
        instructions: str | Omit = omit,
        llm_api_key_ref: str | Omit = omit,
        messaging_settings: MessagingSettingsParam | Omit = omit,
        model: str | Omit = omit,
        name: str | Omit = omit,
        observability_settings: assistant_update_params.ObservabilitySettings | Omit = omit,
        privacy_settings: PrivacySettingsParam | Omit = omit,
        promote_to_main: bool | Omit = omit,
        telephony_settings: TelephonySettingsParam | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        tools: Iterable[AssistantToolParam] | Omit = omit,
        transcription: TranscriptionSettingsParam | Omit = omit,
        voice_settings: VoiceSettingsParam | Omit = omit,
        widget_settings: WidgetSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
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
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
              Use an empty string to have the assistant wait for the user to speak first. Use
              the special value `<assistant-speaks-first-with-model-generated-message>` to
              have the assistant generate the greeting based on the system instructions.

          instructions: System instructions for the assistant. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          llm_api_key_ref: This is only needed when using third-party inference providers. The `identifier`
              for an integration secret
              [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              that refers to your LLM provider's API key. Warning: Free plans are unlikely to
              work with this integration.

          model: ID of the model to use. You can use the
              [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
              to see all of your available models,

          promote_to_main: Indicates whether the assistant should be promoted to the main version. Defaults
              to true.

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          widget_settings: Configuration settings for the assistant's web widget.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            path_template("/ai/assistants/{assistant_id}", assistant_id=assistant_id),
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
                    "observability_settings": observability_settings,
                    "privacy_settings": privacy_settings,
                    "promote_to_main": promote_to_main,
                    "telephony_settings": telephony_settings,
                    "tool_ids": tool_ids,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                    "widget_settings": widget_settings,
                },
                assistant_update_params.AssistantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceEmbedding,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ai/assistants/{assistant_id}", assistant_id=assistant_id),
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
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantChatResponse:
        """
        This endpoint allows a client to send a chat message to a specific AI Assistant.
        The assistant processes the message and returns a relevant reply based on the
        current conversation context. Refer to the Conversation API to
        [create a conversation](https://developers.telnyx.com/api-reference/conversations/create-a-conversation),
        [filter existing conversations](https://developers.telnyx.com/api-reference/conversations/list-conversations),
        [fetch messages for a conversation](https://developers.telnyx.com/api-reference/conversations/get-conversation-messages),
        and
        [manually add messages to a conversation](https://developers.telnyx.com/api-reference/conversations/create-message).

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
            path_template("/ai/assistants/{assistant_id}/chat", assistant_id=assistant_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceEmbedding:
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
            path_template("/ai/assistants/{assistant_id}/clone", assistant_id=assistant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceEmbedding,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/ai/assistants/{assistant_id}/texml", assistant_id=assistant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def imports(
        self,
        *,
        api_key_ref: str,
        provider: Literal["elevenlabs", "vapi", "retell"],
        import_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          import_ids: Optional list of assistant IDs to import from the external provider. If not
              provided, all assistants will be imported.

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
                    "import_ids": import_ids,
                },
                assistant_imports_params.AssistantImportsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )

    async def send_sms(
        self,
        assistant_id: str,
        *,
        from_: str,
        to: str,
        conversation_metadata: Dict[str, Union[str, int, bool]] | Omit = omit,
        should_create_conversation: bool | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantSendSMSResponse:
        """Send an SMS message for an assistant.

        This endpoint:

        1. Validates the assistant exists and has messaging profile configured
        2. If should_create_conversation is true, creates a new conversation with
           metadata
        3. Sends the SMS message (If `text` is set, this will be sent. Otherwise, if
           this is the first message in the conversation and the assistant has a
           `greeting` configured, this will be sent. Otherwise the assistant will
           generate the text to send.)
        4. Updates conversation metadata if provided
        5. Returns the conversation ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            path_template("/ai/assistants/{assistant_id}/chat/sms", assistant_id=assistant_id),
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "conversation_metadata": conversation_metadata,
                    "should_create_conversation": should_create_conversation,
                    "text": text,
                },
                assistant_send_sms_params.AssistantSendSMSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantSendSMSResponse,
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
        self.imports = to_raw_response_wrapper(
            assistants.imports,
        )
        self.send_sms = to_raw_response_wrapper(
            assistants.send_sms,
        )

    @cached_property
    def tests(self) -> TestsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return TestsResourceWithRawResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> CanaryDeploysResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return CanaryDeploysResourceWithRawResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> ScheduledEventsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return ScheduledEventsResourceWithRawResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return ToolsResourceWithRawResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return VersionsResourceWithRawResponse(self._assistants.versions)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return TagsResourceWithRawResponse(self._assistants.tags)


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
        self.imports = async_to_raw_response_wrapper(
            assistants.imports,
        )
        self.send_sms = async_to_raw_response_wrapper(
            assistants.send_sms,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncTestsResourceWithRawResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> AsyncCanaryDeploysResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncCanaryDeploysResourceWithRawResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> AsyncScheduledEventsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncScheduledEventsResourceWithRawResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncToolsResourceWithRawResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncVersionsResourceWithRawResponse(self._assistants.versions)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncTagsResourceWithRawResponse(self._assistants.tags)


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
        self.imports = to_streamed_response_wrapper(
            assistants.imports,
        )
        self.send_sms = to_streamed_response_wrapper(
            assistants.send_sms,
        )

    @cached_property
    def tests(self) -> TestsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return TestsResourceWithStreamingResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> CanaryDeploysResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return CanaryDeploysResourceWithStreamingResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> ScheduledEventsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return ScheduledEventsResourceWithStreamingResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return ToolsResourceWithStreamingResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return VersionsResourceWithStreamingResponse(self._assistants.versions)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return TagsResourceWithStreamingResponse(self._assistants.tags)


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
        self.imports = async_to_streamed_response_wrapper(
            assistants.imports,
        )
        self.send_sms = async_to_streamed_response_wrapper(
            assistants.send_sms,
        )

    @cached_property
    def tests(self) -> AsyncTestsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncTestsResourceWithStreamingResponse(self._assistants.tests)

    @cached_property
    def canary_deploys(self) -> AsyncCanaryDeploysResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncCanaryDeploysResourceWithStreamingResponse(self._assistants.canary_deploys)

    @cached_property
    def scheduled_events(self) -> AsyncScheduledEventsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncScheduledEventsResourceWithStreamingResponse(self._assistants.scheduled_events)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncToolsResourceWithStreamingResponse(self._assistants.tools)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncVersionsResourceWithStreamingResponse(self._assistants.versions)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncTagsResourceWithStreamingResponse(self._assistants.tags)
