# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AzureConfigurationData"]


class AzureConfigurationData(BaseModel):
    account_key: Optional[str] = None
    """Azure Blob Storage account key."""

    account_name: Optional[str] = None
    """Azure Blob Storage account name."""

    bucket: Optional[str] = None
    """Name of the bucket to be used to store recording files."""
