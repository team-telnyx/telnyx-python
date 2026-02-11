# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TelnyxAgentLinkParams"]


class TelnyxAgentLinkParams(TypedDict, total=False):
    mission_id: Required[str]

    telnyx_agent_id: Required[str]
    """The Telnyx AI agent ID to link"""
