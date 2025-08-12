# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .telnyx_conversation_channel import TelnyxConversationChannel

__all__ = ["TestCreateParams", "Rubric"]


class TestCreateParams(TypedDict, total=False):
    destination: Required[str]
    """The target destination for the test conversation.

    Format depends on the channel: phone number for SMS/voice, webhook URL for web
    chat, etc.
    """

    instructions: Required[str]
    """
    Detailed instructions that define the test scenario and what the assistant
    should accomplish. This guides the test execution and evaluation.
    """

    name: Required[str]
    """A descriptive name for the assistant test.

    This will be used to identify the test in the UI and reports.
    """

    rubric: Required[Iterable[Rubric]]
    """Evaluation criteria used to assess the assistant's performance.

    Each rubric item contains a name and specific criteria for evaluation.
    """

    description: str
    """Optional detailed description of what this test evaluates and its purpose.

    Helps team members understand the test's objectives.
    """

    max_duration_seconds: int
    """
    Maximum duration in seconds that the test conversation should run before timing
    out. If not specified, uses system default timeout.
    """

    telnyx_conversation_channel: TelnyxConversationChannel
    """The communication channel through which the test will be conducted.

    Determines how the assistant will receive and respond to test messages.
    """

    test_suite: str
    """Optional test suite name to group related tests together.

    Useful for organizing tests by feature, team, or release cycle.
    """


class Rubric(TypedDict, total=False):
    criteria: Required[str]
    """
    Specific guidance on how to assess the assistant’s performance for this rubric
    item.
    """

    name: Required[str]
    """Label for the evaluation criterion, e.g., Empathy, Accuracy, Clarity."""
