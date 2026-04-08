# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PronunciationDictPhonemeItemParam"]


class PronunciationDictPhonemeItemParam(TypedDict, total=False):
    """A phoneme pronunciation item.

    When the `text` value is found in input, it is pronounced using the specified IPA phoneme notation.
    """

    alphabet: Required[Literal["ipa"]]
    """The phonetic alphabet used for the phoneme notation."""

    phoneme: Required[str]
    """The phoneme notation representing the desired pronunciation."""

    text: Required[str]
    """The text to match in the input.

    Case-insensitive matching is used during synthesis.
    """

    type: Required[Literal["phoneme"]]
    """The item type."""
