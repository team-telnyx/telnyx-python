# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SignaturePayloadParam"]


class SignaturePayloadParam(TypedDict, total=False):
    image_base64: Required[str]
    """PNG image, base64-encoded."""

    signer_name: Optional[str]
    """Optional.

    When absent the rendered PDF falls back to the enterprise contact's legal name.
    """
