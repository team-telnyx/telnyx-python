# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .agent_interaction_param import AgentInteractionParam
from .agent_consent_configuration_param import AgentConsentConfigurationParam
from .agent_testing_configuration_param import AgentTestingConfigurationParam
from .agent_campaign_configuration_param import AgentCampaignConfigurationParam

__all__ = ["AgentLaunchParams", "Campaign"]


class AgentLaunchParams(TypedDict, total=False):
    campaign: Required[Campaign]

    testing: Required[AgentTestingConfigurationParam]


class Campaign(AgentCampaignConfigurationParam, total=False):
    agent_overview: Required[str]  # type: ignore

    consent_settings: Required[AgentConsentConfigurationParam]  # type: ignore

    interactions: Required[Iterable[AgentInteractionParam]]  # type: ignore

    message_examples: Required[SequenceNotStr[str]]  # type: ignore
