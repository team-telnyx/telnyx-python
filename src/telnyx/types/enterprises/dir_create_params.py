# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..document_param import DocumentParam

__all__ = ["DirCreateParams"]


class DirCreateParams(TypedDict, total=False):
    authorizer_email: Required[str]
    """Contact email of the authorizer.

    Telnyx may send verification or infringement-notice email here; use a monitored
    mailbox.
    """

    authorizer_name: Required[str]
    """Name of the person at your enterprise who is authorizing this DIR registration.

    Must be a real individual (used for audit and trademark-claim contests).
    """

    certify_brand_is_accurate: Required[Literal[True]]
    """Must be `true`."""

    certify_ip_ownership: Required[Literal[True]]
    """Must be `true`. Confirms ownership of any logos/trademarks shown."""

    certify_no_shaft_content: Required[Literal[True]]
    """Must be `true`.

    Confirms this DIR is not used for SHAFT content (Sex, Hate, Alcohol, Firearms,
    Tobacco) where prohibited.
    """

    display_name: Required[str]
    """Name shown to call recipients. No emoji; not whitespace-only."""

    call_reasons: SequenceNotStr[str]
    """1–10 reasons your business calls customers.

    Validate phrasing against `POST /call_reasons/validate`.
    """

    documents: Iterable[DocumentParam]
    """Supporting documents. Each `document_id` may appear at most once on a DIR."""

    logo_url: str
    """Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB)."""

    reselling: bool
    """
    Set to true if your organization places calls on behalf of other enterprises
    (BPO/reseller).
    """
