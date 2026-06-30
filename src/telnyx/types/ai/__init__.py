# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .assistant_tool import AssistantTool as AssistantTool
from .execution_mode import ExecutionMode as ExecutionMode
from .assistant_param import AssistantParam as AssistantParam
from .flow_edge_param import FlowEdgeParam as FlowEdgeParam
from .bucket_ids_param import BucketIDsParam as BucketIDsParam
from .enabled_features import EnabledFeatures as EnabledFeatures
from .tool_list_params import ToolListParams as ToolListParams
from .hangup_tool_param import HangupToolParam as HangupToolParam
from .prompt_sync_status import PromptSyncStatus as PromptSyncStatus
from .tool_create_params import ToolCreateParams as ToolCreateParams
from .tool_update_params import ToolUpdateParams as ToolUpdateParams
from .webhook_tool_param import WebhookToolParam as WebhookToolParam
from .cluster_list_params import ClusterListParams as ClusterListParams
from .mission_list_params import MissionListParams as MissionListParams
from .node_position_param import NodePositionParam as NodePositionParam
from .transfer_tool_param import TransferToolParam as TransferToolParam
from .assistant_tool_param import AssistantToolParam as AssistantToolParam
from .embedding_url_params import EmbeddingURLParams as EmbeddingURLParams
from .observability_status import ObservabilityStatus as ObservabilityStatus
from .retrieval_tool_param import RetrievalToolParam as RetrievalToolParam
from .voice_settings_param import VoiceSettingsParam as VoiceSettingsParam
from .assistant_chat_params import AssistantChatParams as AssistantChatParams
from .authentication_method import AuthenticationMethod as AuthenticationMethod
from .embedding_list_params import EmbeddingListParams as EmbeddingListParams
from .mission_create_params import MissionCreateParams as MissionCreateParams
from .widget_settings_param import WidgetSettingsParam as WidgetSettingsParam
from .background_task_status import BackgroundTaskStatus as BackgroundTaskStatus
from .cluster_compute_params import ClusterComputeParams as ClusterComputeParams
from .external_llm_req_param import ExternalLlmReqParam as ExternalLlmReqParam
from .insight_settings_param import InsightSettingsParam as InsightSettingsParam
from .mcp_server_list_params import McpServerListParams as McpServerListParams
from .privacy_settings_param import PrivacySettingsParam as PrivacySettingsParam
from .assistant_create_params import AssistantCreateParams as AssistantCreateParams
from .assistant_update_params import AssistantUpdateParams as AssistantUpdateParams
from .audio_transcribe_params import AudioTranscribeParams as AudioTranscribeParams
from .cluster_retrieve_params import ClusterRetrieveParams as ClusterRetrieveParams
from .embedding_create_params import EmbeddingCreateParams as EmbeddingCreateParams
from .observability_req_param import ObservabilityReqParam as ObservabilityReqParam
from .assistant_imports_params import AssistantImportsParams as AssistantImportsParams
from .conversation_list_params import ConversationListParams as ConversationListParams
from .hangup_tool_params_param import HangupToolParamsParam as HangupToolParamsParam
from .mcp_server_create_params import McpServerCreateParams as McpServerCreateParams
from .mcp_server_update_params import McpServerUpdateParams as McpServerUpdateParams
from .messaging_settings_param import MessagingSettingsParam as MessagingSettingsParam
from .telephony_settings_param import TelephonySettingsParam as TelephonySettingsParam
from .assistant_retrieve_params import AssistantRetrieveParams as AssistantRetrieveParams
from .assistant_send_sms_params import AssistantSendSMSParams as AssistantSendSMSParams
from .fallback_config_req_param import FallbackConfigReqParam as FallbackConfigReqParam
from .start_speaking_plan_param import StartSpeakingPlanParam as StartSpeakingPlanParam
from .assistant_mcp_server_param import AssistantMcpServerParam as AssistantMcpServerParam
from .cluster_fetch_graph_params import ClusterFetchGraphParams as ClusterFetchGraphParams
from .conversation_create_params import ConversationCreateParams as ConversationCreateParams
from .conversation_update_params import ConversationUpdateParams as ConversationUpdateParams
from .mission_list_events_params import MissionListEventsParams as MissionListEventsParams
from .assistant_integration_param import AssistantIntegrationParam as AssistantIntegrationParam
from .conversation_flow_req_param import ConversationFlowReqParam as ConversationFlowReqParam
from .assistant_get_texml_response import AssistantGetTexmlResponse as AssistantGetTexmlResponse
from .transcription_settings_param import TranscriptionSettingsParam as TranscriptionSettingsParam
from .audio_visualizer_config_param import AudioVisualizerConfigParam as AudioVisualizerConfigParam
from .chat_create_completion_params import ChatCreateCompletionParams as ChatCreateCompletionParams
from .mission_update_mission_params import MissionUpdateMissionParams as MissionUpdateMissionParams
from .openai_create_response_params import OpenAICreateResponseParams as OpenAICreateResponseParams
from .chat_create_completion_response import ChatCreateCompletionResponse as ChatCreateCompletionResponse
from .conversation_add_message_params import ConversationAddMessageParams as ConversationAddMessageParams
from .openai_create_response_response import OpenAICreateResponseResponse as OpenAICreateResponseResponse
from .embedding_similarity_search_params import EmbeddingSimilaritySearchParams as EmbeddingSimilaritySearchParams
from .transcription_settings_config_param import TranscriptionSettingsConfigParam as TranscriptionSettingsConfigParam
from .post_conversation_settings_req_param import PostConversationSettingsReqParam as PostConversationSettingsReqParam
from .transcription_endpointing_plan_param import TranscriptionEndpointingPlanParam as TranscriptionEndpointingPlanParam
from .inference_embedding_webhook_tool_params_param import (
    InferenceEmbeddingWebhookToolParamsParam as InferenceEmbeddingWebhookToolParamsParam,
)
from .inference_embedding_interruption_settings_param import (
    InferenceEmbeddingInterruptionSettingsParam as InferenceEmbeddingInterruptionSettingsParam,
)

