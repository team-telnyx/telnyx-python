# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bulk_sim_card_action_detailed import BulkSimCardActionDetailed

__all__ = ["BulkSimCardActionRetrieveResponse"]


class BulkSimCardActionRetrieveResponse(BaseModel):
    data: Optional[BulkSimCardActionDetailed] = None
