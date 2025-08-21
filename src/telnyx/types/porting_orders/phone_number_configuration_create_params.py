# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberConfigurationCreateParams", "PhoneNumberConfiguration"]


class PhoneNumberConfigurationCreateParams(TypedDict, total=False):
    phone_number_configurations: Iterable[PhoneNumberConfiguration]


class PhoneNumberConfiguration(TypedDict, total=False):
    porting_phone_number_id: Required[str]
    """Identifies the porting phone number to be configured."""

    user_bundle_id: Required[str]
    """Identifies the user bundle to be associated with the porting phone number."""
