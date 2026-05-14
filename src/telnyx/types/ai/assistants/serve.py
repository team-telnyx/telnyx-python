# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .rollout_slot import RolloutSlot

__all__ = ["Serve"]


class Serve(BaseModel):
    """What a rule serves when matched.

    Exactly one of:
    - ``version_id`` — serve a specific version
    - ``rollout`` — weighted random across versions; weights must sum to
      less than 100, with the leftover routing to the main version
    """

    rollout: Optional[List[RolloutSlot]] = None

    version_id: Optional[str] = None
