# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RolloutSlotParam"]


class RolloutSlotParam(TypedDict, total=False):
    """One slot in a percentage rollout."""

    version_id: Required[str]

    weight: Required[float]
