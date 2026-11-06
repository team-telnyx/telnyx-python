# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentGatewayNoAuthParam"]


class AgentGatewayNoAuthParam(TypedDict, total=False):
    """The gateway sends no credential."""

    type: Literal["none"]
