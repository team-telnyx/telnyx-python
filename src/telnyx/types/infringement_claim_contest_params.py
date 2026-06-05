# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InfringementClaimContestParams", "Document"]


class InfringementClaimContestParams(TypedDict, total=False):
    contest_notes: Required[str]
    """Customer's response to the claim. 10–2000 characters."""

    documents: Iterable[Document]
    """Up to 20 supporting documents per submission.

    `document_id` must be unique within this submission. Documents are aggregated
    into the claim's `contest_documents` across all submissions.
    """


class Document(TypedDict, total=False):
    document_id: Required[str]
    """
    Id returned by the Telnyx Documents API after you upload the file (upload via
    `POST /v2/documents`; see https://developers.telnyx.com/api/documents).
    """

    document_type: Required[
        Literal[
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
    ]
    """Type of supporting document.

    Pick the closest match to what the file actually contains; `other` triggers
    manual vetting and may slow approval. The matching short_name reference list is
    at `GET /v2/dir/document_types`.
    """

    description: str
