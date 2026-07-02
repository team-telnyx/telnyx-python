# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .document_param import DocumentParam

__all__ = ["DirUpdateInfringementParams"]


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

    documents: Optional[Iterable[DocumentParam]]
    """Append-only supporting documents to attach while resolving the claim (e.g.

    authorization or licensing proof).
    """

    logo_url: Optional[str]
    """Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB)."""
