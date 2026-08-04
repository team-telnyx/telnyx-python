# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .quality import Quality
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

    failure_reason: Optional[str] = None
    """Customer-facing failure reason for the fax.

    Present on every fax object (null when the fax has not failed). Mapped from the
    more granular `internal_failure_reason`. Common values include:
    `receiver_call_dropped`, `sender_call_dropped`, `sender_canceled`,
    `carrier_lost`, `service_unavailable`, `fax_signaling_error`,
    `receiver_communication_error`, `sender_communication_error`,
    `receiver_decline`, `receiver_recovery_on_timer_expire`, `receiver_no_response`,
    `receiver_invalid_number_format`, `receiver_no_answer`,
    `receiver_incompatible_destination`, `receiver_unallocated_number`,
    `destination_unreachable`, `user_busy`, `invalid_ecm_response_from_receiver`,
    `fax_initial_communication_timeout`, `destination_not_in_service_plan`,
    `account_disabled`, `destination_invalid`, `no_outbound_profile`,
    `destination_not_in_countries_whitelist`, `user_channel_limit_exceeded`,
    `outbound_profile_channel_limit_exceeded`, `connection_channel_limit_exceeded`,
    `outbound_profile_daily_spend_limit_exceeded`, `unverified_origination_number`,
    `unverified_destination_not_allowed`, `file_format_invalid`,
    `file_download_failed`, `file_size_limit_exceeded`, `page_count_limit_exceeded`,
    `media_processing_exception`.
    """

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The phone number, in E.164 format, the fax will be sent from."""

    from_display_name: Optional[str] = None
    """
    The string used as the caller id name (SIP From Display Name) presented to the
    destination (`to` number).
    """

    internal_failure_reason: Optional[str] = None
    """Internal, more granular failure reason for the fax.

    Present on every fax object (null when the fax has not failed). Useful for
    deeper debugging beyond the customer-facing `failure_reason`.
    """

    media_name: Optional[str] = None
    """The media_name used for the fax's media.

    Must point to a file previously uploaded to api.telnyx.com/v2/media by the same
    user/organization. Supported formats: PDF, TIFF, JPEG, PNG, DOC, DOCX, RTF, and
    TXT. media_name and media_url/contents can't be submitted together.
    """

    media_url: Optional[str] = None
    """The URL (or list of URLs) to the fax document.

    Supported formats: PDF, TIFF, JPEG, PNG, DOC, DOCX, RTF, and TXT. media_url and
    media_name/contents can't be submitted together.
    """

    preview_url: Optional[str] = None
    """If `store_preview` was set to `true`, this is a link to temporary location.

    Link expires after 10 minutes.
    """

    quality: Optional[Quality] = None
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
