# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoaUpdateParams"]


class LoaUpdateParams(TypedDict, total=False):
    loa_document_id: Required[str]
    """Id of the new signed LOA document (from the Telnyx Documents API).

    Changing it resets LOA approval; the new document must be approved before more
    numbers can be added.
    """
