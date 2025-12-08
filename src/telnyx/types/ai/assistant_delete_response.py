# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AssistantDeleteResponse"]


class AssistantDeleteResponse(BaseModel):
    """
    Aligns with the OpenAI API:
    https://platform.openai.com/docs/api-reference/assistants/deleteAssistant
    """

    id: str

    deleted: bool

    object: str
