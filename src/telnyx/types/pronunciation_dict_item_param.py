# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .pronunciation_dict_alias_item_param import PronunciationDictAliasItemParam
from .pronunciation_dict_phoneme_item_param import PronunciationDictPhonemeItemParam

__all__ = ["PronunciationDictItemParam"]

PronunciationDictItemParam: TypeAlias = Union[PronunciationDictAliasItemParam, PronunciationDictPhonemeItemParam]
