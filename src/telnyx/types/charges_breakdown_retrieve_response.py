# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import date

from .._models import BaseModel

__all__ = ["ChargesBreakdownRetrieveResponse", "Data", "DataResult", "DataResultService"]


class DataResultService(BaseModel):
    cost: str
    """Cost per unit as decimal string"""

    cost_type: str
    """Type of cost (MRC or OTC)"""

    name: str
    """Service name"""


class DataResult(BaseModel):
    charge_type: str
    """Type of charge for the number"""

    service_owner_email: str
    """Email address of the service owner"""

    service_owner_user_id: str
    """User ID of the service owner"""

    services: List[DataResultService]
    """List of services associated with this number"""

    tn: str
    """Phone number"""


class Data(BaseModel):
    currency: str
    """Currency code"""

    end_date: date
    """End date of the breakdown period"""

    results: List[DataResult]
    """List of phone number charge breakdowns"""

    start_date: date
    """Start date of the breakdown period"""

    user_email: str
    """User email address"""

    user_id: str
    """User identifier"""


class ChargesBreakdownRetrieveResponse(BaseModel):
    data: Data
