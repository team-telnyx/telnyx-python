# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .serve_param import ServeParam as ServeParam
from .clause_param import ClauseParam as ClauseParam
from .event_status import EventStatus as EventStatus
from .tag_add_params import TagAddParams as TagAddParams
from .rule_input_param import RuleInputParam as RuleInputParam
from .test_list_params import TestListParams as TestListParams
from .tool_test_params import ToolTestParams as ToolTestParams
from .rollout_slot_param import RolloutSlotParam as RolloutSlotParam
from .test_create_params import TestCreateParams as TestCreateParams
from .test_update_params import TestUpdateParams as TestUpdateParams
from .version_update_params import VersionUpdateParams as VersionUpdateParams
from .version_retrieve_params import VersionRetrieveParams as VersionRetrieveParams
from .scheduled_event_response import ScheduledEventResponse as ScheduledEventResponse
from .conversation_channel_type import ConversationChannelType as ConversationChannelType
from .instruction_enhance_params import InstructionEnhanceParams as InstructionEnhanceParams
from .canary_deploy_create_params import CanaryDeployCreateParams as CanaryDeployCreateParams
from .canary_deploy_update_params import CanaryDeployUpdateParams as CanaryDeployUpdateParams
from .scheduled_event_list_params import ScheduledEventListParams as ScheduledEventListParams
from .telnyx_conversation_channel import TelnyxConversationChannel as TelnyxConversationChannel
from .instruction_enhance_response import InstructionEnhanceResponse as InstructionEnhanceResponse
from .scheduled_call_settings_param import ScheduledCallSettingsParam as ScheduledCallSettingsParam
from .scheduled_event_create_params import ScheduledEventCreateParams as ScheduledEventCreateParams
from .scheduled_event_list_response import ScheduledEventListResponse as ScheduledEventListResponse

if TYPE_CHECKING:
    from .serve import Serve as Serve
    from .clause import Clause as Clause
    from .rule_output import RuleOutput as RuleOutput
    from .rollout_slot import RolloutSlot as RolloutSlot
    from .tags_response import TagsResponse as TagsResponse
    from .assistant_test import AssistantTest as AssistantTest
    from .tool_test_response import ToolTestResponse as ToolTestResponse
    from .canary_deploy_response import CanaryDeployResponse as CanaryDeployResponse
    from .scheduled_call_settings import ScheduledCallSettings as ScheduledCallSettings
    from .scheduled_sms_event_response import ScheduledSMSEventResponse as ScheduledSMSEventResponse
    from .scheduled_phone_call_event_response import ScheduledPhoneCallEventResponse as ScheduledPhoneCallEventResponse


def __getattr__(name: str) -> Any:
    if name == "AssistantTest":
        from .assistant_test import AssistantTest

        return AssistantTest
    if name == "CanaryDeployResponse":
        from .canary_deploy_response import CanaryDeployResponse

        return CanaryDeployResponse
    if name == "Clause":
        from .clause import Clause

        return Clause
    if name == "RolloutSlot":
        from .rollout_slot import RolloutSlot

        return RolloutSlot
    if name == "RuleOutput":
        from .rule_output import RuleOutput

        return RuleOutput
    if name == "Serve":
        from .serve import Serve

        return Serve
    if name == "ScheduledCallSettings":
        from .scheduled_call_settings import ScheduledCallSettings

        return ScheduledCallSettings
    if name == "ScheduledPhoneCallEventResponse":
        from .scheduled_phone_call_event_response import ScheduledPhoneCallEventResponse

        return ScheduledPhoneCallEventResponse
    if name == "ScheduledSMSEventResponse":
        from .scheduled_sms_event_response import ScheduledSMSEventResponse

        return ScheduledSMSEventResponse
    if name == "ToolTestResponse":
        from .tool_test_response import ToolTestResponse

        return ToolTestResponse
    if name == "TagsResponse":
        from .tags_response import TagsResponse

        return TagsResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
