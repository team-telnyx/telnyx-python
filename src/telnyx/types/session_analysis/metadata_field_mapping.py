# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MetadataFieldMapping"]


class MetadataFieldMapping(BaseModel):
    local_field: str

    parent_field: str
