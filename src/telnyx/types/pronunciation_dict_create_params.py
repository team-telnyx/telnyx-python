# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .pronunciation_dict_item_param import PronunciationDictItemParam

__all__ = ["PronunciationDictCreateParams"]


class PronunciationDictCreateParams(TypedDict, total=False):
    items: Required[Iterable[PronunciationDictItemParam]]
    """List of pronunciation items (alias or phoneme type).

    At least one item is required.
    """

    name: Required[str]
    """Human-readable name. Must be unique within the organization."""
