# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..document_param import DocumentParam

__all__ = ["PhoneNumberAddParams"]


class PhoneNumberAddParams(TypedDict, total=False):
    documents: Required[Iterable[DocumentParam]]
    """Supporting documents covering this batch.

    At least one entry with `document_type: letter_of_authorization` is required -
    the LOA authorises Telnyx to register these numbers under the DIR. Each
    `document_id` must come from the Telnyx Documents API. Additional document types
    (e.g. business registration) may be included alongside the LOA.
    """

    phone_numbers: Required[SequenceNotStr[str]]
    """1–15 phone numbers in E.164 format.

    10-digit US numbers are auto-prefixed with `1`.
    """
