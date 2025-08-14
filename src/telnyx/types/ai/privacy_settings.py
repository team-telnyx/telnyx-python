# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PrivacySettings"]


class PrivacySettings(BaseModel):
    data_retention: Optional[bool] = None
    """If true, conversation history and insights will be stored.

    If false, they will not be stored. This in‑tool toggle governs solely the
    retention of conversation history and insights via the AI assistant. It has no
    effect on any separate recording, transcription, or storage configuration that
    you have set at the account, number, or application level. All such external
    settings remain in force regardless of your selection here.
    """
