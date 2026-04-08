# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PronunciationDictAliasItemParam"]


class PronunciationDictAliasItemParam(TypedDict, total=False):
    """An alias pronunciation item.

    When the `text` value is found in input, it is replaced with the `alias` before speech synthesis.
    """

    alias: Required[str]
    """The replacement text that will be spoken instead."""

    text: Required[str]
    """The text to match in the input.

    Case-insensitive matching is used during synthesis.
    """

    type: Required[Literal["alias"]]
    """The item type."""
