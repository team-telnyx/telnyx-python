# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.assistants import version_update_params, version_retrieve_params
from ....types.ai.assistants_list import AssistantsList
from ....types.ai.enabled_features import EnabledFeatures
from ....types.ai.assistant_tool_param import AssistantToolParam
from ....types.ai.voice_settings_param import VoiceSettingsParam
from ....types.ai.insight_settings_param import InsightSettingsParam
from ....types.ai.privacy_settings_param import PrivacySettingsParam
from ....types.ai.messaging_settings_param import MessagingSettingsParam
from ....types.ai.telephony_settings_param import TelephonySettingsParam
from ....types.ai.transcription_settings_param import TranscriptionSettingsParam
from ....types.ai.assistants.version_update_response import VersionUpdateResponse
from ....types.ai.assistants.version_promote_response import VersionPromoteResponse
from ....types.ai.assistants.version_retrieve_response import VersionRetrieveResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        version_id: str,
        *,
        assistant_id: str,
        include_mcp_servers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionRetrieveResponse:
        """
        Retrieves a specific version of an assistant by assistant_id and version_id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._get(
            f"/ai/assistants/{assistant_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_mcp_servers": include_mcp_servers}, version_retrieve_params.VersionRetrieveParams
                ),
            ),
            cast_to=VersionRetrieveResponse,
        )

    def update(
        self,
        version_id: str,
        *,
        assistant_id: str,
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
    ) -> VersionUpdateResponse:
        """Updates the configuration of a specific assistant version.

        Can not update main
        version

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

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._post(
            f"/ai/assistants/{assistant_id}/versions/{version_id}",
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
                    "telephony_settings": telephony_settings,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                },
                version_update_params.VersionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionUpdateResponse,
        )

    def list(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantsList:
        """
        Retrieves all versions of a specific assistant with complete configuration and
        metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/ai/assistants/{assistant_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )

    def delete(
        self,
        version_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Permanently removes a specific version of an assistant.

        Can not delete main
        version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/assistants/{assistant_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def promote(
        self,
        version_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionPromoteResponse:
        """
        Promotes a specific version to be the main/current version of the assistant.
        This will delete any existing canary deploy configuration and send all live
        production traffic to this version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._post(
            f"/ai/assistants/{assistant_id}/versions/{version_id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionPromoteResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        version_id: str,
        *,
        assistant_id: str,
        include_mcp_servers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionRetrieveResponse:
        """
        Retrieves a specific version of an assistant by assistant_id and version_id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._get(
            f"/ai/assistants/{assistant_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_mcp_servers": include_mcp_servers}, version_retrieve_params.VersionRetrieveParams
                ),
            ),
            cast_to=VersionRetrieveResponse,
        )

    async def update(
        self,
        version_id: str,
        *,
        assistant_id: str,
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
    ) -> VersionUpdateResponse:
        """Updates the configuration of a specific assistant version.

        Can not update main
        version

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

          tools: The tools that the assistant can use. These may be templated with
              [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._post(
            f"/ai/assistants/{assistant_id}/versions/{version_id}",
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
                    "telephony_settings": telephony_settings,
                    "tools": tools,
                    "transcription": transcription,
                    "voice_settings": voice_settings,
                },
                version_update_params.VersionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionUpdateResponse,
        )

    async def list(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantsList:
        """
        Retrieves all versions of a specific assistant with complete configuration and
        metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/ai/assistants/{assistant_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantsList,
        )

    async def delete(
        self,
        version_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Permanently removes a specific version of an assistant.

        Can not delete main
        version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/assistants/{assistant_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def promote(
        self,
        version_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionPromoteResponse:
        """
        Promotes a specific version to be the main/current version of the assistant.
        This will delete any existing canary deploy configuration and send all live
        production traffic to this version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._post(
            f"/ai/assistants/{assistant_id}/versions/{version_id}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionPromoteResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            versions.update,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.promote = to_raw_response_wrapper(
            versions.promote,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            versions.update,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.promote = async_to_raw_response_wrapper(
            versions.promote,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            versions.update,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.promote = to_streamed_response_wrapper(
            versions.promote,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            versions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.promote = async_to_streamed_response_wrapper(
            versions.promote,
        )
