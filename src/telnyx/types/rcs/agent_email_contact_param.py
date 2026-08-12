# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentEmailContactParam"]


class AgentEmailContactParam(TypedDict, total=False):
    address: Required[str]

    label: Required[str]
