# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["AdditionalDocumentCreateParams", "AdditionalDocument"]


class AdditionalDocumentCreateParams(TypedDict, total=False):
    additional_documents: Iterable[AdditionalDocument]


class AdditionalDocument(TypedDict, total=False):
    document_id: str
    """The document identification"""

    document_type: Literal["loa", "invoice", "csr", "other"]
    """The type of document being created."""
