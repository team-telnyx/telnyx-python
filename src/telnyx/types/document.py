# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document"]


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
