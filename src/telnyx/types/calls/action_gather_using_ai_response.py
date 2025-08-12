# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionGatherUsingAIResponse", "Data"]


class Data(BaseModel):
    conversation_id: Optional[str] = None
    """The ID of the conversation created by the command."""

    result: Optional[str] = None


class ActionGatherUsingAIResponse(BaseModel):
    data: Optional[Data] = None
