# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .conference_region import ConferenceRegion as ConferenceRegion
from .action_hold_params import ActionHoldParams as ActionHoldParams
from .action_join_params import ActionJoinParams as ActionJoinParams
from .action_mute_params import ActionMuteParams as ActionMuteParams
from .action_play_params import ActionPlayParams as ActionPlayParams
from .action_stop_params import ActionStopParams as ActionStopParams
from .action_leave_params import ActionLeaveParams as ActionLeaveParams
from .action_speak_params import ActionSpeakParams as ActionSpeakParams
from .action_unhold_params import ActionUnholdParams as ActionUnholdParams
from .action_unmute_params import ActionUnmuteParams as ActionUnmuteParams
from .action_update_params import ActionUpdateParams as ActionUpdateParams
from .action_send_dtmf_params import ActionSendDtmfParams as ActionSendDtmfParams
from .action_record_stop_params import ActionRecordStopParams as ActionRecordStopParams
from .action_record_pause_params import ActionRecordPauseParams as ActionRecordPauseParams
from .action_record_start_params import ActionRecordStartParams as ActionRecordStartParams
from .action_record_resume_params import ActionRecordResumeParams as ActionRecordResumeParams
from .action_end_conference_params import ActionEndConferenceParams as ActionEndConferenceParams
from .action_gather_dtmf_audio_params import ActionGatherDtmfAudioParams as ActionGatherDtmfAudioParams

if TYPE_CHECKING:
    from .action_hold_response import ActionHoldResponse as ActionHoldResponse
    from .action_join_response import ActionJoinResponse as ActionJoinResponse
    from .action_mute_response import ActionMuteResponse as ActionMuteResponse
    from .action_play_response import ActionPlayResponse as ActionPlayResponse
    from .action_stop_response import ActionStopResponse as ActionStopResponse
    from .action_leave_response import ActionLeaveResponse as ActionLeaveResponse
    from .action_speak_response import ActionSpeakResponse as ActionSpeakResponse
    from .action_unhold_response import ActionUnholdResponse as ActionUnholdResponse
    from .action_unmute_response import ActionUnmuteResponse as ActionUnmuteResponse
    from .action_update_response import ActionUpdateResponse as ActionUpdateResponse
    from .action_send_dtmf_response import ActionSendDtmfResponse as ActionSendDtmfResponse
    from .conference_command_result import ConferenceCommandResult as ConferenceCommandResult
    from .action_record_stop_response import ActionRecordStopResponse as ActionRecordStopResponse
    from .action_record_pause_response import ActionRecordPauseResponse as ActionRecordPauseResponse
    from .action_record_start_response import ActionRecordStartResponse as ActionRecordStartResponse
    from .action_record_resume_response import ActionRecordResumeResponse as ActionRecordResumeResponse
    from .action_end_conference_response import ActionEndConferenceResponse as ActionEndConferenceResponse
    from .action_gather_dtmf_audio_response import ActionGatherDtmfAudioResponse as ActionGatherDtmfAudioResponse


def __getattr__(name: str) -> Any:
    if name == "ConferenceCommandResult":
        from .conference_command_result import ConferenceCommandResult

        return ConferenceCommandResult
    if name == "ActionUpdateResponse":
        from .action_update_response import ActionUpdateResponse

        return ActionUpdateResponse
    if name == "ActionEndConferenceResponse":
        from .action_end_conference_response import ActionEndConferenceResponse

        return ActionEndConferenceResponse
    if name == "ActionGatherDtmfAudioResponse":
        from .action_gather_dtmf_audio_response import ActionGatherDtmfAudioResponse

        return ActionGatherDtmfAudioResponse
    if name == "ActionHoldResponse":
        from .action_hold_response import ActionHoldResponse

        return ActionHoldResponse
    if name == "ActionJoinResponse":
        from .action_join_response import ActionJoinResponse

        return ActionJoinResponse
    if name == "ActionLeaveResponse":
        from .action_leave_response import ActionLeaveResponse

        return ActionLeaveResponse
    if name == "ActionMuteResponse":
        from .action_mute_response import ActionMuteResponse

        return ActionMuteResponse
    if name == "ActionPlayResponse":
        from .action_play_response import ActionPlayResponse

        return ActionPlayResponse
    if name == "ActionRecordPauseResponse":
        from .action_record_pause_response import ActionRecordPauseResponse

        return ActionRecordPauseResponse
    if name == "ActionRecordResumeResponse":
        from .action_record_resume_response import ActionRecordResumeResponse

        return ActionRecordResumeResponse
    if name == "ActionRecordStartResponse":
        from .action_record_start_response import ActionRecordStartResponse

        return ActionRecordStartResponse
    if name == "ActionRecordStopResponse":
        from .action_record_stop_response import ActionRecordStopResponse

        return ActionRecordStopResponse
    if name == "ActionSendDtmfResponse":
        from .action_send_dtmf_response import ActionSendDtmfResponse

        return ActionSendDtmfResponse
    if name == "ActionSpeakResponse":
        from .action_speak_response import ActionSpeakResponse

        return ActionSpeakResponse
    if name == "ActionStopResponse":
        from .action_stop_response import ActionStopResponse

        return ActionStopResponse
    if name == "ActionUnholdResponse":
        from .action_unhold_response import ActionUnholdResponse

        return ActionUnholdResponse
    if name == "ActionUnmuteResponse":
        from .action_unmute_response import ActionUnmuteResponse

        return ActionUnmuteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
