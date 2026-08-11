# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .agent_email_contact_param import AgentEmailContactParam
from .agent_phone_contact_param import AgentPhoneContactParam
from .agent_website_contact_param import AgentWebsiteContactParam
from .agent_testing_configuration_param import AgentTestingConfigurationParam
from .agent_campaign_configuration_param import AgentCampaignConfigurationParam

__all__ = ["AgentConfigurationParam", "Basics", "BasicsUnionMember0", "BasicsUnionMember1", "BasicsUnionMember2"]


class BasicsUnionMember0(TypedDict, total=False):
    phone_number: Required[AgentPhoneContactParam]

    brand_color: str

    description: str

    email: Optional[AgentEmailContactParam]

    hero_url: str

    logo_url: str

    privacy_policy_url: str

    terms_and_conditions_url: str

    website: Optional[AgentWebsiteContactParam]


class BasicsUnionMember1(TypedDict, total=False):
    website: Required[AgentWebsiteContactParam]

    brand_color: str

    description: str

    email: Optional[AgentEmailContactParam]

    hero_url: str

    logo_url: str

    phone_number: Optional[AgentPhoneContactParam]

    privacy_policy_url: str

    terms_and_conditions_url: str


class BasicsUnionMember2(TypedDict, total=False):
    email: Required[AgentEmailContactParam]

    brand_color: str

    description: str

    hero_url: str

    logo_url: str

    phone_number: Optional[AgentPhoneContactParam]

    privacy_policy_url: str

    terms_and_conditions_url: str

    website: Optional[AgentWebsiteContactParam]


Basics: TypeAlias = Union[BasicsUnionMember0, BasicsUnionMember1, BasicsUnionMember2]


class AgentConfigurationParam(TypedDict, total=False):
    basics: Required[Basics]
    """Basic agent identity and contact information.

    At least one complete phone, website, or email contact is required.
    """

    campaign: Optional[AgentCampaignConfigurationParam]

    testing: Optional[AgentTestingConfigurationParam]
