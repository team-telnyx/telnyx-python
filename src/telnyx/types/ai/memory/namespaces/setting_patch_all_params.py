# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SettingPatchAllParams", "Summary"]


class SettingPatchAllParams(TypedDict, total=False):
    summary: Optional[Summary]
    """A partial update to a namespace's summary settings.

    Only the fields present in the request are changed; the rest are left as they
    are. Sending `instructions: null` (or empty) clears the instructions.
    """


class Summary(TypedDict, total=False):
    """A partial update to a namespace's summary settings.

    Only the fields present in the request are changed; the rest are left as
    they are. Sending `instructions: null` (or empty) clears the instructions.
    """

    instructions: Optional[str]
    """Replace the namespace's summary instructions.

    Null or empty clears them and returns to the neutral default. Omit the field to
    leave the current instructions unchanged.
    """
