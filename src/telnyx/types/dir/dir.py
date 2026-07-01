# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..document import Document
from ..dir_status import DirStatus
from .rejection_reason import RejectionReason

__all__ = ["Dir", "CallReason"]


class CallReason(BaseModel):
    created_at: Optional[datetime] = None

    reason: Optional[str] = None


class Dir(BaseModel):
    id: Optional[str] = None

    authorizer_email: Optional[str] = None

    authorizer_name: Optional[str] = None

    call_reasons: Optional[List[CallReason]] = None

    certify_brand_is_accurate: Optional[bool] = None

    certify_ip_ownership: Optional[bool] = None

    certify_no_shaft_content: Optional[bool] = None

    created_at: Optional[datetime] = None

    display_name: Optional[str] = None

    documents: Optional[List[Document]] = None

    enterprise_id: Optional[str] = None

    expiring_at: Optional[datetime] = None

    logo_url: Optional[str] = None

    rejected_at: Optional[datetime] = None

    rejection_reasons: Optional[List[RejectionReason]] = None
    """
    Populated when `status` is `rejected`; cleared on `/submit` or successful
    approval.
    """

    reselling: Optional[bool] = None

    status: Optional[DirStatus] = None
    """DIR lifecycle status.

    - `draft` - newly created; editable; not yet submitted.
    - `submitted` / `in_review` - Telnyx is reviewing.
    - `verified` - approved; phone numbers may be attached.
    - `rejected` - Telnyx rejected this submission; `rejection_reasons` is
      populated; customer can edit and resubmit.
    - `unsuccessful` - system-side error during processing; customer can edit and
      resubmit.
    - `suspended` - temporarily disabled (e.g. by an active infringement claim).
    - `expired` - verification expired; customer must resubmit.
    - `infringement_claimed` - a trademark/impersonation claim is open against this
      DIR.
    - `permanently_rejected` - terminal; cannot be resubmitted.
    """

    submitted_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    verified_at: Optional[datetime] = None
