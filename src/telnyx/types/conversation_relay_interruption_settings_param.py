# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConversationRelayInterruptionSettingsParam"]


class ConversationRelayInterruptionSettingsParam(TypedDict, total=False):
    """Settings for handling caller interruptions during Conversation Relay speech."""

    enable: bool
    """Legacy boolean form.

    `true` is equivalent to `interruptible=any`; `false` is equivalent to
    `interruptible=none`.
    """

    interruptible: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    interruptible_greeting: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    welcome_greeting_interruptible: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """
