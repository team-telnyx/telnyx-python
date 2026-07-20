# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .cloudfs_filesystem_status import CloudfsFilesystemStatus

__all__ = ["CloudfsFilesystemDetailResponseWrapper", "Data"]


class Data(BaseModel):
    """A CloudFS filesystem as returned by get, update, and delete.

    `meta_url` omits the credential and there is no `meta_token` field — the token is only returned by create and rotate-meta-token.
    """

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    error: Optional[str] = None
    """Explanation of the most recent failed lifecycle action.

    Present only when the filesystem is in a `failed` state.
    """

    meta_url: Optional[str] = None
    """
    PostgreSQL connection URL for the filesystem's metadata database, without the
    credential. Combine it with your stored metadata token, or issue a new token
    with rotate-meta-token.
    """

    name: Optional[str] = None

    record_type: Optional[str] = None

    region: Optional[str] = None

    s3_bucket: Optional[str] = None
    """Name of the bucket that stores this filesystem's data.

    Created during provisioning.
    """

    s3_endpoint: Optional[str] = None
    """URL of the Telnyx Cloud Storage endpoint backing this filesystem."""

    status: Optional[CloudfsFilesystemStatus] = None
    """Lifecycle status of the filesystem.

    `ready` means it is fully provisioned and usable. `needs_format` means the
    storage bucket and metadata database were provisioned but the filesystem has not
    yet been formatted — run `juicefs format` with the filesystem's `meta_url`
    before mounting. `failed` means the last lifecycle action failed — see the
    filesystem's `error` message. `deleted` appears only in the delete response:
    deleted filesystems are excluded from list results and return a `404` on
    retrieval.
    """

    updated_at: Optional[datetime] = None


class CloudfsFilesystemDetailResponseWrapper(BaseModel):
    data: Optional[Data] = None
    """A CloudFS filesystem as returned by get, update, and delete.

    `meta_url` omits the credential and there is no `meta_token` field — the token
    is only returned by create and rotate-meta-token.
    """
