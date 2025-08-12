# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ManagedAccountGetAllocatableGlobalOutboundChannelsResponse", "Data"]


class Data(BaseModel):
    allocatable_global_outbound_channels: Optional[int] = None
    """
    The total amount of allocatable global outbound channels available to the
    authenticated manager. Will be 0 if the feature is not enabled for their
    account.
    """

    managed_account_allow_custom_pricing: Optional[bool] = None
    """
    Boolean value that indicates if the managed account is able to have custom
    pricing set for it or not. If false, uses the pricing of the manager account.
    Defaults to false. This value may be changed, but there may be time lag between
    when the value is changed and pricing changes take effect.
    """

    record_type: Optional[str] = None
    """The type of the data contained in this record."""

    total_global_channels_allocated: Optional[int] = None
    """
    The total number of allocatable global outbound channels currently allocated
    across all managed accounts for the authenticated user. This includes any amount
    of channels allocated by default at managed account creation time. Will be 0 if
    the feature is not enabled for their account.
    """


class ManagedAccountGetAllocatableGlobalOutboundChannelsResponse(BaseModel):
    data: Optional[Data] = None
