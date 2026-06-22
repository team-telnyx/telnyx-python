# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .document_param import DocumentParam

__all__ = ["InfringementClaimContestParams"]


class InfringementClaimContestParams(TypedDict, total=False):
    contest_notes: Required[str]
    """Customer's response to the claim. 10–2000 characters."""

    documents: Iterable[DocumentParam]
    """Up to 20 supporting documents per submission.

    `document_id` must be unique within this submission. Documents are aggregated
    into the claim's `contest_documents` across all submissions.
    """
