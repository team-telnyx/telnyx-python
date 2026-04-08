# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["VoiceCloneCreateParams", "TelnyxDesignClone", "MinimaxDesignClone"]


class TelnyxDesignClone(TypedDict, total=False):
    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code for the clone.

    Supports the combined Telnyx language set.
    """

    name: Required[str]
    """Name for the voice clone."""

    voice_design_id: Required[str]
    """UUID of the source voice design to clone."""

    provider: Literal["telnyx", "Telnyx"]
    """Voice synthesis provider. Defaults to `telnyx`."""


class MinimaxDesignClone(TypedDict, total=False):
    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code for the clone. Supports the Minimax language set."""

    name: Required[str]
    """Name for the voice clone."""

    provider: Required[Literal["minimax", "Minimax"]]
    """Voice synthesis provider. Must be `minimax`."""

    voice_design_id: Required[str]
    """UUID of the source voice design to clone."""


VoiceCloneCreateParams: TypeAlias = Union[TelnyxDesignClone, MinimaxDesignClone]
