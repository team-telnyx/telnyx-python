# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List

from ...._models import BaseModel
from .reputation_phone_number import ReputationPhoneNumber

if TYPE_CHECKING:
    from ...number_reputation_pagination_meta import NumberReputationPaginationMeta

__all__ = ["ReputationPhoneNumberList"]


class ReputationPhoneNumberList(BaseModel):
    data: List[ReputationPhoneNumber]

    meta: NumberReputationPaginationMeta
    """JSON:API pagination metadata returned with every paginated list response.

    Page numbering is 1-based. `page_size` reports the number of items actually
    returned in `data` for this page; the requested size is taken from the
    `page[size]` query parameter.
    """
