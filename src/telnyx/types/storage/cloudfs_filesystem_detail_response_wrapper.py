# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .cloudfs_filesystem_detail import CloudfsFilesystemDetail

__all__ = ["CloudfsFilesystemDetailResponseWrapper"]


class CloudfsFilesystemDetailResponseWrapper(BaseModel):
    data: Optional[CloudfsFilesystemDetail] = None
    """A CloudFS filesystem as returned by get, update, and delete.

    `meta_url` omits the credential and there is no `meta_token` field — the token
    is only returned by create and rotate-meta-token.
    """
