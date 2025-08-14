# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OtaUpdateRetrieveResponse", "Data", "DataSettings", "DataSettingsMobileNetworkOperatorsPreference"]


class DataSettingsMobileNetworkOperatorsPreference(BaseModel):
    mobile_network_operator_id: Optional[str] = None
    """The mobile network operator resource identification UUID."""

    mobile_network_operator_name: Optional[str] = None
    """The mobile network operator resource name."""

    priority: Optional[int] = None
    """
    It determines what is the priority of a specific network operator that should be
    assumed by a SIM card when connecting to a network. The highest priority is 0,
    the second highest is 1 and so on.
    """


class DataSettings(BaseModel):
    mobile_network_operators_preferences: Optional[List[DataSettingsMobileNetworkOperatorsPreference]] = None
    """
    A list of mobile network operators and the priority that should be applied when
    the SIM is connecting to the network.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    settings: Optional[DataSettings] = None
    """A JSON object representation of the operation.

    The information present here will relate directly to the source of the OTA
    request.
    """

    sim_card_id: Optional[str] = None
    """The identification UUID of the related SIM card resource."""

    status: Optional[Literal["in-progress", "completed", "failed"]] = None

    type: Optional[Literal["sim_card_network_preferences"]] = None
    """Represents the type of the operation requested.

    This will relate directly to the source of the request.
    """

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class OtaUpdateRetrieveResponse(BaseModel):
    data: Optional[Data] = None
    """This object represents an Over the Air (OTA) update request.

    It allows tracking the current status of a operation that apply settings in a
    particular SIM card. <br/><br/>
    """
