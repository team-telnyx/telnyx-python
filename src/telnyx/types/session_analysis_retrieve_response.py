# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "SessionAnalysisRetrieveResponse",
    "Cost",
    "Meta",
    "Root",
    "RootCost",
    "RootLinks",
    "RootRelationship",
    "RootRelationshipVia",
]


class Cost(BaseModel):
    currency: str
    """ISO 4217 currency code."""

    total: str
    """Total session cost as a decimal string."""


class Meta(BaseModel):
    event_count: int
    """Total number of events in the session tree."""

    products: List[str]
    """List of distinct products involved in the session."""


class RootCost(BaseModel):
    cumulative_cost: str
    """Cumulative cost including all descendants."""

    currency: str
    """ISO 4217 currency code."""

    event_cost: str
    """Cost of this individual event."""


class RootLinks(BaseModel):
    records: str
    """Link to the underlying detail records."""

    self: str
    """Link to this session analysis node."""


class RootRelationshipVia(BaseModel):
    local_field: str
    """Field name on the child record."""

    parent_field: str
    """Field name on the parent record."""


class RootRelationship(BaseModel):
    """Relationship to the parent node, null for root."""

    parent_id: str
    """Identifier of the parent event."""

    type: str
    """Relationship type identifier."""

    via: RootRelationshipVia


class Root(BaseModel):
    id: str
    """Event identifier."""

    children: List[object]
    """Child events in the session tree."""

    cost: RootCost

    event_name: str
    """Name of the event type."""

    links: RootLinks

    product: str
    """Product that generated this event."""

    record: Dict[str, object]
    """The underlying detail record data. Contents vary by record type."""

    relationship: Optional[RootRelationship] = None
    """Relationship to the parent node, null for root."""


class SessionAnalysisRetrieveResponse(BaseModel):
    cost: Cost

    created_at: datetime
    """When the session started."""

    meta: Meta

    root: Root

    session_id: str
    """Identifier for the analyzed session."""

    status: str
    """Analysis status (e.g. "completed")."""

    completed_at: Optional[datetime] = None
    """When the session completed."""
