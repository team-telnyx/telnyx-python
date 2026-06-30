# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .event_type import EventType as EventType
from .step_status import StepStatus as StepStatus
from .event_log_params import EventLogParams as EventLogParams
from .event_list_params import EventListParams as EventListParams
from .plan_create_params import PlanCreateParams as PlanCreateParams
from .plan_update_step_params import PlanUpdateStepParams as PlanUpdateStepParams
from .telnyx_agent_link_params import TelnyxAgentLinkParams as TelnyxAgentLinkParams
from .plan_add_steps_to_plan_params import PlanAddStepsToPlanParams as PlanAddStepsToPlanParams
from .create_plan_step_request_param import CreatePlanStepRequestParam as CreatePlanStepRequestParam

if TYPE_CHECKING:
    from .event_data import EventData as EventData
    from .event_response import EventResponse as EventResponse
    from .plan_step_data import PlanStepData as PlanStepData
    from .telnyx_agent_data import TelnyxAgentData as TelnyxAgentData
    from .plan_step_response import PlanStepResponse as PlanStepResponse
    from .plan_retrieve_response import PlanRetrieveResponse as PlanRetrieveResponse
    from .telnyx_agent_link_response import TelnyxAgentLinkResponse as TelnyxAgentLinkResponse
    from .telnyx_agent_list_response import TelnyxAgentListResponse as TelnyxAgentListResponse
    from .plan_steps_created_response import PlanStepsCreatedResponse as PlanStepsCreatedResponse


def __getattr__(name: str) -> Any:
    if name == "EventData":
        from .event_data import EventData

        return EventData
    if name == "EventResponse":
        from .event_response import EventResponse

        return EventResponse
    if name == "PlanStepData":
        from .plan_step_data import PlanStepData

        return PlanStepData
    if name == "PlanStepResponse":
        from .plan_step_response import PlanStepResponse

        return PlanStepResponse
    if name == "PlanStepsCreatedResponse":
        from .plan_steps_created_response import PlanStepsCreatedResponse

        return PlanStepsCreatedResponse
    if name == "PlanRetrieveResponse":
        from .plan_retrieve_response import PlanRetrieveResponse

        return PlanRetrieveResponse
    if name == "TelnyxAgentData":
        from .telnyx_agent_data import TelnyxAgentData

        return TelnyxAgentData
    if name == "TelnyxAgentListResponse":
        from .telnyx_agent_list_response import TelnyxAgentListResponse

        return TelnyxAgentListResponse
    if name == "TelnyxAgentLinkResponse":
        from .telnyx_agent_link_response import TelnyxAgentLinkResponse

        return TelnyxAgentLinkResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
