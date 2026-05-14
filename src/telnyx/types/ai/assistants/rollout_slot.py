# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["RolloutSlot"]


class RolloutSlot(BaseModel):
    """One slot in a percentage rollout."""

    version_id: str

    weight: float
