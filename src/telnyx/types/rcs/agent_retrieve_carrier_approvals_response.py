# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from .carrier_approval_response import CarrierApprovalResponse

__all__ = ["AgentRetrieveCarrierApprovalsResponse"]

AgentRetrieveCarrierApprovalsResponse: TypeAlias = List[CarrierApprovalResponse]
