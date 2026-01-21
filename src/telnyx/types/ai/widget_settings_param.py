# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WidgetSettingsParam", "AudioVisualizerConfig"]


class AudioVisualizerConfig(TypedDict, total=False):
    color: Literal["verdant", "twilight", "bloom", "mystic", "flare", "glacier"]
    """The color theme for the audio visualizer."""

    preset: str
    """The preset style for the audio visualizer."""


class WidgetSettingsParam(TypedDict, total=False):
    """Configuration settings for the assistant's web widget."""

    agent_thinking_text: str
    """Text displayed while the agent is processing."""

    audio_visualizer_config: AudioVisualizerConfig

    default_state: Literal["expanded", "collapsed"]
    """The default state of the widget."""

    give_feedback_url: Optional[str]
    """URL for users to give feedback."""

    logo_icon_url: Optional[str]
    """URL to a custom logo icon for the widget."""

    position: Literal["fixed", "static"]
    """The positioning style for the widget."""

    report_issue_url: Optional[str]
    """URL for users to report issues."""

    speak_to_interrupt_text: str
    """Text prompting users to speak to interrupt."""

    start_call_text: str
    """Custom text displayed on the start call button."""

    theme: Literal["light", "dark"]
    """The visual theme for the widget."""

    view_history_url: Optional[str]
    """URL to view conversation history."""
