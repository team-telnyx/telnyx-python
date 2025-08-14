# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .assistants.tests.test_suites.meta import Meta

__all__ = ["ConversationRetrieveConversationsInsightsResponse", "Data", "DataConversationInsight"]


class DataConversationInsight(BaseModel):
    insight_id: str
    """Unique identifier for the insight configuration."""

    result: str
    """Insight result from the conversation.

    If the insight has a JSON schema, this will be stringified JSON object.
    """


class Data(BaseModel):
    id: str
    """Unique identifier for the conversation insight."""

    conversation_insights: List[DataConversationInsight]
    """List of insights extracted from the conversation."""

    created_at: datetime
    """Timestamp of when the object was created."""

    status: Literal["pending", "in_progress", "completed", "failed"]
    """Current status of the insight generation for the conversation."""


class ConversationRetrieveConversationsInsightsResponse(BaseModel):
    data: List[Data]

    meta: Meta
