# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["MobileNetworkOperatorListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    country_code: Optional[str] = None
    """The mobile operator two-character (ISO 3166-1 alpha-2) origin country code."""

    mcc: Optional[str] = None
    """MCC stands for Mobile Country Code.

    It's a three decimal digit that identifies a country.<br/><br/> This code is
    commonly seen joined with a Mobile Network Code (MNC) in a tuple that allows
    identifying a carrier known as PLMN (Public Land Mobile Network) code.
    """

    mnc: Optional[str] = None
    """MNC stands for Mobile Network Code.

    It's a two to three decimal digits that identify a network.<br/><br/> This code
    is commonly seen joined with a Mobile Country Code (MCC) in a tuple that allows
    identifying a carrier known as PLMN (Public Land Mobile Network) code.
    """

    name: Optional[str] = None
    """The network operator name."""

    network_preferences_enabled: Optional[bool] = None
    """
    Indicate whether the mobile network operator can be set as preferred in the
    Network Preferences API.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    tadig: Optional[str] = None
    """TADIG stands for Transferred Account Data Interchange Group.

    The TADIG code is a unique identifier for network operators in GSM mobile
    networks.
    """


class MobileNetworkOperatorListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
