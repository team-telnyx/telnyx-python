# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .month_detail import MonthDetail

__all__ = [
    "ChargesSummaryRetrieveResponse",
    "Data",
    "DataSummary",
    "DataSummaryAdjustment",
    "DataSummaryLine",
    "DataSummaryLineComparative",
    "DataSummaryLineSimple",
    "DataTotal",
]


class DataSummaryAdjustment(BaseModel):
    amount: str
    """Adjustment amount as decimal string"""

    description: str
    """Description of the adjustment"""

    event_date: date
    """Date when the adjustment occurred"""


class DataSummaryLineComparative(BaseModel):
    alias: str
    """Service alias"""

    existing_this_month: MonthDetail

    name: str
    """Service name"""

    new_this_month: MonthDetail

    type: Literal["comparative"]


class DataSummaryLineSimple(BaseModel):
    alias: str
    """Service alias"""

    amount: str
    """Total amount as decimal string"""

    name: str
    """Service name"""

    quantity: int
    """Number of items"""

    type: Literal["simple"]


DataSummaryLine: TypeAlias = Annotated[
    Union[DataSummaryLineComparative, DataSummaryLineSimple], PropertyInfo(discriminator="type")
]


class DataSummary(BaseModel):
    adjustments: List[DataSummaryAdjustment]
    """List of billing adjustments"""

    lines: List[DataSummaryLine]
    """List of charge summary lines"""


class DataTotal(BaseModel):
    credits: str
    """Total credits as decimal string"""

    existing_mrc: str
    """Total existing monthly recurring charges as decimal string"""

    grand_total: str
    """Grand total of all charges as decimal string"""

    ledger_adjustments: str
    """Ledger adjustments as decimal string"""

    new_mrc: str
    """Total new monthly recurring charges as decimal string"""

    new_otc: str
    """Total new one-time charges as decimal string"""

    other: str
    """Other charges as decimal string"""


class Data(BaseModel):
    currency: str
    """Currency code"""

    end_date: date
    """End date of the summary period"""

    start_date: date
    """Start date of the summary period"""

    summary: DataSummary

    total: DataTotal

    user_email: str
    """User email address"""

    user_id: str
    """User identifier"""


class ChargesSummaryRetrieveResponse(BaseModel):
    data: Data
