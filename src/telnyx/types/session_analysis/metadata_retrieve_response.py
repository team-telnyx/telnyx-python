# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "MetadataRetrieveResponse",
    "Meta",
    "QueryParameters",
    "RecordType",
    "RecordTypeChildRelationship",
    "RecordTypeChildRelationshipVia",
    "RecordTypeParentRelationship",
    "RecordTypeParentRelationshipVia",
]


class Meta(BaseModel):
    last_updated: datetime

    total_record_types: int


class QueryParameters(BaseModel):
    default: str

    description: str

    type: str

    enum_values: Optional[List[str]] = None

    max: Optional[int] = None

    min: Optional[int] = None


class RecordTypeChildRelationshipVia(BaseModel):
    local_field: str

    parent_field: str


class RecordTypeChildRelationship(BaseModel):
    child_event: str

    child_product: str

    child_record_type: str

    cost_rollup: bool

    description: str

    relationship_type: str

    traversal_enabled: bool

    via: RecordTypeChildRelationshipVia


class RecordTypeParentRelationshipVia(BaseModel):
    local_field: str

    parent_field: str


class RecordTypeParentRelationship(BaseModel):
    cost_rollup: bool

    description: str

    parent_event: str

    parent_product: str

    parent_record_type: str

    relationship_type: str

    traversal_enabled: bool

    via: RecordTypeParentRelationshipVia


class RecordType(BaseModel):
    aliases: List[str]

    child_relationships: List[RecordTypeChildRelationship]

    description: str

    event: str

    parent_relationships: List[RecordTypeParentRelationship]

    product: str

    record_type: str


class MetadataRetrieveResponse(BaseModel):
    meta: Meta

    query_parameters: Dict[str, QueryParameters]
    """Map of supported query parameter names to their definitions."""

    record_types: List[RecordType]
