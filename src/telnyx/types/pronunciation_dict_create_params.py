# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .pronunciation_dict_alias_item_param import PronunciationDictAliasItemParam
from .pronunciation_dict_phoneme_item_param import PronunciationDictPhonemeItemParam

__all__ = ["PronunciationDictCreateParams", "Item"]


class PronunciationDictCreateParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """List of pronunciation items (alias or phoneme type).

    At least one item is required.
    """

    name: Required[str]
    """Human-readable name. Must be unique within the organization."""


Item: TypeAlias = Union[PronunciationDictAliasItemParam, PronunciationDictPhonemeItemParam]
