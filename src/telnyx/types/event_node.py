# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["EventNode", "Cost", "Links", "Relationship", "RelationshipVia"]


class Cost(BaseModel):
    cumulative_cost: str
    """Cumulative cost including all descendants."""

    currency: str
    """ISO 4217 currency code."""

    event_cost: str
    """Cost of this individual event."""


class Links(BaseModel):
    records: str
    """Link to the underlying detail records."""

    self: str
    """Link to this session analysis node."""


class RelationshipVia(BaseModel):
    local_field: str
    """Field name on the child record."""

    parent_field: str
    """Field name on the parent record."""


class Relationship(BaseModel):
    """Relationship to the parent node, null for root."""

    parent_id: str
    """Identifier of the parent event."""

    type: str
    """Relationship type identifier."""

    via: RelationshipVia


class EventNode(BaseModel):
    id: str
    """Event identifier."""

    children: List["EventNode"]
    """Child events in the session tree."""

    cost: Cost

    event_name: str
    """Name of the event type."""

    links: Links

    product: str
    """Product that generated this event."""

    record: Dict[str, object]
    """The underlying detail record data. Contents vary by record type."""

    relationship: Optional[Relationship] = None
    """Relationship to the parent node, null for root."""
