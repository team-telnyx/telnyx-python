# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ConversationInsightRetrieveAggregatesResponse", "Data"]


class Data(BaseModel):
    """An aggregation row.

    Contains the grouped field values (keyed by the group_by field names) and a `record_count` integer. For example, when grouping by `score`, each row has a `score` value and a `record_count` of conversations with that score. When also splitting by `metadata.assistant_version_id`, each row includes both `score` and `metadata.assistant_version_id` plus their combined `record_count`.
    """

    record_count: int
    """
    Number of conversation insights that match this combination of grouped field
    values.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ConversationInsightRetrieveAggregatesResponse(BaseModel):
    """Aggregated conversation insight counts grouped by the specified fields.

    Each item in `data` contains the grouped field values and a `record_count` indicating how many conversation insights match that combination.
    """

    data: List[Data]
    """Aggregation result rows.

    Each row contains the grouped field values and a `record_count`.
    """
