# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PronunciationDictUpdateResponse",
    "Data",
    "DataItem",
    "DataItemPronunciationDictAliasItem",
    "DataItemPronunciationDictPhonemeItem",
]


class DataItemPronunciationDictAliasItem(BaseModel):
    """An alias pronunciation item.

    When the `text` value is found in input, it is replaced with the `alias` before speech synthesis.
    """

    alias: str
    """The replacement text that will be spoken instead."""

    text: str
    """The text to match in the input.

    Case-insensitive matching is used during synthesis.
    """

    type: Literal["alias"]
    """The item type."""


class DataItemPronunciationDictPhonemeItem(BaseModel):
    """A phoneme pronunciation item.

    When the `text` value is found in input, it is pronounced using the specified IPA phoneme notation.
    """

    alphabet: Literal["ipa"]
    """The phonetic alphabet used for the phoneme notation."""

    phoneme: str
    """The phoneme notation representing the desired pronunciation."""

    text: str
    """The text to match in the input.

    Case-insensitive matching is used during synthesis.
    """

    type: Literal["phoneme"]
    """The item type."""


DataItem: TypeAlias = Annotated[
    Union[DataItemPronunciationDictAliasItem, DataItemPronunciationDictPhonemeItem], PropertyInfo(discriminator="type")
]


class Data(BaseModel):
    """A pronunciation dictionary record."""

    id: Optional[str] = None
    """Unique identifier for the pronunciation dictionary."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp with millisecond precision."""

    items: Optional[List[DataItem]] = None
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


class PronunciationDictUpdateResponse(BaseModel):
    """Response containing a single pronunciation dictionary."""

    data: Optional[Data] = None
    """A pronunciation dictionary record."""
