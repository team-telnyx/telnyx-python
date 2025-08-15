# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GcsConfigurationData"]


class GcsConfigurationData(BaseModel):
    bucket: Optional[str] = None
    """Name of the bucket to be used to store recording files."""

    credentials: Optional[str] = None
    """
    Opaque credential token used to authenticate and authorize with storage
    provider.
    """
