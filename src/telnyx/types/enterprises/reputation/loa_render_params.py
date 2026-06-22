# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .agent_input_param import AgentInputParam

__all__ = ["LoaRenderParams", "Signature"]


class LoaRenderParams(TypedDict, total=False):
    agent: AgentInputParam
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    signature: Signature
    """Optional signature embedded in the rendered PDF.

    When omitted the PDF is returned unsigned for the customer to sign and upload.
    """


class Signature(TypedDict, total=False):
    """Optional signature embedded in the rendered PDF.

    When omitted the PDF is returned unsigned for the customer to sign and upload.
    """

    image_base64: Required[str]
    """Base64-encoded signature image."""

    signer_name: Optional[str]
