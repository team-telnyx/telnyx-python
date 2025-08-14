# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MigrationParams"]


class MigrationParams(BaseModel):
    source_id: str
    """ID of the Migration Source from which to migrate data."""

    target_bucket_name: str
    """Bucket name to migrate the data into.

    Will default to the same name as the `source_bucket_name`.
    """

    target_region: str
    """Telnyx Cloud Storage region to migrate the data to."""

    id: Optional[str] = None
    """Unique identifier for the data migration."""

    bytes_migrated: Optional[int] = None
    """Total amount of data that has been succesfully migrated."""

    bytes_to_migrate: Optional[int] = None
    """Total amount of data found in source bucket to migrate."""

    created_at: Optional[datetime] = None
    """Time when data migration was created"""

    eta: Optional[datetime] = None
    """Estimated time the migration will complete."""

    last_copy: Optional[datetime] = None
    """Time when data migration was last copied from the source."""

    refresh: Optional[bool] = None
    """
    If true, will continue to poll the source bucket to ensure new data is
    continually migrated over.
    """

    speed: Optional[int] = None
    """Current speed of the migration."""

    status: Optional[Literal["pending", "checking", "migrating", "complete", "error", "stopped"]] = None
    """Status of the migration."""
