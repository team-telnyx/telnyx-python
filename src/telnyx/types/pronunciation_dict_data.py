# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .pronunciation_dict_alias_item import PronunciationDictAliasItem
from .pronunciation_dict_phoneme_item import PronunciationDictPhonemeItem

__all__ = ["PronunciationDictData", "Item"]

Item: TypeAlias = Annotated[
    Union[PronunciationDictAliasItem, PronunciationDictPhonemeItem], PropertyInfo(discriminator="type")
]


class PronunciationDictData(BaseModel):
    """A pronunciation dictionary record."""

    id: Optional[str] = None
    """Unique identifier for the pronunciation dictionary."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp with millisecond precision."""

    items: Optional[List[Item]] = None
    """List of pronunciation items (alias or phoneme type)."""

    name: Optional[str] = None
    """Human-readable name for the dictionary. Must be unique within the organization."""

    record_type: Optional[Literal["pronunciation_dict"]] = None
    """Identifies the resource type."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp with millisecond precision."""

    version: Optional[int] = None
    """Auto-incrementing version number.

    Increases by 1 on each update. Used for optimistic concurrency control and cache
    invalidation.
    """
