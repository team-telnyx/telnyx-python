# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .metadata_field_mapping import MetadataFieldMapping

__all__ = ["ParentRelationshipInfo"]


class ParentRelationshipInfo(BaseModel):
    cost_rollup: bool

    description: str

    parent_event: str

    parent_product: str

    parent_record_type: str

    relationship_type: str

    traversal_enabled: bool

    via: MetadataFieldMapping
