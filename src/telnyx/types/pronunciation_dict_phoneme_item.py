# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PronunciationDictPhonemeItem"]


class PronunciationDictPhonemeItem(BaseModel):
    """A phoneme pronunciation item.

    When the `text` value is found in input, it is pronounced using the specified IPA phoneme notation.
    """

    alphabet: Literal["ipa"]
    """The phonetic alphabet used for the phoneme notation."""

    phoneme: str
    """The phoneme notation representing the desired pronunciation."""

    text: str
    """The text to match in the input.

    Case-insensitive matching is used during synthesis.
    """

    type: Literal["phoneme"]
    """The item type."""
