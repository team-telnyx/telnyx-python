# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .conversation import Conversation

__all__ = ["ConversationRetrieveResponse"]


class ConversationRetrieveResponse(BaseModel):
    data: Optional[Conversation] = None
