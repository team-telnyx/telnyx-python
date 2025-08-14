# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ManagedAccountUpdateGlobalChannelLimitResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The user ID of the managed account."""

    channel_limit: Optional[int] = None
    """
    Integer value that indicates the number of allocatable global outbound channels
    that are allocated to the managed account. If the value is 0 then the account
    will have no usable channels and will not be able to perform outbound calling.
    """

    email: Optional[str] = None
    """The email of the managed account."""

    manager_account_id: Optional[str] = None
    """The user ID of the manager of the account."""

    record_type: Optional[str] = None
    """The name of the type of data in the response."""


class ManagedAccountUpdateGlobalChannelLimitResponse(BaseModel):
    data: Optional[Data] = None
