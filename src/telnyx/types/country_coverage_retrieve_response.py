# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["CountryCoverageRetrieveResponse", "Data", "DataLocal", "DataTollFree"]


class DataLocal(BaseModel):
    features: Optional[List[str]] = None

    international_sms: Optional[bool] = None

    p2p: Optional[bool] = None

    quickship: Optional[bool] = None

    reservable: Optional[bool] = None


class DataTollFree(BaseModel):
    features: Optional[List[str]] = None

    international_sms: Optional[bool] = None

    p2p: Optional[bool] = None

    quickship: Optional[bool] = None

    reservable: Optional[bool] = None


class Data(BaseModel):
    code: Optional[str] = None
    """Country ISO code"""

    features: Optional[List[str]] = None
    """Set of features supported"""

    international_sms: Optional[bool] = None

    inventory_coverage: Optional[bool] = None
    """Indicates whether country can be queried with inventory coverage endpoint"""

    local: Optional[DataLocal] = None

    mobile: Optional[Dict[str, object]] = None

    national: Optional[Dict[str, object]] = None

    numbers: Optional[bool] = None

    p2p: Optional[bool] = None

    phone_number_type: Optional[List[str]] = None
    """Phone number type"""

    quickship: Optional[bool] = None
    """Supports quickship"""

    reservable: Optional[bool] = None
    """Supports reservable"""

    shared_cost: Optional[Dict[str, object]] = None

    toll_free: Optional[DataTollFree] = None


class CountryCoverageRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
