# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .rollout_slot_param import RolloutSlotParam

__all__ = ["ServeParam"]


class ServeParam(TypedDict, total=False):
    """What a rule serves when matched.

    Exactly one of:
    - ``version_id`` — serve a specific version
    - ``rollout`` — weighted random across versions; weights must sum to
      less than 100, with the leftover routing to the main version
    """

    rollout: Iterable[RolloutSlotParam]

    version_id: str
