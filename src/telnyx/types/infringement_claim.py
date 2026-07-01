# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .document import Document
from .dir_status import DirStatus

__all__ = ["InfringementClaim", "ContestHistory", "Dir"]


class ContestHistory(BaseModel):
    """One round of customer contest evidence on an infringement claim.

    The aggregated documents across rounds live on the parent claim's `contest_documents`; this submission record carries only the per-round notes and document count.
    """

    document_count: Optional[int] = None

    notes: Optional[str] = None

    submitted_at: Optional[datetime] = None


class Dir(BaseModel):
    """Snapshot of the DIR the claim is filed against, embedded for convenience."""

    id: Optional[str] = None

    display_name: Optional[str] = None

    enterprise_id: Optional[str] = None

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


class InfringementClaim(BaseModel):
    id: Optional[str] = None

    claim_date: Optional[datetime] = None
    """When the claim was filed (set by the claimant's representative at file time)."""

    claim_description: Optional[str] = None

    claim_type: Optional[Literal["trademark", "copyright"]] = None
    """Category of infringement being claimed."""

    claimant_contact: Optional[str] = None

    claimant_name: Optional[str] = None

    contest_documents: Optional[List[Document]] = None
    """Aggregated across all customer contest submissions on this claim."""

    contest_history: Optional[List[ContestHistory]] = None
    """Per-round submission audit trail.

    Each entry records one `POST /infringement_claims/{id}/contest` call (notes,
    timestamp, document count). Aggregated documents live on `contest_documents`.
    """

    created_at: Optional[datetime] = None

    dir: Optional[Dir] = None
    """Snapshot of the DIR the claim is filed against, embedded for convenience."""

    dir_id: Optional[str] = None

    enterprise_id: Optional[str] = None

    resolution: Optional[Literal["upheld", "rejected", "modified"]] = None
    """Set only when `status` is `resolved`."""

    resolution_date: Optional[datetime] = None

    resolution_notes: Optional[str] = None

    status: Optional[Literal["pending", "contested", "resolved"]] = None
    """Lifecycle status.

    `pending` - newly filed; the DIR is auto-suspended. `contested` - you have
    submitted contest evidence; awaiting Telnyx review. `resolved` - final.
    """

    updated_at: Optional[datetime] = None
