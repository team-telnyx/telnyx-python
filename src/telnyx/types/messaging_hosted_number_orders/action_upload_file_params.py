# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import FileTypes

__all__ = ["ActionUploadFileParams"]


class ActionUploadFileParams(TypedDict, total=False):
    bill: FileTypes
    """
    Must be the last month's bill with proof of ownership of all of the numbers in
    the order in PDF format.
    """

    loa: FileTypes
    """Must be a signed LOA for the numbers in the order in PDF format."""
