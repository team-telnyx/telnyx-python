# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .metadata_field_mapping import MetadataFieldMapping

__all__ = ["ChildRelationshipInfo"]


class ChildRelationshipInfo(BaseModel):
    child_event: str

    child_product: str

    child_record_type: str

    cost_rollup: bool

    description: str

    relationship_type: str

    traversal_enabled: bool

    via: MetadataFieldMapping
