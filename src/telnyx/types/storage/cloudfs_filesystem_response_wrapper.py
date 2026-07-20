# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .cloudfs_filesystem_status import CloudfsFilesystemStatus

__all__ = ["CloudfsFilesystemResponseWrapper", "Data"]


class Data(BaseModel):
    """A CloudFS filesystem, including its metadata credential.

    This shape is returned only by create and rotate-meta-token.
    """

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    meta_token: Optional[str] = None
    """Metadata access token, in cleartext.

    Returned only by create and rotate-meta-token and not retrievable afterwards —
    store it securely.
    """

    meta_url: Optional[str] = None
    """PostgreSQL connection URL for the filesystem's metadata database.

    In create and rotate-meta-token responses it embeds the metadata token as the
    password:
    `postgres://<database>:<meta_token>@us-east-1.telnyxcloudfs.com:5432/<database>?sslmode=require`
    (the example below is shown without the credential; the actual response includes
    it). Pass it to `juicefs mount`: the storage configuration is baked in at
    provisioning, so the metadata URL is all a client needs to mount the filesystem.
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


class CloudfsFilesystemResponseWrapper(BaseModel):
    data: Optional[Data] = None
    """A CloudFS filesystem, including its metadata credential.

    This shape is returned only by create and rotate-meta-token.
    """
