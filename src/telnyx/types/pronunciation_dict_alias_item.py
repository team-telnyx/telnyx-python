# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PronunciationDictAliasItem"]


class PronunciationDictAliasItem(BaseModel):
    """An alias pronunciation item.

    When the `text` value is found in input, it is replaced with the `alias` before speech synthesis.
    """

    alias: str
    """The replacement text that will be spoken instead."""

    text: str
    """The text to match in the input.

    Case-insensitive matching is used during synthesis.
    """

    type: Literal["alias"]
    """The item type."""
