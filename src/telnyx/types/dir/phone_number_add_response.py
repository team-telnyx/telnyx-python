# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PhoneNumberAddResponse", "Data", "DataRejectionReason"]


class DataRejectionReason(BaseModel):
    """Populated when `status` is `unsuccessful` or `permanently_rejected`."""

    code: Optional[str] = None

    detail: Optional[str] = None

    message: Optional[str] = None
    """Customer-visible free-text comment from the Telnyx vetting team.

    Only the first entry of `rejection_reasons` carries this; the rest are `null`.
    """

    title: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    batch_id: Optional[str] = None
    """Id of the batch this number was vetted as part of."""

    created_at: Optional[datetime] = None

    dir_id: Optional[str] = None

    enterprise_id: Optional[str] = None

    loa_document_id: Optional[str] = None
    """Id of the Letter of Authorization document attached to this number's batch."""

    phone_number: Optional[str] = None
    """E.164 with leading `+`."""

    rejection_reason: Optional[DataRejectionReason] = None
    """Populated when `status` is `unsuccessful` or `permanently_rejected`."""

    status: Optional[
        Literal["submitted", "in_review", "verified", "unsuccessful", "suspended", "expired", "permanently_rejected"]
    ] = None
    """Phone-number lifecycle status.

    - `submitted` / `in_review` - Telnyx is reviewing the batch this number belongs
      to.
    - `verified` - approved; the DIR's display identity will be shown on outbound
      calls from this number.
    - `unsuccessful` - Telnyx rejected this submission; the customer may re-add to
      retry.
    - `suspended` - temporarily disabled (e.g. by an active infringement claim on
      the DIR).
    - `expired` - verification expired; re-add to renew.
    - `permanently_rejected` - terminal; cannot be re-added on this or any other DIR
      you own.
    """

    updated_at: Optional[datetime] = None

    verified_at: Optional[datetime] = None


class PhoneNumberAddResponse(BaseModel):
    """Bulk-add success response (HTTP 201).

    All numbers in the request were accepted into a single new batch. Every entry in `data` shares the same `batch_id` - read it from any element to obtain the batch id for subsequent `GET .../phone_number_batches/{batch_id}` calls. If any number in the request fails (schema-invalid, not in inventory, already attached to another DIR, etc.) the entire request is rejected with HTTP 400 and the canonical Telnyx error envelope; the success body described here is therefore an all-or-nothing payload.
    """

    data: List[Data]
    """Phone numbers accepted into the new batch.

    List order mirrors the request order. Each element shares the same `batch_id`.
    """
