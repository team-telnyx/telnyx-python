# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    billing_group_id: str
    """Identifies the billing group associated with the phone number."""

    connection_id: str
    """Identifies the connection associated with the phone number."""

    customer_reference: str
    """A customer reference string for customer look ups."""

    external_pin: str
    """
    If someone attempts to port your phone number away from Telnyx and your phone
    number has an external PIN set, we will attempt to verify that you provided the
    correct external PIN to the winning carrier. Note that not all carriers
    cooperate with this security mechanism.
    """

    hd_voice_enabled: bool
    """Indicates whether HD voice is enabled for this number."""

    tags: List[str]
    """A list of user-assigned tags to help organize phone numbers."""
