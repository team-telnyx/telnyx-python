# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .enterprises.reputation.agent_input_param import AgentInputParam

__all__ = ["DirNewLoaParams", "Signature"]


class DirNewLoaParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """
    Telephone numbers to authorize on the DIR, in `+E164` format (`+` followed by
    10-15 digits). Max 15 per request.
    """

    agent: AgentInputParam
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    signature: Signature
    """Optional.

    When provided the rendered PDF embeds the signature image, printed name, and
    signed-at date. When absent the PDF is returned unsigned so the customer can
    sign externally and upload it via the Documents API.
    """


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
