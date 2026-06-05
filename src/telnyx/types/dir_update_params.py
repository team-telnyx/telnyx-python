# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["DirUpdateParams"]


class DirUpdateParams(TypedDict, total=False):
    authorizer_email: str
    """Contact email of the authorizer.

    Telnyx may send verification or infringement notices here.
    """

    authorizer_name: str
    """Name of the person at your enterprise authorizing this DIR.

    Must be a real individual.
    """

    call_reasons: SequenceNotStr[str]
    """1–10 reasons your business calls customers.

    Validate phrasing against `POST /call_reasons/validate`.
    """

    display_name: str
    """Name shown to call recipients. 1–35 characters, no emoji, not whitespace-only."""

    logo_url: str
    """Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB)."""

    reselling: bool
    """
    Set to true if your organization places calls on behalf of other enterprises
    (BPO/reseller). Updating this triggers re-vetting on next submit.
    """
