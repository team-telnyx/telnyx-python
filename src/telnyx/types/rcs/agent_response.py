# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .agent_use_case import AgentUseCase
from .agent_configuration import AgentConfiguration
from .capabilities_response import CapabilitiesResponse
from .agent_submission_status import AgentSubmissionStatus
from .carrier_approval_response import CarrierApprovalResponse
from .agents.test_device_response import TestDeviceResponse

__all__ = ["AgentResponse"]


class AgentResponse(BaseModel):
    agent_id: str

    basics_status: Optional[AgentSubmissionStatus] = None

    billing_category: Optional[Literal["NON_CONVERSATIONAL", "CONVERSATIONAL"]] = None

    brand_id: str

    campaign_status: Optional[AgentSubmissionStatus] = None

    capabilities: CapabilitiesResponse

    carrier_approvals: List[CarrierApprovalResponse]

    configuration: AgentConfiguration

    display_name: str

    hosting_region: Optional[str] = None

    profile_id: Optional[str] = None

    status: Literal[
        "CREATED", "SUBMITTED", "VERIFYING", "VERIFIED", "LAUNCHING", "LAUNCHED", "LIVE", "REJECTED", "FAILED"
    ]

    test_devices: List[TestDeviceResponse]

    testing_status: Optional[AgentSubmissionStatus] = None

    use_case: AgentUseCase
