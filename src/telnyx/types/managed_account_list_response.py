# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["ManagedAccountListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Uniquely identifies the managed account."""

    api_user: str
    """The manager account's email, which serves as the V1 API user identifier"""

    created_at: str
    """ISO 8601 formatted date indicating when the resource was created."""

    email: str
    """The managed account's email."""

    manager_account_id: str
    """The ID of the manager account associated with the managed account."""

    record_type: Literal["managed_account"]
    """Identifies the type of the resource."""

    updated_at: str
    """ISO 8601 formatted date indicating when the resource was updated."""

    managed_account_allow_custom_pricing: Optional[bool] = None
    """
    Boolean value that indicates if the managed account is able to have custom
    pricing set for it or not. If false, uses the pricing of the manager account.
    Defaults to false. There may be time lag between when the value is changed and
    pricing changes take effect.
    """

    organization_name: Optional[str] = None
    """The organization the managed account is associated with."""

    rollup_billing: Optional[bool] = None
    """
    Boolean value that indicates if the billing information and charges to the
    managed account "roll up" to the manager account. If true, the managed account
    will not have its own balance and will use the shared balance with the manager
    account. This value cannot be changed after account creation without going
    through Telnyx support as changes require manual updates to the account ledger.
    Defaults to false.
    """


class ManagedAccountListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
