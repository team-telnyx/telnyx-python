# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .pronunciation_dict_alias_item_param import PronunciationDictAliasItemParam
from .pronunciation_dict_phoneme_item_param import PronunciationDictPhonemeItemParam

__all__ = ["PronunciationDictUpdateParams", "Item"]


class PronunciationDictUpdateParams(TypedDict, total=False):
    items: Iterable[Item]
    """Updated list of pronunciation items (alias or phoneme type)."""

    name: str
    """Updated dictionary name."""


Item: TypeAlias = Union[PronunciationDictAliasItemParam, PronunciationDictPhonemeItemParam]
