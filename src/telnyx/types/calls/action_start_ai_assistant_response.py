# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionStartAIAssistantResponse", "Data"]


class Data(BaseModel):
    conversation_id: Optional[str] = None
    """The ID of the conversation created by the command."""

    result: Optional[str] = None


class ActionStartAIAssistantResponse(BaseModel):
    data: Optional[Data] = None
