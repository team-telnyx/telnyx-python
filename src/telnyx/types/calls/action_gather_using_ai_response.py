# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .call_control_command_result_with_conversation_id import CallControlCommandResultWithConversationID

__all__ = ["ActionGatherUsingAIResponse"]


class ActionGatherUsingAIResponse(BaseModel):
    data: Optional[CallControlCommandResultWithConversationID] = None
