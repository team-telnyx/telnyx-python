# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TelephonyCredential"]


class TelephonyCredential(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO-8601 formatted date indicating when the resource was created."""

    expired: Optional[bool] = None
    """Defaults to false"""

    expires_at: Optional[str] = None
    """ISO-8601 formatted date indicating when the resource will expire."""

    name: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    resource_id: Optional[str] = None
    """Identifies the resource this credential is associated with."""

    sip_password: Optional[str] = None
    """The randomly generated SIP password for the credential."""

    sip_username: Optional[str] = None
    """The randomly generated SIP username for the credential."""

    updated_at: Optional[str] = None
    """ISO-8601 formatted date indicating when the resource was updated."""
