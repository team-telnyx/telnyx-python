# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .pronunciation_dict_item_param import PronunciationDictItemParam

__all__ = ["PronunciationDictUpdateParams"]


class PronunciationDictUpdateParams(TypedDict, total=False):
    items: Iterable[PronunciationDictItemParam]
    """Updated list of pronunciation items (alias or phoneme type)."""

    name: str
    """Updated dictionary name."""
