# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessagingUpdateParams"]


class MessagingUpdateParams(TypedDict, total=False):
    messaging_product: str
    """Configure the messaging product for this number:

    - Omit this field or set its value to `null` to keep the current value.
    - Set this field to a quoted product ID to set this phone number to that product
    """

    messaging_profile_id: str
    """Configure the messaging profile this phone number is assigned to:

    - Omit this field or set its value to `null` to keep the current value.
    - Set this field to `""` to unassign the number from its messaging profile
    - Set this field to a quoted UUID of a messaging profile to assign this number
      to that messaging profile
    """
