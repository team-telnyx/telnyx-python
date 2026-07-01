# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .loopcount_param import LoopcountParam as LoopcountParam
from .tool_message_param import ToolMessageParam as ToolMessageParam
from .user_message_param import UserMessageParam as UserMessageParam
from .action_refer_params import ActionReferParams as ActionReferParams
from .action_speak_params import ActionSpeakParams as ActionSpeakParams
from .action_answer_params import ActionAnswerParams as ActionAnswerParams
from .action_bridge_params import ActionBridgeParams as ActionBridgeParams
from .action_gather_params import ActionGatherParams as ActionGatherParams
from .action_hangup_params import ActionHangupParams as ActionHangupParams
from .action_reject_params import ActionRejectParams as ActionRejectParams
from .system_message_param import SystemMessageParam as SystemMessageParam
from .action_enqueue_params import ActionEnqueueParams as ActionEnqueueParams
from .action_transfer_params import ActionTransferParams as ActionTransferParams
from .action_send_dtmf_params import ActionSendDtmfParams as ActionSendDtmfParams
from .assistant_message_param import AssistantMessageParam as AssistantMessageParam
from .developer_message_param import DeveloperMessageParam as DeveloperMessageParam
from .aws_voice_settings_param import AwsVoiceSettingsParam as AwsVoiceSettingsParam
from .action_leave_queue_params import ActionLeaveQueueParams as ActionLeaveQueueParams
from .action_stop_gather_params import ActionStopGatherParams as ActionStopGatherParams
from .action_stop_siprec_params import ActionStopSiprecParams as ActionStopSiprecParams
from .action_start_siprec_params import ActionStartSiprecParams as ActionStartSiprecParams
from .action_stop_forking_params import ActionStopForkingParams as ActionStopForkingParams
from .transcription_config_param import TranscriptionConfigParam as TranscriptionConfigParam
from .action_send_sip_info_params import ActionSendSipInfoParams as ActionSendSipInfoParams
from .action_start_forking_params import ActionStartForkingParams as ActionStartForkingParams
from .action_stop_playback_params import ActionStopPlaybackParams as ActionStopPlaybackParams
from .deepgram_nova2_config_param import DeepgramNova2ConfigParam as DeepgramNova2ConfigParam
from .deepgram_nova3_config_param import DeepgramNova3ConfigParam as DeepgramNova3ConfigParam
from .interruption_settings_param import InterruptionSettingsParam as InterruptionSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam as TelnyxVoiceSettingsParam
from .action_start_playback_params import ActionStartPlaybackParams as ActionStartPlaybackParams
from .action_stop_recording_params import ActionStopRecordingParams as ActionStopRecordingParams
from .action_stop_streaming_params import ActionStopStreamingParams as ActionStopStreamingParams
from .action_gather_using_ai_params import ActionGatherUsingAIParams as ActionGatherUsingAIParams
from .action_pause_recording_params import ActionPauseRecordingParams as ActionPauseRecordingParams
from .action_start_recording_params import ActionStartRecordingParams as ActionStartRecordingParams
from .action_start_streaming_params import ActionStartStreamingParams as ActionStartStreamingParams
from .google_transcription_language import GoogleTranscriptionLanguage as GoogleTranscriptionLanguage
from .telnyx_transcription_language import TelnyxTranscriptionLanguage as TelnyxTranscriptionLanguage
from .action_resume_recording_params import ActionResumeRecordingParams as ActionResumeRecordingParams
from .action_join_ai_assistant_params import ActionJoinAIAssistantParams as ActionJoinAIAssistantParams
from .action_stop_ai_assistant_params import ActionStopAIAssistantParams as ActionStopAIAssistantParams
from .action_gather_using_audio_params import ActionGatherUsingAudioParams as ActionGatherUsingAudioParams
from .action_gather_using_speak_params import ActionGatherUsingSpeakParams as ActionGatherUsingSpeakParams
from .action_start_ai_assistant_params import ActionStartAIAssistantParams as ActionStartAIAssistantParams
from .action_stop_transcription_params import ActionStopTranscriptionParams as ActionStopTranscriptionParams
from .conversation_relay_interruptible import ConversationRelayInterruptible as ConversationRelayInterruptible
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam as ElevenLabsVoiceSettingsParam
from .action_start_transcription_params import ActionStartTranscriptionParams as ActionStartTranscriptionParams
from .action_update_client_state_params import ActionUpdateClientStateParams as ActionUpdateClientStateParams
from .transcription_start_request_param import TranscriptionStartRequestParam as TranscriptionStartRequestParam
from .ai_assistant_join_participant_param import AIAssistantJoinParticipantParam as AIAssistantJoinParticipantParam
from .transcription_engine_a_config_param import TranscriptionEngineAConfigParam as TranscriptionEngineAConfigParam
from .transcription_engine_b_config_param import TranscriptionEngineBConfigParam as TranscriptionEngineBConfigParam
from .action_stop_noise_suppression_params import ActionStopNoiseSuppressionParams as ActionStopNoiseSuppressionParams
from .action_switch_supervisor_role_params import ActionSwitchSupervisorRoleParams as ActionSwitchSupervisorRoleParams
from .action_start_noise_suppression_params import (
    ActionStartNoiseSuppressionParams as ActionStartNoiseSuppressionParams,
)
from .action_stop_conversation_relay_params import (
    ActionStopConversationRelayParams as ActionStopConversationRelayParams,
)
from .transcription_engine_xai_config_param import (
    TranscriptionEngineXaiConfigParam as TranscriptionEngineXaiConfigParam,
)
from .action_start_conversation_relay_params import (
    ActionStartConversationRelayParams as ActionStartConversationRelayParams,
)
from .action_add_ai_assistant_messages_params import (
    ActionAddAIAssistantMessagesParams as ActionAddAIAssistantMessagesParams,
)
from .transcription_engine_azure_config_param import (
    TranscriptionEngineAzureConfigParam as TranscriptionEngineAzureConfigParam,
)
from .transcription_engine_google_config_param import (
    TranscriptionEngineGoogleConfigParam as TranscriptionEngineGoogleConfigParam,
)
from .transcription_engine_soniox_config_param import (
    TranscriptionEngineSonioxConfigParam as TranscriptionEngineSonioxConfigParam,
)
from .transcription_engine_telnyx_config_param import (
    TranscriptionEngineTelnyxConfigParam as TranscriptionEngineTelnyxConfigParam,
)
from .transcription_engine_parakeet_config_param import (
    TranscriptionEngineParakeetConfigParam as TranscriptionEngineParakeetConfigParam,
)
from .transcription_engine_assemblyai_config_param import (
    TranscriptionEngineAssemblyaiConfigParam as TranscriptionEngineAssemblyaiConfigParam,
)
from .transcription_engine_speechmatics_config_param import (
    TranscriptionEngineSpeechmaticsConfigParam as TranscriptionEngineSpeechmaticsConfigParam,
)

