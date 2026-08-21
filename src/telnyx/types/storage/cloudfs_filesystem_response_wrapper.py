# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .cloudfs_filesystem import CloudfsFilesystem

__all__ = ["CloudfsFilesystemResponseWrapper"]


class CloudfsFilesystemResponseWrapper(BaseModel):
    data: Optional[CloudfsFilesystem] = None
    """A CloudFS filesystem, including its metadata credential.

    This shape is returned only by create and rotate-meta-token.
    """
