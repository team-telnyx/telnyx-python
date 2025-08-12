# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CallRetrieveResponse"]


class CallRetrieveResponse(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    answered_by: Optional[Literal["human", "machine", "not_sure"]] = None
    """
    The value of the answering machine detection result, if this feature was enabled
    for the call.
    """

    caller_name: Optional[str] = None
    """Caller ID, if present."""

    date_created: Optional[str] = None
    """The timestamp of when the resource was created."""

    date_updated: Optional[str] = None
    """The timestamp of when the resource was last updated."""

    direction: Optional[Literal["inbound", "outbound"]] = None
    """The direction of this call."""

    duration: Optional[str] = None
    """The duration of this call, given in seconds."""

    end_time: Optional[str] = None
    """The end time of this call."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The phone number or SIP address that made this call."""

    from_formatted: Optional[str] = None
    """The from number formatted for display."""

    price: Optional[str] = None
    """The price of this call, the currency is specified in the price_unit field.

    Only populated when the call cost feature is enabled for the account.
    """

    price_unit: Optional[str] = None
    """The unit in which the price is given."""

    sid: Optional[str] = None
    """The identifier of this call."""

    start_time: Optional[str] = None
    """The start time of this call."""

    status: Optional[Literal["ringing", "in-progress", "canceled", "completed", "failed", "busy", "no-answer"]] = None
    """The status of this call."""

    to: Optional[str] = None
    """The phone number or SIP address that received this call."""

    to_formatted: Optional[str] = None
    """The to number formatted for display."""

    uri: Optional[str] = None
    """The relative URI for this call."""
