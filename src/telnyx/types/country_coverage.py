# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["CountryCoverage", "Local", "TollFree"]


class Local(BaseModel):
    features: Optional[List[str]] = None

    full_pstn_replacement: Optional[bool] = None

    international_sms: Optional[bool] = None

    p2p: Optional[bool] = None

    quickship: Optional[bool] = None

    reservable: Optional[bool] = None


class TollFree(BaseModel):
    features: Optional[List[str]] = None

    full_pstn_replacement: Optional[bool] = None

    international_sms: Optional[bool] = None

    p2p: Optional[bool] = None

    quickship: Optional[bool] = None

    reservable: Optional[bool] = None


class CountryCoverage(BaseModel):
    code: Optional[str] = None
    """Country ISO code"""

    features: Optional[List[str]] = None
    """Set of features supported"""

    international_sms: Optional[bool] = None

    inventory_coverage: Optional[bool] = None
    """Indicates whether country can be queried with inventory coverage endpoint"""

    local: Optional[Local] = None

    mobile: Optional[Dict[str, object]] = None

    national: Optional[Dict[str, object]] = None

    numbers: Optional[bool] = None

    p2p: Optional[bool] = None

    phone_number_type: Optional[List[str]] = None
    """Phone number type"""

    quickship: Optional[bool] = None
    """Supports quickship"""

    region: Optional[str] = None
    """Geographic region (e.g., AMER, EMEA, APAC)"""

    reservable: Optional[bool] = None
    """Supports reservable"""

    shared_cost: Optional[Dict[str, object]] = None

    toll_free: Optional[TollFree] = None
