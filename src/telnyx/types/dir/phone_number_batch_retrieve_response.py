# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .phone_number_batch import PhoneNumberBatch

__all__ = ["PhoneNumberBatchRetrieveResponse"]


class PhoneNumberBatchRetrieveResponse(BaseModel):
    data: PhoneNumberBatch
    """A phone-number batch groups all numbers added in a single bulk-add request.

    Telnyx vets the batch as a unit. The response embeds the full `phone_numbers`
    array so you can read per-number status without a separate call, plus a
    batch-level `status` summarising the unit's progress.
    """
