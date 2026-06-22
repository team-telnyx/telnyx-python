# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .pronunciation_dict_alias_item import PronunciationDictAliasItem
from .pronunciation_dict_phoneme_item import PronunciationDictPhonemeItem

__all__ = ["PronunciationDictItem"]

PronunciationDictItem: TypeAlias = Annotated[
    Union[PronunciationDictAliasItem, PronunciationDictPhonemeItem], PropertyInfo(discriminator="type")
]
