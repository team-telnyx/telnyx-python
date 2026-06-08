# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DirListResponse", "CallReason", "Document", "RejectionReason"]


class CallReason(BaseModel):
    created_at: Optional[datetime] = None

    reason: Optional[str] = None


class Document(BaseModel):
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


class RejectionReason(BaseModel):
    code: Optional[str] = None

    detail: Optional[str] = None

    message: Optional[str] = None
    """Customer-visible free-text comment from the Telnyx vetting team.

    Only the first entry of `rejection_reasons` carries this; the rest are `null`.
    """

    title: Optional[str] = None


class DirListResponse(BaseModel):
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
