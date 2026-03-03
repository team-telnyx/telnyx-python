# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = [
    "MetadataRetrieveRecordTypeResponse",
    "ChildRelationship",
    "ChildRelationshipVia",
    "Meta",
    "ParentRelationship",
    "ParentRelationshipVia",
]


class ChildRelationshipVia(BaseModel):
    local_field: str

    parent_field: str


class ChildRelationship(BaseModel):
    child_event: str

    child_product: str

    child_record_type: str

    cost_rollup: bool

    description: str

    relationship_type: str

    traversal_enabled: bool

    via: ChildRelationshipVia


class Meta(BaseModel):
    max_recommended_depth: int

    total_children: int

    total_parents: int

    total_siblings: int


class ParentRelationshipVia(BaseModel):
    local_field: str

    parent_field: str


class ParentRelationship(BaseModel):
    cost_rollup: bool

    description: str

    parent_event: str

    parent_product: str

    parent_record_type: str

    relationship_type: str

    traversal_enabled: bool

    via: ParentRelationshipVia


class MetadataRetrieveRecordTypeResponse(BaseModel):
    aliases: List[str]

    child_relationships: List[ChildRelationship]

    event: str

    examples: Dict[str, object]
    """Example queries and responses for this record type."""

    meta: Meta

    parent_relationships: List[ParentRelationship]

    product: str

    record_type: str
