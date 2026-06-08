# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DirCreateLoaParams", "Agent", "Signature"]


class DirCreateLoaParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """
    Telephone numbers to authorize on the DIR, in `+E164` format (`+` followed by
    10-15 digits). Max 15 per request.
    """

    agent: Agent
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    signature: Signature
    """Optional.

    When provided the rendered PDF embeds the signature image, printed name, and
    signed-at date. When absent the PDF is returned unsigned so the customer can
    sign externally and upload it via the Documents API.
    """


class Agent(TypedDict, total=False):
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    administrative_area: Required[str]

    city: Required[str]

    contact_email: Required[str]

    contact_name: Required[str]

    contact_phone: Required[str]

    contact_title: Required[str]

    country: Required[str]

    legal_name: Required[str]

    postal_code: Required[str]

    street_address: Required[str]

    dba: Optional[str]

    extended_address: Optional[str]


class Signature(TypedDict, total=False):
    """Optional.

    When provided the rendered PDF embeds the signature image, printed name, and signed-at date. When absent the PDF is returned unsigned so the customer can sign externally and upload it via the Documents API.
    """

    image_base64: Required[str]
    """PNG image, base64-encoded."""

    signer_name: Optional[str]
    """Optional.

    When absent the rendered PDF falls back to the enterprise contact's legal name.
    """
