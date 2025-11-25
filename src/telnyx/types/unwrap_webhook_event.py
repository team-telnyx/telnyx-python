# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .fax_failed_webhook_event import FaxFailedWebhookEvent
from .fax_queued_webhook_event import FaxQueuedWebhookEvent
from .call_hangup_webhook_event import CallHangupWebhookEvent
from .call_bridged_webhook_event import CallBridgedWebhookEvent
from .call_answered_webhook_event import CallAnsweredWebhookEvent
from .call_enqueued_webhook_event import CallEnqueuedWebhookEvent
from .fax_delivered_webhook_event import FaxDeliveredWebhookEvent
from .transcription_webhook_event import TranscriptionWebhookEvent
from .call_initiated_webhook_event import CallInitiatedWebhookEvent
from .call_left_queue_webhook_event import CallLeftQueueWebhookEvent
from .delivery_update_webhook_event import DeliveryUpdateWebhookEvent
from .inbound_message_webhook_event import InboundMessageWebhookEvent
from .call_speak_ended_webhook_event import CallSpeakEndedWebhookEvent
from .conference_ended_webhook_event import ConferenceEndedWebhookEvent
from .streaming_failed_webhook_event import StreamingFailedWebhookEvent
from .call_fork_started_webhook_event import CallForkStartedWebhookEvent
from .call_fork_stopped_webhook_event import CallForkStoppedWebhookEvent
from .call_gather_ended_webhook_event import CallGatherEndedWebhookEvent
from .call_refer_failed_webhook_event import CallReferFailedWebhookEvent
from .streaming_started_webhook_event import StreamingStartedWebhookEvent
from .streaming_stopped_webhook_event import StreamingStoppedWebhookEvent
from .call_dtmf_received_webhook_event import CallDtmfReceivedWebhookEvent
from .call_refer_started_webhook_event import CallReferStartedWebhookEvent
from .call_siprec_failed_webhook_event import CallSiprecFailedWebhookEvent
from .call_speak_started_webhook_event import CallSpeakStartedWebhookEvent
from .conference_created_webhook_event import ConferenceCreatedWebhookEvent
from .call_playback_ended_webhook_event import CallPlaybackEndedWebhookEvent
from .call_siprec_started_webhook_event import CallSiprecStartedWebhookEvent
from .call_siprec_stopped_webhook_event import CallSiprecStoppedWebhookEvent
from .fax_media_processed_webhook_event import FaxMediaProcessedWebhookEvent
from .fax_sending_started_webhook_event import FaxSendingStartedWebhookEvent
from .replaced_link_click_webhook_event import ReplacedLinkClickWebhookEvent
from .call_ai_gather_ended_webhook_event import CallAIGatherEndedWebhookEvent
from .call_recording_error_webhook_event import CallRecordingErrorWebhookEvent
from .call_recording_saved_webhook_event import CallRecordingSavedWebhookEvent
from .call_refer_completed_webhook_event import CallReferCompletedWebhookEvent
from .call_playback_started_webhook_event import CallPlaybackStartedWebhookEvent
from .call_streaming_failed_webhook_event import CallStreamingFailedWebhookEvent
from .call_streaming_started_webhook_event import CallStreamingStartedWebhookEvent
from .call_streaming_stopped_webhook_event import CallStreamingStoppedWebhookEvent
from .conference_speak_ended_webhook_event import ConferenceSpeakEndedWebhookEvent
from .call_conversation_ended_webhook_event import CallConversationEndedWebhookEvent
from .conference_floor_changed_webhook_event import ConferenceFloorChangedWebhookEvent
from .conference_speak_started_webhook_event import ConferenceSpeakStartedWebhookEvent
from .conference_playback_ended_webhook_event import ConferencePlaybackEndedWebhookEvent
from .conference_recording_saved_webhook_event import ConferenceRecordingSavedWebhookEvent
from .number_order_status_update_webhook_event import NumberOrderStatusUpdateWebhookEvent
from .call_machine_greeting_ended_webhook_event import CallMachineGreetingEndedWebhookEvent
from .conference_participant_left_webhook_event import ConferenceParticipantLeftWebhookEvent
from .conference_playback_started_webhook_event import ConferencePlaybackStartedWebhookEvent
from .call_machine_detection_ended_webhook_event import CallMachineDetectionEndedWebhookEvent
from .conference_participant_joined_webhook_event import ConferenceParticipantJoinedWebhookEvent
from .call_ai_gather_partial_results_webhook_event import CallAIGatherPartialResultsWebhookEvent
from .call_recording_transcription_saved_webhook_event import CallRecordingTranscriptionSavedWebhookEvent
from .conference_participant_speak_ended_webhook_event import ConferenceParticipantSpeakEndedWebhookEvent
from .call_machine_premium_greeting_ended_webhook_event import CallMachinePremiumGreetingEndedWebhookEvent
from .call_conversation_insights_generated_webhook_event import CallConversationInsightsGeneratedWebhookEvent
from .call_machine_premium_detection_ended_webhook_event import CallMachinePremiumDetectionEndedWebhookEvent
from .conference_participant_speak_started_webhook_event import ConferenceParticipantSpeakStartedWebhookEvent
from .conference_participant_playback_ended_webhook_event import ConferenceParticipantPlaybackEndedWebhookEvent
from .call_ai_gather_message_history_updated_webhook_event import CallAIGatherMessageHistoryUpdatedWebhookEvent
from .customer_service_record_status_changed_webhook_event import CustomerServiceRecordStatusChangedWebhookEvent
from .conference_participant_playback_started_webhook_event import ConferenceParticipantPlaybackStartedWebhookEvent

