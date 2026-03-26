# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.reputation_phone_number_with_reputation_data import ReputationPhoneNumberWithReputationData

__all__ = ["NumberRetrieveResponse"]


class NumberRetrieveResponse(BaseModel):
    data: Optional[ReputationPhoneNumberWithReputationData] = None
