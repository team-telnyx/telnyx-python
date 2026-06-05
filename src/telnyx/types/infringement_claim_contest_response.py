# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InfringementClaimContestResponse", "Data", "DataContestDocument", "DataContestHistory", "DataDir"]


class DataContestDocument(BaseModel):
    document_id: str
    """
    Id returned by the Telnyx Documents API after you upload the file (upload via
    `POST /v2/documents`; see https://developers.telnyx.com/api/documents).
    """

    document_type: Literal[
        "letter_of_authorization",
        "business_registration",
        "articles_of_incorporation",
        "tax_document",
        "ein_letter",
        "trademark_registration",
        "website_ownership",
        "business_license",
        "professional_license",
        "government_id",
        "utility_bill",
        "bank_statement",
        "other",
    ]
    """Type of supporting document.

    Pick the closest match to what the file actually contains; `other` triggers
    manual vetting and may slow approval. The matching short_name reference list is
    at `GET /v2/dir/document_types`.
    """

    description: Optional[str] = None


class DataContestHistory(BaseModel):
    """One round of customer contest evidence on an infringement claim.

    The aggregated documents across rounds live on the parent claim's `contest_documents`; this submission record carries only the per-round notes and document count.
    """

    document_count: Optional[int] = None

    notes: Optional[str] = None

    submitted_at: Optional[datetime] = None


class DataDir(BaseModel):
    """Snapshot of the DIR the claim is filed against, embedded for convenience."""

    id: Optional[str] = None

    display_name: Optional[str] = None

    enterprise_id: Optional[str] = None

    status: Optional[
        Literal[
            "draft",
            "submitted",
            "in_review",
            "verified",
            "rejected",
            "unsuccessful",
            "suspended",
            "expired",
            "infringement_claimed",
            "permanently_rejected",
        ]
    ] = None
    """DIR lifecycle status.

    - `draft` — newly created; editable; not yet submitted.
    - `submitted` / `in_review` — Telnyx is reviewing.
    - `verified` — approved; phone numbers may be attached.
    - `rejected` — Telnyx rejected this submission; `rejection_reasons` is
      populated; customer can edit and resubmit.
    - `unsuccessful` — system-side error during processing; customer can edit and
      resubmit.
    - `suspended` — temporarily disabled (e.g. by an active infringement claim).
    - `expired` — verification expired; customer must resubmit.
    - `infringement_claimed` — a trademark/impersonation claim is open against this
      DIR.
    - `permanently_rejected` — terminal; cannot be resubmitted.
    """


class Data(BaseModel):
    id: Optional[str] = None

    claim_date: Optional[datetime] = None
    """When the claim was filed (set by the claimant's representative at file time)."""

    claim_description: Optional[str] = None

    claim_type: Optional[Literal["trademark", "copyright"]] = None
    """Category of infringement being claimed."""

    claimant_contact: Optional[str] = None

    claimant_name: Optional[str] = None

    contest_documents: Optional[List[DataContestDocument]] = None
    """Aggregated across all customer contest submissions on this claim."""

    contest_history: Optional[List[DataContestHistory]] = None
    """Per-round submission audit trail.

    Each entry records one `POST /infringement_claims/{id}/contest` call (notes,
    timestamp, document count). Aggregated documents live on `contest_documents`.
    """

    created_at: Optional[datetime] = None

    dir: Optional[DataDir] = None
    """Snapshot of the DIR the claim is filed against, embedded for convenience."""

    dir_id: Optional[str] = None

    enterprise_id: Optional[str] = None

    resolution: Optional[Literal["upheld", "rejected", "modified"]] = None
    """Set only when `status` is `resolved`."""

    resolution_date: Optional[datetime] = None

    resolution_notes: Optional[str] = None

    status: Optional[Literal["pending", "contested", "resolved"]] = None
    """Lifecycle status.

    `pending` — newly filed; the DIR is auto-suspended. `contested` — you have
    submitted contest evidence; awaiting Telnyx review. `resolved` — final.
    """

    updated_at: Optional[datetime] = None


class InfringementClaimContestResponse(BaseModel):
    data: Data