__all__ = ["UnwrapWebhookEvent", "CampaignStatusUpdateEvent", "CampaignSuspendedEvent"]


class CampaignStatusUpdateEvent(BaseModel):
    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)
    """Brand ID associated with the campaign."""

    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)
    """The ID of the campaign."""

    create_date: Optional[str] = FieldInfo(alias="createDate", default=None)
    """Unix timestamp when campaign was created."""

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)
    """Alphanumeric identifier of the CSP associated with this campaign."""

    is_t_mobile_registered: Optional[bool] = FieldInfo(alias="isTMobileRegistered", default=None)
    """Indicates whether the campaign is registered with T-Mobile."""


class CampaignSuspendedEvent(BaseModel):
    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)
    """The ID of the campaign."""

    description: Optional[str] = None
    """Description of the event."""

    status: Optional[Literal["DORMANT"]] = None
    """The status of the campaign."""

    type: Optional[Literal["TELNYX_EVENT"]] = None


UnwrapWebhookEvent: TypeAlias = Union[
    CallAIGatherEndedWebhookEvent,
    CallAIGatherMessageHistoryUpdatedWebhookEvent,
    CallAIGatherPartialResultsWebhookEvent,
    CustomerServiceRecordStatusChangedWebhookEvent,
    CallAnsweredWebhookEvent,
    CallBridgedWebhookEvent,
    CallConversationEndedWebhookEvent,
    CallConversationInsightsGeneratedWebhookEvent,
    CallDtmfReceivedWebhookEvent,
    CallEnqueuedWebhookEvent,
    CallForkStartedWebhookEvent,
    CallForkStoppedWebhookEvent,
    CallGatherEndedWebhookEvent,
    CallHangupWebhookEvent,
    CallInitiatedWebhookEvent,
    CallLeftQueueWebhookEvent,
    CallMachineDetectionEndedWebhookEvent,
    CallMachineGreetingEndedWebhookEvent,
    CallMachinePremiumDetectionEndedWebhookEvent,
    CallMachinePremiumGreetingEndedWebhookEvent,
    CallPlaybackEndedWebhookEvent,
    CallPlaybackStartedWebhookEvent,
    CallRecordingErrorWebhookEvent,
    CallRecordingSavedWebhookEvent,
    CallRecordingTranscriptionSavedWebhookEvent,
    CallReferCompletedWebhookEvent,
    CallReferFailedWebhookEvent,
    CallReferStartedWebhookEvent,
    CallSiprecFailedWebhookEvent,
    CallSiprecStartedWebhookEvent,
    CallSiprecStoppedWebhookEvent,
    CallSpeakEndedWebhookEvent,
    CallSpeakStartedWebhookEvent,
    CallStreamingFailedWebhookEvent,
    CallStreamingStartedWebhookEvent,
    CallStreamingStoppedWebhookEvent,
    CampaignStatusUpdateEvent,
    CampaignSuspendedEvent,
    ConferenceCreatedWebhookEvent,
    ConferenceEndedWebhookEvent,
    ConferenceFloorChangedWebhookEvent,
    ConferenceParticipantJoinedWebhookEvent,
    ConferenceParticipantLeftWebhookEvent,
    ConferenceParticipantPlaybackEndedWebhookEvent,
    ConferenceParticipantPlaybackStartedWebhookEvent,
    ConferenceParticipantSpeakEndedWebhookEvent,
    ConferenceParticipantSpeakStartedWebhookEvent,
    ConferencePlaybackEndedWebhookEvent,
    ConferencePlaybackStartedWebhookEvent,
    ConferenceRecordingSavedWebhookEvent,
    ConferenceSpeakEndedWebhookEvent,
    ConferenceSpeakStartedWebhookEvent,
    DeliveryUpdateWebhookEvent,
    FaxDeliveredWebhookEvent,
    FaxFailedWebhookEvent,
    FaxMediaProcessedWebhookEvent,
    FaxQueuedWebhookEvent,
    FaxSendingStartedWebhookEvent,
    InboundMessageWebhookEvent,
    NumberOrderStatusUpdateWebhookEvent,
    ReplacedLinkClickWebhookEvent,
    StreamingFailedWebhookEvent,
    StreamingStartedWebhookEvent,
    StreamingStoppedWebhookEvent,
    TranscriptionWebhookEvent,
]
