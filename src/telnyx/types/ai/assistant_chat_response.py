# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AssistantChatResponse"]


class AssistantChatResponse(BaseModel):
    content: str
    """The assistant's generated response based on the input message and context."""
