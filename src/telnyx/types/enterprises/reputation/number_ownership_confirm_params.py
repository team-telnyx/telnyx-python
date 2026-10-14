# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NumberOwnershipConfirmParams"]


class NumberOwnershipConfirmParams(TypedDict, total=False):
    enterprise_id: Required[str]

    still_own: Required[bool]
    """`true` confirms you still own the number.

    `false` reports that you no longer own it and removes it from Number Reputation.
    """

    evidence_document_id: str
    """Optional id of an uploaded document supporting the confirmation."""
