# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DirUpdateInfringementParams", "Document"]


class DirUpdateInfringementParams(TypedDict, total=False):
    certify_brand_is_accurate: Required[Literal[True]]
    """Must be `true`."""

    certify_ip_ownership: Required[Literal[True]]
    """Must be `true`."""

    certify_no_infringement: Required[Literal[True]]
    """Must be `true`."""

    certify_no_shaft_content: Required[Literal[True]]
    """Must be `true`."""

    infringement_resolution_notes: Required[str]
    """Explanation of how the infringement concern was addressed."""

    call_reasons: Optional[SequenceNotStr[str]]

    display_name: Optional[str]

    documents: Optional[Iterable[Document]]
    """Append-only supporting documents."""

    logo_url: Optional[str]
    """Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB)."""


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
