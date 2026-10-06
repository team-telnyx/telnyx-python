# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..document_param import DocumentParam
from ..bpo_authorization_input_param import BpoAuthorizationInputParam

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

    call_reasons: Required[SequenceNotStr[str]]
    """1–10 reasons your business calls customers.

    Validate phrasing against `POST /call_reasons/validate`.
    """

    certify_brand_is_accurate: Required[Literal[True]]
    """Certification that the DIR information is accurate.

    Must be `true` for the DIR to be submitted for vetting.
    """

    certify_ip_ownership: Required[Literal[True]]
    """Must be `true`. Confirms ownership of any logos/trademarks shown."""

    certify_no_shaft_content: Required[Literal[True]]
    """Must be `true`.

    Confirms this DIR is not used for SHAFT content (Sex, Hate, Alcohol, Firearms,
    Tobacco) where prohibited.
    """

    display_name: Required[str]
    """Name shown to call recipients. No emoji; not whitespace-only."""

    bpo_authorizations: Iterable[BpoAuthorizationInputParam]
    """Optional.

    Approved BPO (Business Process Outsourcer) accounts on your organization
    authorized to place branded calls for this DIR, each with the signed Letter of
    Authorization the Brand Owner granted it. Each authorization starts `pending`
    and takes effect only after an admin reviews its Letter of Authorization. Omit
    or send an empty list to authorize no BPO on this DIR. Maximum 10.
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

    webhook_url: Optional[str]
    """
    Optional `https://` URL that receives webhook notifications when this DIR's
    compliance review completes (rejection outcomes include structured rejection
    reasons). Maximum 2048 characters.
    """
