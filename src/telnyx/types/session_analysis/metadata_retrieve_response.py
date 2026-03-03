# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .child_relationship_info import ChildRelationshipInfo
from .parent_relationship_info import ParentRelationshipInfo

__all__ = ["MetadataRetrieveResponse", "Meta", "QueryParameters", "RecordType"]


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


class RecordType(BaseModel):
    aliases: List[str]

    child_relationships: List[ChildRelationshipInfo]

    description: str

    event: str

    parent_relationships: List[ParentRelationshipInfo]

    product: str

    record_type: str


class MetadataRetrieveResponse(BaseModel):
    meta: Meta

    query_parameters: Dict[str, QueryParameters]
    """Map of supported query parameter names to their definitions."""

    record_types: List[RecordType]