if TYPE_CHECKING:
    from .action_refer_response import ActionReferResponse as ActionReferResponse
    from .action_speak_response import ActionSpeakResponse as ActionSpeakResponse
    from .action_answer_response import ActionAnswerResponse as ActionAnswerResponse
    from .action_bridge_response import ActionBridgeResponse as ActionBridgeResponse
    from .action_gather_response import ActionGatherResponse as ActionGatherResponse
    from .action_hangup_response import ActionHangupResponse as ActionHangupResponse
    from .action_reject_response import ActionRejectResponse as ActionRejectResponse
    from .action_enqueue_response import ActionEnqueueResponse as ActionEnqueueResponse
    from .action_transfer_response import ActionTransferResponse as ActionTransferResponse
    from .action_send_dtmf_response import ActionSendDtmfResponse as ActionSendDtmfResponse
    from .action_leave_queue_response import ActionLeaveQueueResponse as ActionLeaveQueueResponse
    from .action_stop_gather_response import ActionStopGatherResponse as ActionStopGatherResponse
    from .action_stop_siprec_response import ActionStopSiprecResponse as ActionStopSiprecResponse
    from .call_control_command_result import CallControlCommandResult as CallControlCommandResult
    from .action_start_siprec_response import ActionStartSiprecResponse as ActionStartSiprecResponse
    from .action_stop_forking_response import ActionStopForkingResponse as ActionStopForkingResponse
    from .action_send_sip_info_response import ActionSendSipInfoResponse as ActionSendSipInfoResponse
    from .action_start_forking_response import ActionStartForkingResponse as ActionStartForkingResponse
    from .action_stop_playback_response import ActionStopPlaybackResponse as ActionStopPlaybackResponse
    from .action_start_playback_response import ActionStartPlaybackResponse as ActionStartPlaybackResponse
    from .action_stop_recording_response import ActionStopRecordingResponse as ActionStopRecordingResponse
    from .action_stop_streaming_response import ActionStopStreamingResponse as ActionStopStreamingResponse
    from .action_gather_using_ai_response import ActionGatherUsingAIResponse as ActionGatherUsingAIResponse
    from .action_pause_recording_response import ActionPauseRecordingResponse as ActionPauseRecordingResponse
    from .action_start_recording_response import ActionStartRecordingResponse as ActionStartRecordingResponse
    from .action_start_streaming_response import ActionStartStreamingResponse as ActionStartStreamingResponse
    from .action_resume_recording_response import ActionResumeRecordingResponse as ActionResumeRecordingResponse
    from .action_join_ai_assistant_response import ActionJoinAIAssistantResponse as ActionJoinAIAssistantResponse
    from .action_stop_ai_assistant_response import ActionStopAIAssistantResponse as ActionStopAIAssistantResponse
    from .action_gather_using_audio_response import ActionGatherUsingAudioResponse as ActionGatherUsingAudioResponse
    from .action_gather_using_speak_response import ActionGatherUsingSpeakResponse as ActionGatherUsingSpeakResponse
    from .action_start_ai_assistant_response import ActionStartAIAssistantResponse as ActionStartAIAssistantResponse
    from .action_stop_transcription_response import ActionStopTranscriptionResponse as ActionStopTranscriptionResponse
    from .action_start_transcription_response import (
        ActionStartTranscriptionResponse as ActionStartTranscriptionResponse,
    )
    from .action_update_client_state_response import ActionUpdateClientStateResponse as ActionUpdateClientStateResponse
    from .action_stop_noise_suppression_response import (
        ActionStopNoiseSuppressionResponse as ActionStopNoiseSuppressionResponse,
    )
    from .action_switch_supervisor_role_response import (
        ActionSwitchSupervisorRoleResponse as ActionSwitchSupervisorRoleResponse,
    )
    from .action_start_noise_suppression_response import (
        ActionStartNoiseSuppressionResponse as ActionStartNoiseSuppressionResponse,
    )
    from .action_stop_conversation_relay_response import (
        ActionStopConversationRelayResponse as ActionStopConversationRelayResponse,
    )
    from .action_start_conversation_relay_response import (
        ActionStartConversationRelayResponse as ActionStartConversationRelayResponse,
    )
    from .action_add_ai_assistant_messages_response import (
        ActionAddAIAssistantMessagesResponse as ActionAddAIAssistantMessagesResponse,
    )
    from .call_control_command_result_with_conversation_id import (
        CallControlCommandResultWithConversationID as CallControlCommandResultWithConversationID,
    )


