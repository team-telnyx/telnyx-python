# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .agent_use_case import AgentUseCase
from .agent_configuration_param import AgentConfigurationParam

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    configuration: AgentConfigurationParam

    display_name: str

    hosting_region: str

    profile_id: str

    use_case: AgentUseCase
