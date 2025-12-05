# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AzureConfigurationDataParam"]


class AzureConfigurationDataParam(TypedDict, total=False):
    backend: Required[Literal["azure"]]
    """Storage backend type"""

    account_key: str
    """Azure Blob Storage account key."""

    account_name: str
    """Azure Blob Storage account name."""

    bucket: str
    """Name of the bucket to be used to store recording files."""
