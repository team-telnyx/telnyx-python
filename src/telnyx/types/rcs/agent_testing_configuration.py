# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["AgentTestingConfiguration"]


class AgentTestingConfiguration(BaseModel):
    test_url: str
    """A publicly accessible test video or evidence URL."""

    additional_information: Optional[str] = None

    message_id: Optional[str] = None
