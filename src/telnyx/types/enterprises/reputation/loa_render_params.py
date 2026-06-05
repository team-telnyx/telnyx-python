# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LoaRenderParams", "Agent", "Signature"]


class LoaRenderParams(TypedDict, total=False):
    agent: Agent
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    signature: Signature
    """Optional signature embedded in the rendered PDF.

    When omitted the PDF is returned unsigned for the customer to sign and upload.
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
    """Optional signature embedded in the rendered PDF.

    When omitted the PDF is returned unsigned for the customer to sign and upload.
    """

    image_base64: Required[str]
    """Base64-encoded signature image."""

    signer_name: Optional[str]
