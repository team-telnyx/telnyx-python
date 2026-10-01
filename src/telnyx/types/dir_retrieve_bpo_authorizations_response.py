# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .branded_calling_pagination_meta import BrandedCallingPaginationMeta

__all__ = ["DirRetrieveBpoAuthorizationsResponse", "Data"]


class Data(BaseModel):
    """A single authorization of a BPO (Business Process Outsourcer) account on a DIR."""

    bpo_enterprise_id: str
    """The authorized BPO account's enterprise id."""

    loa_document_id: str
    """Id of the signed Letter of Authorization document submitted for this BPO.

    Send it back unchanged in `bpo_authorizations` when updating the DIR to keep
    this authorization and its review state.
    """

    record_type: Literal["bpo_authorization"]
    """Always `bpo_authorization`."""

    status: Literal["pending", "approved", "rejected"]
    """Review state of this authorization.

    `pending` on create or when the Letter of Authorization is re-uploaded; an admin
    moves it to `approved` or `rejected`. Only an `approved` authorization adds the
    BPO to this DIR's authorized callers in the branded calling registry.
    """

    rejection_reason: Optional[str] = None
    """Why the authorization was rejected. `null` unless `status` is `rejected`."""


class DirRetrieveBpoAuthorizationsResponse(BaseModel):
    """Paginated list of a DIR's BPO authorizations."""

    data: List[Data]

    meta: BrandedCallingPaginationMeta
    """JSON:API pagination metadata returned with every paginated list response.

    Page numbering is 1-based. `page_size` reports the number of items actually
    returned in `data` for this page; the requested size is taken from the
    `page[size]` query parameter.
    """
