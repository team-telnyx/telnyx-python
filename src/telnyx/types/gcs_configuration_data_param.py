# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GcsConfigurationDataParam"]


class GcsConfigurationDataParam(TypedDict, total=False):
    bucket: str
    """Name of the bucket to be used to store recording files."""

    credentials: str
    """
    Opaque credential token used to authenticate and authorize with storage
    provider.
    """
