# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .agent_interaction import AgentInteraction
from .agent_consent_configuration import AgentConsentConfiguration

__all__ = ["AgentCampaignConfiguration"]


class AgentCampaignConfiguration(BaseModel):
    company_overview: str

    additional_information: Optional[str] = None

    agent_overview: Optional[str] = None

    consent_settings: Optional[AgentConsentConfiguration] = None

    interactions: Optional[List[AgentInteraction]] = None

    message_examples: Optional[List[str]] = None
