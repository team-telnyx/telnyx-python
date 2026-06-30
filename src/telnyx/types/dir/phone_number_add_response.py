# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .dir_phone_number import DirPhoneNumber

__all__ = ["PhoneNumberAddResponse"]


class PhoneNumberAddResponse(BaseModel):
    """Bulk-add success response (HTTP 201).

    All numbers in the request were accepted into a single new batch. Every entry in `data` shares the same `batch_id` - read it from any element to obtain the batch id for subsequent `GET .../phone_number_batches/{batch_id}` calls. If any number in the request fails (schema-invalid, not in inventory, already attached to another DIR, etc.) the entire request is rejected with HTTP 400 and the canonical Telnyx error envelope; the success body described here is therefore an all-or-nothing payload.
    """

    data: List[DirPhoneNumber]
    """Phone numbers accepted into the new batch.

    List order mirrors the request order. Each element shares the same `batch_id`.
    """