if TYPE_CHECKING:
    from .flow_edge import FlowEdge as FlowEdge
    from .bucket_ids import BucketIDs as BucketIDs
    from .mcp_server import McpServer as McpServer
    from .hangup_tool import HangupTool as HangupTool
    from .integration import Integration as Integration
    from .conversation import Conversation as Conversation
    from .external_llm import ExternalLlm as ExternalLlm
    from .mission_data import MissionData as MissionData
    from .node_position import NodePosition as NodePosition
    from .observability import Observability as Observability
    from .retrieval_tool import RetrievalTool as RetrievalTool
    from .voice_settings import VoiceSettings as VoiceSettings
    from .assistants_list import AssistantsList as AssistantsList
    from .fallback_config import FallbackConfig as FallbackConfig
    from .import_metadata import ImportMetadata as ImportMetadata
    from .widget_settings import WidgetSettings as WidgetSettings
    from .insight_settings import InsightSettings as InsightSettings
    from .mission_response import MissionResponse as MissionResponse
    from .privacy_settings import PrivacySettings as PrivacySettings
    from .recursive_cluster import RecursiveCluster as RecursiveCluster
    from .embedding_response import EmbeddingResponse as EmbeddingResponse
    from .hangup_tool_params import HangupToolParams as HangupToolParams
    from .messaging_settings import MessagingSettings as MessagingSettings
    from .telephony_settings import TelephonySettings as TelephonySettings
    from .inference_embedding import InferenceEmbedding as InferenceEmbedding
    from .start_speaking_plan import StartSpeakingPlan as StartSpeakingPlan
    from .assistant_mcp_server import AssistantMcpServer as AssistantMcpServer
    from .events_list_response import EventsListResponse as EventsListResponse
    from .shared_tool_response import SharedToolResponse as SharedToolResponse
    from .assistant_integration import AssistantIntegration as AssistantIntegration
    from .cluster_list_response import ClusterListResponse as ClusterListResponse
    from .transcription_settings import TranscriptionSettings as TranscriptionSettings
    from .assistant_chat_response import AssistantChatResponse as AssistantChatResponse
    from .audio_visualizer_config import AudioVisualizerConfig as AudioVisualizerConfig
    from .embedding_list_response import EmbeddingListResponse as EmbeddingListResponse
    from .cluster_compute_response import ClusterComputeResponse as ClusterComputeResponse
    from .assistant_delete_response import AssistantDeleteResponse as AssistantDeleteResponse
    from .audio_transcribe_response import AudioTranscribeResponse as AudioTranscribeResponse
    from .cluster_retrieve_response import ClusterRetrieveResponse as ClusterRetrieveResponse
    from .integration_list_response import IntegrationListResponse as IntegrationListResponse
    from .conversation_list_response import ConversationListResponse as ConversationListResponse
    from .post_conversation_settings import PostConversationSettings as PostConversationSettings
    from .assistant_send_sms_response import AssistantSendSMSResponse as AssistantSendSMSResponse
    from .embedding_retrieve_response import EmbeddingRetrieveResponse as EmbeddingRetrieveResponse
    from .conversation_update_response import ConversationUpdateResponse as ConversationUpdateResponse
    from .transcription_settings_config import TranscriptionSettingsConfig as TranscriptionSettingsConfig
    from .conversation_retrieve_response import ConversationRetrieveResponse as ConversationRetrieveResponse
    from .transcription_endpointing_plan import TranscriptionEndpointingPlan as TranscriptionEndpointingPlan
    from .embedding_similarity_search_response import (
        EmbeddingSimilaritySearchResponse as EmbeddingSimilaritySearchResponse,
    )
    from .inference_embedding_webhook_tool_params import (
        InferenceEmbeddingWebhookToolParams as InferenceEmbeddingWebhookToolParams,
    )
    from .inference_embedding_interruption_settings import (
        InferenceEmbeddingInterruptionSettings as InferenceEmbeddingInterruptionSettings,
    )
    from .conversation_retrieve_conversations_insights_response import (
        ConversationRetrieveConversationsInsightsResponse as ConversationRetrieveConversationsInsightsResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "AssistantIntegration":
        from .assistant_integration import AssistantIntegration

        return AssistantIntegration
    if name == "AssistantMcpServer":
        from .assistant_mcp_server import AssistantMcpServer

        return AssistantMcpServer
    if name == "AssistantsList":
        from .assistants_list import AssistantsList

        return AssistantsList
    if name == "AudioVisualizerConfig":
        from .audio_visualizer_config import AudioVisualizerConfig

        return AudioVisualizerConfig
    if name == "ExternalLlm":
        from .external_llm import ExternalLlm

        return ExternalLlm
    if name == "FallbackConfig":
        from .fallback_config import FallbackConfig

        return FallbackConfig
    if name == "FlowEdge":
        from .flow_edge import FlowEdge

        return FlowEdge
    if name == "HangupTool":
        from .hangup_tool import HangupTool

        return HangupTool
    if name == "HangupToolParams":
        from .hangup_tool_params import HangupToolParams

        return HangupToolParams
    if name == "ImportMetadata":
        from .import_metadata import ImportMetadata

        return ImportMetadata
    if name == "InferenceEmbedding":
        from .inference_embedding import InferenceEmbedding

        return InferenceEmbedding
    if name == "InferenceEmbeddingInterruptionSettings":
        from .inference_embedding_interruption_settings import InferenceEmbeddingInterruptionSettings

        return InferenceEmbeddingInterruptionSettings
    if name == "InferenceEmbeddingWebhookToolParams":
        from .inference_embedding_webhook_tool_params import InferenceEmbeddingWebhookToolParams

        return InferenceEmbeddingWebhookToolParams
    if name == "InsightSettings":
        from .insight_settings import InsightSettings

        return InsightSettings
    if name == "MessagingSettings":
        from .messaging_settings import MessagingSettings

        return MessagingSettings
    if name == "NodePosition":
        from .node_position import NodePosition

        return NodePosition
    if name == "Observability":
        from .observability import Observability

        return Observability
    if name == "PostConversationSettings":
        from .post_conversation_settings import PostConversationSettings

        return PostConversationSettings
    if name == "PrivacySettings":
        from .privacy_settings import PrivacySettings

        return PrivacySettings
    if name == "RetrievalTool":
        from .retrieval_tool import RetrievalTool

        return RetrievalTool
    if name == "StartSpeakingPlan":
        from .start_speaking_plan import StartSpeakingPlan

        return StartSpeakingPlan
    if name == "TelephonySettings":
        from .telephony_settings import TelephonySettings

        return TelephonySettings
    if name == "TranscriptionEndpointingPlan":
        from .transcription_endpointing_plan import TranscriptionEndpointingPlan

        return TranscriptionEndpointingPlan
    if name == "TranscriptionSettings":
        from .transcription_settings import TranscriptionSettings

        return TranscriptionSettings
    if name == "TranscriptionSettingsConfig":
        from .transcription_settings_config import TranscriptionSettingsConfig

        return TranscriptionSettingsConfig
    if name == "VoiceSettings":
        from .voice_settings import VoiceSettings

        return VoiceSettings
    if name == "WidgetSettings":
        from .widget_settings import WidgetSettings

        return WidgetSettings
    if name == "AssistantDeleteResponse":
        from .assistant_delete_response import AssistantDeleteResponse

        return AssistantDeleteResponse
    if name == "AssistantChatResponse":
        from .assistant_chat_response import AssistantChatResponse

        return AssistantChatResponse
    if name == "AssistantSendSMSResponse":
        from .assistant_send_sms_response import AssistantSendSMSResponse

        return AssistantSendSMSResponse
    if name == "AudioTranscribeResponse":
        from .audio_transcribe_response import AudioTranscribeResponse

        return AudioTranscribeResponse
    if name == "BucketIDs":
        from .bucket_ids import BucketIDs

        return BucketIDs
    if name == "RecursiveCluster":
        from .recursive_cluster import RecursiveCluster

        return RecursiveCluster
    if name == "ClusterRetrieveResponse":
        from .cluster_retrieve_response import ClusterRetrieveResponse

        return ClusterRetrieveResponse
    if name == "ClusterListResponse":
        from .cluster_list_response import ClusterListResponse

        return ClusterListResponse
    if name == "ClusterComputeResponse":
        from .cluster_compute_response import ClusterComputeResponse

        return ClusterComputeResponse
    if name == "Conversation":
        from .conversation import Conversation

        return Conversation
    if name == "ConversationRetrieveResponse":
        from .conversation_retrieve_response import ConversationRetrieveResponse

        return ConversationRetrieveResponse
    if name == "ConversationUpdateResponse":
        from .conversation_update_response import ConversationUpdateResponse

        return ConversationUpdateResponse
    if name == "ConversationListResponse":
        from .conversation_list_response import ConversationListResponse

        return ConversationListResponse
    if name == "ConversationRetrieveConversationsInsightsResponse":
        from .conversation_retrieve_conversations_insights_response import (
            ConversationRetrieveConversationsInsightsResponse,
        )

        return ConversationRetrieveConversationsInsightsResponse
    if name == "EmbeddingResponse":
        from .embedding_response import EmbeddingResponse

        return EmbeddingResponse
    if name == "EmbeddingRetrieveResponse":
        from .embedding_retrieve_response import EmbeddingRetrieveResponse

        return EmbeddingRetrieveResponse
    if name == "EmbeddingListResponse":
        from .embedding_list_response import EmbeddingListResponse

        return EmbeddingListResponse
    if name == "EmbeddingSimilaritySearchResponse":
        from .embedding_similarity_search_response import EmbeddingSimilaritySearchResponse

        return EmbeddingSimilaritySearchResponse
    if name == "Integration":
        from .integration import Integration

        return Integration
    if name == "IntegrationListResponse":
        from .integration_list_response import IntegrationListResponse

        return IntegrationListResponse
    if name == "McpServer":
        from .mcp_server import McpServer

        return McpServer
    if name == "EventsListResponse":
        from .events_list_response import EventsListResponse

        return EventsListResponse
    if name == "MissionData":
        from .mission_data import MissionData

        return MissionData
    if name == "MissionResponse":
        from .mission_response import MissionResponse

        return MissionResponse
    if name == "SharedToolResponse":
        from .shared_tool_response import SharedToolResponse

        return SharedToolResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
