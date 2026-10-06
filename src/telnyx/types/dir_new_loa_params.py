# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DirNewLoaParams"]


class DirNewLoaParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """
    Telephone numbers to authorize on the DIR, in `+E164` format (`+` followed by
    10-15 digits). Max 15 per request.
    """

    agent: "AgentInputParam"
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    signature: "SignaturePayloadParam"
    """Optional.

    When provided the rendered PDF embeds the signature image, printed name, and
    signed-at date. When absent the PDF is returned unsigned so the customer can
    sign externally and upload it via the Documents API.
    """


from .signature_payload_param import SignaturePayloadParam
from .enterprises.reputation.agent_input_param import AgentInputParam
