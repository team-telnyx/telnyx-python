# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "PronunciationDictUpdateParams",
    "Item",
    "ItemPronunciationDictAliasItem",
    "ItemPronunciationDictPhonemeItem",
]


class PronunciationDictUpdateParams(TypedDict, total=False):
    items: Iterable[Item]
    """Updated list of pronunciation items (alias or phoneme type)."""

    name: str
    """Updated dictionary name."""


class ItemPronunciationDictAliasItem(TypedDict, total=False):
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


class ItemPronunciationDictPhonemeItem(TypedDict, total=False):
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


Item: TypeAlias = Union[ItemPronunciationDictAliasItem, ItemPronunciationDictPhonemeItem]