def __getattr__(name: str) -> Any:
    if name == "CallControlCommandResult":
        from .call_control_command_result import CallControlCommandResult

        return CallControlCommandResult
    if name == "CallControlCommandResultWithConversationID":
        from .call_control_command_result_with_conversation_id import CallControlCommandResultWithConversationID

        return CallControlCommandResultWithConversationID
    if name == "ActionAddAIAssistantMessagesResponse":
        from .action_add_ai_assistant_messages_response import ActionAddAIAssistantMessagesResponse

        return ActionAddAIAssistantMessagesResponse
    if name == "ActionAnswerResponse":
        from .action_answer_response import ActionAnswerResponse

        return ActionAnswerResponse
    if name == "ActionBridgeResponse":
        from .action_bridge_response import ActionBridgeResponse

        return ActionBridgeResponse
    if name == "ActionEnqueueResponse":
        from .action_enqueue_response import ActionEnqueueResponse

        return ActionEnqueueResponse
    if name == "ActionGatherResponse":
        from .action_gather_response import ActionGatherResponse

        return ActionGatherResponse
    if name == "ActionGatherUsingAIResponse":
        from .action_gather_using_ai_response import ActionGatherUsingAIResponse

        return ActionGatherUsingAIResponse
    if name == "ActionGatherUsingAudioResponse":
        from .action_gather_using_audio_response import ActionGatherUsingAudioResponse

        return ActionGatherUsingAudioResponse
    if name == "ActionGatherUsingSpeakResponse":
        from .action_gather_using_speak_response import ActionGatherUsingSpeakResponse

        return ActionGatherUsingSpeakResponse
    if name == "ActionHangupResponse":
        from .action_hangup_response import ActionHangupResponse

        return ActionHangupResponse
    if name == "ActionJoinAIAssistantResponse":
        from .action_join_ai_assistant_response import ActionJoinAIAssistantResponse

        return ActionJoinAIAssistantResponse
    if name == "ActionLeaveQueueResponse":
        from .action_leave_queue_response import ActionLeaveQueueResponse

        return ActionLeaveQueueResponse
    if name == "ActionPauseRecordingResponse":
        from .action_pause_recording_response import ActionPauseRecordingResponse

        return ActionPauseRecordingResponse
    if name == "ActionReferResponse":
        from .action_refer_response import ActionReferResponse

        return ActionReferResponse
    if name == "ActionRejectResponse":
        from .action_reject_response import ActionRejectResponse

        return ActionRejectResponse
    if name == "ActionResumeRecordingResponse":
        from .action_resume_recording_response import ActionResumeRecordingResponse

        return ActionResumeRecordingResponse
    if name == "ActionSendDtmfResponse":
        from .action_send_dtmf_response import ActionSendDtmfResponse

        return ActionSendDtmfResponse
    if name == "ActionSendSipInfoResponse":
        from .action_send_sip_info_response import ActionSendSipInfoResponse

        return ActionSendSipInfoResponse
    if name == "ActionSpeakResponse":
        from .action_speak_response import ActionSpeakResponse

        return ActionSpeakResponse
    if name == "ActionStartAIAssistantResponse":
        from .action_start_ai_assistant_response import ActionStartAIAssistantResponse

        return ActionStartAIAssistantResponse
    if name == "ActionStartConversationRelayResponse":
        from .action_start_conversation_relay_response import ActionStartConversationRelayResponse

        return ActionStartConversationRelayResponse
    if name == "ActionStartForkingResponse":
        from .action_start_forking_response import ActionStartForkingResponse

        return ActionStartForkingResponse
    if name == "ActionStartNoiseSuppressionResponse":
        from .action_start_noise_suppression_response import ActionStartNoiseSuppressionResponse

        return ActionStartNoiseSuppressionResponse
    if name == "ActionStartPlaybackResponse":
        from .action_start_playback_response import ActionStartPlaybackResponse

        return ActionStartPlaybackResponse
    if name == "ActionStartRecordingResponse":
        from .action_start_recording_response import ActionStartRecordingResponse

        return ActionStartRecordingResponse
    if name == "ActionStartSiprecResponse":
        from .action_start_siprec_response import ActionStartSiprecResponse

        return ActionStartSiprecResponse
    if name == "ActionStartStreamingResponse":
        from .action_start_streaming_response import ActionStartStreamingResponse

        return ActionStartStreamingResponse
    if name == "ActionStartTranscriptionResponse":
        from .action_start_transcription_response import ActionStartTranscriptionResponse

        return ActionStartTranscriptionResponse
    if name == "ActionStopAIAssistantResponse":
        from .action_stop_ai_assistant_response import ActionStopAIAssistantResponse

        return ActionStopAIAssistantResponse
    if name == "ActionStopConversationRelayResponse":
        from .action_stop_conversation_relay_response import ActionStopConversationRelayResponse

        return ActionStopConversationRelayResponse
    if name == "ActionStopForkingResponse":
        from .action_stop_forking_response import ActionStopForkingResponse

        return ActionStopForkingResponse
    if name == "ActionStopGatherResponse":
        from .action_stop_gather_response import ActionStopGatherResponse

        return ActionStopGatherResponse
    if name == "ActionStopNoiseSuppressionResponse":
        from .action_stop_noise_suppression_response import ActionStopNoiseSuppressionResponse

        return ActionStopNoiseSuppressionResponse
    if name == "ActionStopPlaybackResponse":
        from .action_stop_playback_response import ActionStopPlaybackResponse

        return ActionStopPlaybackResponse
    if name == "ActionStopRecordingResponse":
        from .action_stop_recording_response import ActionStopRecordingResponse

        return ActionStopRecordingResponse
    if name == "ActionStopSiprecResponse":
        from .action_stop_siprec_response import ActionStopSiprecResponse

        return ActionStopSiprecResponse
    if name == "ActionStopStreamingResponse":
        from .action_stop_streaming_response import ActionStopStreamingResponse

        return ActionStopStreamingResponse
    if name == "ActionStopTranscriptionResponse":
        from .action_stop_transcription_response import ActionStopTranscriptionResponse

        return ActionStopTranscriptionResponse
    if name == "ActionSwitchSupervisorRoleResponse":
        from .action_switch_supervisor_role_response import ActionSwitchSupervisorRoleResponse

        return ActionSwitchSupervisorRoleResponse
    if name == "ActionTransferResponse":
        from .action_transfer_response import ActionTransferResponse

        return ActionTransferResponse
    if name == "ActionUpdateClientStateResponse":
        from .action_update_client_state_response import ActionUpdateClientStateResponse

        return ActionUpdateClientStateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
