# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FaxFailedWebhookEvent", "Payload"]


class Payload(BaseModel):
    client_state: Optional[str] = None
    """State received from a command."""

    connection_id: Optional[str] = None
    """The ID of the connection used to send the fax."""

    direction: Optional[Literal["inbound", "outbound"]] = None
    """The direction of the fax."""

    failure_reason: Optional[Literal["rejected"]] = None
    """Cause of the sending failure"""

    fax_id: Optional[str] = None
    """Identifies the fax."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The phone number, in E.164 format, the fax will be sent from."""

    media_name: Optional[str] = None
    """The media_name used for the fax's media.

    Must point to a file previously uploaded to api.telnyx.com/v2/media by the same
    user/organization. media_name and media_url/contents can't be submitted
    together.
    """

    original_media_url: Optional[str] = None
    """The original URL to the PDF used for the fax's media.

    If media_name was supplied, this is omitted
    """

    status: Optional[Literal["failed"]] = None
    """The status of the fax."""

    to: Optional[str] = None
    """The phone number, in E.164 format, the fax will be sent to or SIP URI"""

    user_id: Optional[str] = None
    """Identifier of the user to whom the fax belongs"""


class FaxFailedWebhookEvent(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["fax.failed"]] = None
    """The type of event being delivered."""

    payload: Optional[Payload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""
