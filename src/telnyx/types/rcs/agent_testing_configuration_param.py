# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentTestingConfigurationParam"]


class AgentTestingConfigurationParam(TypedDict, total=False):
    test_url: Required[str]
    """A publicly accessible test video or evidence URL."""

    additional_information: Optional[str]

    message_id: Optional[str]
