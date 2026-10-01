# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .signature_payload_param import SignaturePayloadParam

__all__ = ["DirBpoLoaParams"]


class DirBpoLoaParams(TypedDict, total=False):
    bpo_enterprise_id: Required[str]
    """The approved BPO enterprise the Brand Owner is authorizing.

    Must be a BPO account on the caller's organization that has already been
    approved.
    """

    signature: SignaturePayloadParam
    """Optional.

    When provided the rendered PDF embeds the signature image, printed name, and
    signed-at date. When absent the PDF is returned unsigned so the Brand Owner can
    sign externally and the BPO can upload it via the Documents API.
    """
