# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SupportingDocumentCreateParams", "Document"]


class SupportingDocumentCreateParams(TypedDict, total=False):
    documents: Iterable[Document]
    """List of supporting documents parameters"""


class Document(TypedDict, total=False):
    document_id: Required[str]
    """Identifies the associated document"""

    type: Required[Literal["loa", "invoice"]]
    """Identifies the type of the document"""
