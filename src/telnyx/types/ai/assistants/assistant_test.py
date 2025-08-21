# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .telnyx_conversation_channel import TelnyxConversationChannel

__all__ = ["AssistantTest", "Rubric"]


class Rubric(BaseModel):
    criteria: str
    """
    Specific guidance on how to assess the assistant’s performance for this rubric
    item.
    """

    name: str
    """Label for the evaluation criterion, e.g., Empathy, Accuracy, Clarity."""


class AssistantTest(BaseModel):
    created_at: datetime
    """Timestamp when the test was created."""

    name: str
    """Human-readable name of the test."""

    rubric: List[Rubric]
    """Evaluation criteria used to assess test performance."""

    telnyx_conversation_channel: TelnyxConversationChannel
    """Communication channel used for test execution."""

    test_id: str
    """Unique identifier for the assistant test."""

    description: Optional[str] = None
    """Detailed description of the test's purpose and scope."""

    destination: Optional[str] = None
    """Target destination for test conversations."""

    instructions: Optional[str] = None
    """Detailed test scenario instructions and objectives."""

    max_duration_seconds: Optional[int] = None
    """Maximum allowed duration for test execution in seconds."""

    test_suite: Optional[str] = None
    """Test suite grouping for organizational purposes."""
