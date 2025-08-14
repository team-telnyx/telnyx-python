# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .conversation import Conversation

__all__ = ["ConversationListResponse"]


class ConversationListResponse(BaseModel):
    data: List[Conversation]
