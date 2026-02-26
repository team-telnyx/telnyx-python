# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .sub_number_orders_report import SubNumberOrdersReport

__all__ = ["SubNumberOrdersReportRetrieveResponse"]


class SubNumberOrdersReportRetrieveResponse(BaseModel):
    data: Optional[SubNumberOrdersReport] = None
