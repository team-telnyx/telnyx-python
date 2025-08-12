# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InsightSettings"]


class InsightSettings(BaseModel):
    insight_group_id: Optional[str] = None
    """Reference to an Insight Group.

    Insights in this group will be run automatically for all the assistant's
    conversations.
    """
