# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .ledger_billing_group_report import LedgerBillingGroupReport

__all__ = ["LedgerBillingGroupReportRetrieveResponse"]


class LedgerBillingGroupReportRetrieveResponse(BaseModel):
    data: Optional[LedgerBillingGroupReport] = None
