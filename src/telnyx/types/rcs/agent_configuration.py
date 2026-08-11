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

__all__ = ["AgentConfiguration", "Basics", "BasicsUnionMember0", "BasicsUnionMember1", "BasicsUnionMember2"]


class BasicsUnionMember0(BaseModel):
    phone_number: AgentPhoneContact

    brand_color: Optional[str] = None

    description: Optional[str] = None

    email: Optional[AgentEmailContact] = None

    hero_url: Optional[str] = None

    logo_url: Optional[str] = None

    privacy_policy_url: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None

    website: Optional[AgentWebsiteContact] = None


class BasicsUnionMember1(BaseModel):
    website: AgentWebsiteContact

    brand_color: Optional[str] = None

    description: Optional[str] = None

    email: Optional[AgentEmailContact] = None

    hero_url: Optional[str] = None

    logo_url: Optional[str] = None

    phone_number: Optional[AgentPhoneContact] = None

    privacy_policy_url: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None


class BasicsUnionMember2(BaseModel):
    email: AgentEmailContact

    brand_color: Optional[str] = None

    description: Optional[str] = None

    hero_url: Optional[str] = None

    logo_url: Optional[str] = None

    phone_number: Optional[AgentPhoneContact] = None

    privacy_policy_url: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None

    website: Optional[AgentWebsiteContact] = None


Basics: TypeAlias = Union[BasicsUnionMember0, BasicsUnionMember1, BasicsUnionMember2]


class AgentConfiguration(BaseModel):
    basics: Basics
    """Basic agent identity and contact information.

    At least one complete phone, website, or email contact is required.
    """

    campaign: Optional[AgentCampaignConfiguration] = None

    testing: Optional[AgentTestingConfiguration] = None
