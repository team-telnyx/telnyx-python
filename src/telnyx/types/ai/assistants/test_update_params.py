# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .telnyx_conversation_channel import TelnyxConversationChannel

__all__ = ["TestUpdateParams", "Rubric"]


class TestUpdateParams(TypedDict, total=False):
    description: str
    """Updated description of the test's purpose and evaluation criteria."""

    destination: str
    """Updated target destination for test conversations."""

    instructions: str
    """Updated test scenario instructions and objectives."""

    max_duration_seconds: int
    """Updated maximum test duration in seconds."""

    name: str
    """Updated name for the assistant test. Must be unique and descriptive."""

    rubric: Iterable[Rubric]
    """Updated evaluation criteria for assessing assistant performance."""

    telnyx_conversation_channel: TelnyxConversationChannel
    """Updated communication channel for the test execution."""

    test_suite: str
    """Updated test suite assignment for better organization."""


class Rubric(TypedDict, total=False):
    criteria: Required[str]
    """
    Specific guidance on how to assess the assistant’s performance for this rubric
    item.
    """

    name: Required[str]
    """Label for the evaluation criterion, e.g., Empathy, Accuracy, Clarity."""
