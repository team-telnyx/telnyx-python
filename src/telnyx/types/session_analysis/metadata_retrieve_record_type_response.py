# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel
from .child_relationship_info import ChildRelationshipInfo
from .parent_relationship_info import ParentRelationshipInfo

__all__ = ["MetadataRetrieveRecordTypeResponse", "Meta"]


class Meta(BaseModel):
    max_recommended_depth: int

    total_children: int

    total_parents: int

    total_siblings: int


class MetadataRetrieveRecordTypeResponse(BaseModel):
    aliases: List[str]

    child_relationships: List[ChildRelationshipInfo]

    event: str

    examples: Dict[str, object]
    """Example queries and responses for this record type."""

    meta: Meta

    parent_relationships: List[ParentRelationshipInfo]

    product: str

    record_type: str
