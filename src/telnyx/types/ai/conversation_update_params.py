# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["ConversationUpdateParams"]


class ConversationUpdateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """Metadata associated with the conversation."""
