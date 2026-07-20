# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .cloudfs_filesystem_status import CloudfsFilesystemStatus

__all__ = ["CloudfListResponse", "Data", "Meta", "MetaCursors"]


class Data(BaseModel):
    """A CloudFS filesystem as returned in list results.

    Connection details (`meta_url`, `meta_token`) are omitted — retrieve the filesystem by ID for its redacted `meta_url`.
    """

    id: Optional[str] = None

    created_at: Optional[datetime] = None

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


class MetaCursors(BaseModel):
    """Opaque cursors for the adjacent pages. Empty when there are no adjacent pages."""

    after: Optional[str] = None
    """Cursor for the next page; pass it as `page[after]`. Omitted on the last page."""

    before: Optional[str] = None
    """Cursor for the previous page; pass it as `page[before]`.

    Omitted on the first page.
    """


class Meta(BaseModel):
    cursors: Optional[MetaCursors] = None
    """Opaque cursors for the adjacent pages. Empty when there are no adjacent pages."""

    next: Optional[str] = None
    """Relative URL (path and query) of the next page.

    Omitted when there are no further results.
    """

    previous: Optional[str] = None
    """Relative URL (path and query) of the previous page. Omitted on the first page."""


class CloudfListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
