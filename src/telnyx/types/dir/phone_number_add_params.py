# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PhoneNumberAddParams", "Document"]


class PhoneNumberAddParams(TypedDict, total=False):
    documents: Required[Iterable[Document]]
    """Supporting documents covering this batch.

    At least one entry with `document_type: letter_of_authorization` is required —
    the LOA authorises Telnyx to register these numbers under the DIR. Each
    `document_id` must come from the Telnyx Documents API. Additional document types
    (e.g. business registration) may be included alongside the LOA.
    """

    phone_numbers: Required[SequenceNotStr[str]]
    """1–15 phone numbers in E.164 format.

    10-digit US numbers are auto-prefixed with `1`.
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
