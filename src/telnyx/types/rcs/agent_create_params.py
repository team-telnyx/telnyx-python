# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .agent_use_case import AgentUseCase
from .agent_configuration_param import AgentConfigurationParam

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    brand_id: Required[str]

    configuration: Required[AgentConfigurationParam]

    display_name: Required[str]

    use_case: Required[AgentUseCase]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    hosting_region: Optional[str]

    profile_id: Optional[str]
    """A Messaging Profile owned by the authenticated organization.

    When omitted, the agent inherits the brand profile.
    """
