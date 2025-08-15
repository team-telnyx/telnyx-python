# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Fax"]


class Fax(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    client_state: Optional[str] = None
    """State received from a command."""

    connection_id: Optional[str] = None
    """The ID of the connection used to send the fax."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when resource was created"""

    direction: Optional[Literal["inbound", "outbound"]] = None
    """The direction of the fax."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The phone number, in E.164 format, the fax will be sent from."""

    from_display_name: Optional[str] = None
    """
    The string used as the caller id name (SIP From Display Name) presented to the
    destination (`to` number).
    """

    media_name: Optional[str] = None
    """The media_name used for the fax's media.

    Must point to a file previously uploaded to api.telnyx.com/v2/media by the same
    user/organization. media_name and media_url/contents can't be submitted
    together.
    """

    media_url: Optional[str] = None
    """The URL (or list of URLs) to the PDF used for the fax's media.

    media_url and media_name/contents can't be submitted together.
    """

    preview_url: Optional[str] = None
    """If `store_preview` was set to `true`, this is a link to temporary location.

    Link expires after 10 minutes.
    """

    quality: Optional[Literal["normal", "high", "very_high", "ultra_light", "ultra_dark"]] = None
    """The quality of the fax.

    The `ultra` settings provides the highest quality available, but also present
    longer fax processing times. `ultra_light` is best suited for images, wihle
    `ultra_dark` is best suited for text.
    """

    record_type: Optional[Literal["fax"]] = None
    """Identifies the type of the resource."""

    status: Optional[
        Literal[
            "queued",
            "media.processed",
            "originated",
            "sending",
            "delivered",
            "failed",
            "initiated",
            "receiving",
            "media.processing",
            "received",
        ]
    ] = None
    """Status of the fax"""

    store_media: Optional[bool] = None
    """Should fax media be stored on temporary URL. It does not support media_name."""

    stored_media_url: Optional[str] = None
    """If store_media was set to true, this is a link to temporary location.

    Link expires after 10 minutes.
    """

    to: Optional[str] = None
    """The phone number, in E.164 format, the fax will be sent to or SIP URI"""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when resource was updated"""

    webhook_failover_url: Optional[str] = None
    """
    Optional failover URL that will receive fax webhooks if webhook_url doesn't
    return a 2XX response
    """

    webhook_url: Optional[str] = None
    """URL that will receive fax webhooks"""
