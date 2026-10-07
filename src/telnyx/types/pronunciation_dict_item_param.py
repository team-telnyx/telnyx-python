# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, ForwardRef
from typing_extensions import TypeAlias

__all__ = ["PronunciationDictItemParam"]

if TYPE_CHECKING:
    PronunciationDictItemParam: TypeAlias = Union[
        "PronunciationDictAliasItemParam", "PronunciationDictPhonemeItemParam"
    ]
else:
    PronunciationDictItemParam = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).PronunciationDictAliasItemParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).PronunciationDictPhonemeItemParam"),
    ]

from .pronunciation_dict_alias_item_param import PronunciationDictAliasItemParam
from .pronunciation_dict_phoneme_item_param import PronunciationDictPhonemeItemParam
