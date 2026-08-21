# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .agent_email_contact import AgentEmailContact
from .agent_phone_contact import AgentPhoneContact
from .agent_website_contact import AgentWebsiteContact
from .agent_testing_configuration import AgentTestingConfiguration
from .agent_campaign_configuration import AgentCampaignConfiguration

__all__ = [
    "AgentConfiguration",
    "Basics",
    "BasicsAgentPhoneContactRequirement",
    "BasicsAgentWebhookContactRequirement",
    "BasicsAgentProfileContactRequirement",
]


class BasicsAgentPhoneContactRequirement(BaseModel):
    phone_number: AgentPhoneContact

    brand_color: Optional[str] = None

    description: Optional[str] = None

    email: Optional[AgentEmailContact] = None

    hero_url: Optional[str] = None

    logo_url: Optional[str] = None

    privacy_policy_url: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None

    website: Optional[AgentWebsiteContact] = None


class BasicsAgentWebhookContactRequirement(BaseModel):
    website: AgentWebsiteContact

    brand_color: Optional[str] = None

    description: Optional[str] = None

    email: Optional[AgentEmailContact] = None

    hero_url: Optional[str] = None

    logo_url: Optional[str] = None

    phone_number: Optional[AgentPhoneContact] = None

    privacy_policy_url: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None


class BasicsAgentProfileContactRequirement(BaseModel):
    email: AgentEmailContact

    brand_color: Optional[str] = None

    description: Optional[str] = None

    hero_url: Optional[str] = None

    logo_url: Optional[str] = None

    phone_number: Optional[AgentPhoneContact] = None

    privacy_policy_url: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None

    website: Optional[AgentWebsiteContact] = None


Basics: TypeAlias = Union[
    BasicsAgentPhoneContactRequirement, BasicsAgentWebhookContactRequirement, BasicsAgentProfileContactRequirement
]


class AgentConfiguration(BaseModel):
    basics: Basics
    """Basic agent identity and contact information.

    At least one complete phone, website, or email contact is required.
    """

    campaign: Optional[AgentCampaignConfiguration] = None

    testing: Optional[AgentTestingConfiguration] = None
