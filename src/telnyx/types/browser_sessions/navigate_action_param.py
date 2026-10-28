# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NavigateActionParam"]


class NavigateActionParam(TypedDict, total=False):
    """Navigate to a URL."""

    type: Required[Literal["navigate"]]

    url: Required[str]

    idempotency_key: str

    include_observation: bool

    wait_until: Literal["load", "dom_stable", "none"]
