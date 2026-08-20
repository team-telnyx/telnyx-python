# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """Metadata associated with the conversation.

    Set `ai_disabled` to `true` to create the conversation with AI message responses
    disabled.
    """

    name: str

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
