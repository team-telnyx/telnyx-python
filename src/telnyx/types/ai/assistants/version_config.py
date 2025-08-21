# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["VersionConfig"]


class VersionConfig(BaseModel):
    percentage: float
    """Percentage of traffic for this version [1-99]"""

    version_id: str
    """Version ID string that references assistant_versions.version_id"""
