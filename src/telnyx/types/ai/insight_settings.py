# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["InsightSettings"]


class InsightSettings(BaseModel):
    insight_group_id: Optional[str] = None
    """Reference to an Insight Group.

    Insights in this group will be run automatically for all the assistant's
    conversations.
    """

    model: Optional[str] = None
    """The model that generates the assistant's insights when a conversation ends.

    It runs every insight in the group, Telnyx-managed insights included. Must be
    `zai-org/GLM-5.3-Flash` or `meta-llama/Llama-3.3-70B-Instruct`; any other model
    returns `422`. When omitted on create, it defaults to `zai-org/GLM-5.3-Flash`;
    when omitted on update, the current model is kept. `null` uses Telnyx's default
    insight models, which assistants created before this setting have. Insights of
    messaging conversations, and insights regenerated later, always use Telnyx's
    default insight models.
    """
