# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PhoneNumberListResponse", "RejectionReason"]


class RejectionReason(BaseModel):
    """Populated when `status` is `unsuccessful` or `permanently_rejected`."""

    code: Optional[str] = None

    detail: Optional[str] = None

    message: Optional[str] = None
    """Customer-visible free-text comment from the Telnyx vetting team.

    Only the first entry of `rejection_reasons` carries this; the rest are `null`.
    """

    title: Optional[str] = None


class PhoneNumberListResponse(BaseModel):
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

    rejection_reason: Optional[RejectionReason] = None
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
