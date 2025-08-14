# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MigrationSourceParams", "ProviderAuth"]


class ProviderAuth(BaseModel):
    access_key: Optional[str] = None
    """AWS Access Key. For Telnyx-to-Telnyx migrations, use your Telnyx API key here."""

    secret_access_key: Optional[str] = None
    """AWS Secret Access Key.

    For Telnyx-to-Telnyx migrations, use your Telnyx API key here as well.
    """


class MigrationSourceParams(BaseModel):
    bucket_name: str
    """Bucket name to migrate the data from."""

    provider: Literal["aws", "telnyx"]
    """Cloud provider from which to migrate data.

    Use 'telnyx' if you want to migrate data from one Telnyx bucket to another.
    """

    provider_auth: ProviderAuth

    id: Optional[str] = None
    """Unique identifier for the data migration source."""

    source_region: Optional[str] = None
    """
    For intra-Telnyx buckets migration, specify the source bucket region in this
    field.
    """
