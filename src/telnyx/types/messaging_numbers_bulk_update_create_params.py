# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["MessagingNumbersBulkUpdateCreateParams"]


class MessagingNumbersBulkUpdateCreateParams(TypedDict, total=False):
    messaging_profile_id: Required[str]
    """Configure the messaging profile these phone numbers are assigned to:

    - Set this field to `""` to unassign each number from their respective messaging
      profile
    - Set this field to a quoted UUID of a messaging profile to assign these numbers
      to that messaging profile
    """

    numbers: Required[List[str]]
    """The list of phone numbers to update."""
