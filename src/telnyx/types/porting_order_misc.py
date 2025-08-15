# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .porting_order_type import PortingOrderType

__all__ = ["PortingOrderMisc"]


class PortingOrderMisc(BaseModel):
    new_billing_phone_number: Optional[str] = None
    """New billing phone number for the remaining numbers.

    Used in case the current billing phone number is being ported to Telnyx. This
    will be set on your account with your current service provider and should be one
    of the numbers remaining on that account.
    """

    remaining_numbers_action: Optional[Literal["keep", "disconnect"]] = None
    """
    Remaining numbers can be either kept with their current service provider or
    disconnected. 'new_billing_telephone_number' is required when
    'remaining_numbers_action' is 'keep'.
    """

    type: Optional[PortingOrderType] = None
    """A port can be either 'full' or 'partial'.

    When type is 'full' the other attributes should be omitted.
    """
