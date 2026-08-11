# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .agent_interaction_param import AgentInteractionParam
from .agent_consent_configuration_param import AgentConsentConfigurationParam

__all__ = ["AgentCampaignConfigurationParam"]


class AgentCampaignConfigurationParam(TypedDict, total=False):
    company_overview: Required[str]

    additional_information: Optional[str]

    agent_overview: Optional[str]

    consent_settings: Optional[AgentConsentConfigurationParam]

    interactions: Iterable[AgentInteractionParam]

    message_examples: SequenceNotStr[str]
