# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionSetPrivateWirelessGatewayResponse", "Data", "DataSettings"]


class DataSettings(BaseModel):
    private_wireless_gateway_id: Optional[str] = None
    """The identification of the related Private Wireless Gateway resource."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    settings: Optional[DataSettings] = None
    """A JSON object representation of the action params."""

    sim_card_group_id: Optional[str] = None
    """The SIM card group identification."""

    status: Optional[Literal["in-progress", "completed", "failed"]] = None

    type: Optional[
        Literal[
            "set_private_wireless_gateway",
            "remove_private_wireless_gateway",
            "set_wireless_blocklist",
            "remove_wireless_blocklist",
        ]
    ] = None
    """Represents the type of the operation requested."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class ActionSetPrivateWirelessGatewayResponse(BaseModel):
    data: Optional[Data] = None
    """This object represents a SIM card group action request.

    It allows tracking the current status of an operation that impacts the SIM card
    group and SIM card in it.
    """
