# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WidgetSettings", "AudioVisualizerConfig"]


class AudioVisualizerConfig(BaseModel):
    color: Optional[Literal["verdant", "twilight", "bloom", "mystic", "flare", "glacier"]] = None
    """The color theme for the audio visualizer."""

    preset: Optional[str] = None
    """The preset style for the audio visualizer."""


class WidgetSettings(BaseModel):
    """Configuration settings for the assistant's web widget."""

    agent_thinking_text: Optional[str] = None
    """Text displayed while the agent is processing."""

    audio_visualizer_config: Optional[AudioVisualizerConfig] = None

    default_state: Optional[Literal["expanded", "collapsed"]] = None
    """The default state of the widget."""

    give_feedback_url: Optional[str] = None
    """URL for users to give feedback."""

    logo_icon_url: Optional[str] = None
    """URL to a custom logo icon for the widget."""

    position: Optional[Literal["fixed", "static"]] = None
    """The positioning style for the widget."""

    report_issue_url: Optional[str] = None
    """URL for users to report issues."""

    speak_to_interrupt_text: Optional[str] = None
    """Text prompting users to speak to interrupt."""

    start_call_text: Optional[str] = None
    """Custom text displayed on the start call button."""

    theme: Optional[Literal["light", "dark"]] = None
    """The visual theme for the widget."""

    view_history_url: Optional[str] = None
    """URL to view conversation history."""
