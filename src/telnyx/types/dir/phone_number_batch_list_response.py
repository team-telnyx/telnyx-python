# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PhoneNumberBatchListResponse", "Document", "PhoneNumber", "PhoneNumberRejectionReason"]


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


class PhoneNumberRejectionReason(BaseModel):
    """Populated when `status` is `unsuccessful` or `permanently_rejected`."""

    code: Optional[str] = None

    detail: Optional[str] = None

    message: Optional[str] = None
    """Customer-visible free-text comment from the Telnyx vetting team.

    Only the first entry of `rejection_reasons` carries this; the rest are `null`.
    """

    title: Optional[str] = None


class PhoneNumber(BaseModel):
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

    rejection_reason: Optional[PhoneNumberRejectionReason] = None
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


class PhoneNumberBatchListResponse(BaseModel):
    """A phone-number batch groups all numbers added in a single bulk-add request.

    Telnyx vets the batch as a unit. The response embeds the full `phone_numbers` array so you can read per-number status without a separate call, plus a batch-level `status` summarising the unit's progress.
    """

    batch_id: Optional[str] = None

    dir_display_name: Optional[str] = None
    """The DIR's display name at the time the batch was read."""

    dir_id: Optional[str] = None

    documents: Optional[List[Document]] = None
    """Documents attached to this batch (e.g.

    a Letter of Authorization). Empty when none were supplied at add time.
    """

    enterprise_id: Optional[str] = None

    phone_numbers: Optional[List[PhoneNumber]] = None
    """All phone numbers in this batch, with per-number status."""

    status: Optional[
        Literal["submitted", "in_review", "verified", "unsuccessful", "suspended", "expired", "permanently_rejected"]
    ] = None
    """Aggregate batch status.

    Mirrors the values used on individual phone numbers (`submitted`, `in_review`,
    `verified`, `unsuccessful`, `permanently_rejected`, etc.).
    """

    submitted_at: Optional[datetime] = None
    """When the batch was created (and implicitly submitted for vetting)."""

    total_count: Optional[int] = None
    """Number of phone numbers in this batch (length of `phone_numbers`)."""
