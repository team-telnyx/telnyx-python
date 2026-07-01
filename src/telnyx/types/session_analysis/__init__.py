# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .metadata_field_mapping import MetadataFieldMapping as MetadataFieldMapping
    from .child_relationship_info import ChildRelationshipInfo as ChildRelationshipInfo
    from .parent_relationship_info import ParentRelationshipInfo as ParentRelationshipInfo
    from .metadata_retrieve_response import MetadataRetrieveResponse as MetadataRetrieveResponse
    from .metadata_retrieve_record_type_response import (
        MetadataRetrieveRecordTypeResponse as MetadataRetrieveRecordTypeResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "ChildRelationshipInfo":
        from .child_relationship_info import ChildRelationshipInfo

        return ChildRelationshipInfo
    if name == "MetadataFieldMapping":
        from .metadata_field_mapping import MetadataFieldMapping

        return MetadataFieldMapping
    if name == "ParentRelationshipInfo":
        from .parent_relationship_info import ParentRelationshipInfo

        return ParentRelationshipInfo
    if name == "MetadataRetrieveResponse":
        from .metadata_retrieve_response import MetadataRetrieveResponse

        return MetadataRetrieveResponse
    if name == "MetadataRetrieveRecordTypeResponse":
        from .metadata_retrieve_record_type_response import MetadataRetrieveRecordTypeResponse

        return MetadataRetrieveRecordTypeResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
