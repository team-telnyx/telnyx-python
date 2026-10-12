# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ExternalVerificationCreateParams"]


class ExternalVerificationCreateParams(TypedDict, total=False):
    document_ids: Required[SequenceNotStr[str]]
    """
    Ids of uploaded documents (Documents API) proving the enterprise owns its phone
    numbers hosted with another provider, for example a carrier invoice or account
    statement.
    """

    phone_numbers: SequenceNotStr[str]
    """Optional.

    The phone numbers hosted with another provider that the documents cover, in
    E.164 format. Shown to the reviewer to match the documents to your numbers; you
    can still add numbers that are not listed here, and each is checked on its own.
    """
