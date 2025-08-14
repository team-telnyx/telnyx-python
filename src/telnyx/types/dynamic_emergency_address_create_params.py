# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DynamicEmergencyAddressCreateParams"]


class DynamicEmergencyAddressCreateParams(TypedDict, total=False):
    administrative_area: Required[str]

    country_code: Required[Literal["US", "CA", "PR"]]

    house_number: Required[str]

    locality: Required[str]

    postal_code: Required[str]

    street_name: Required[str]

    extended_address: str

    house_suffix: str

    street_post_directional: str

    street_pre_directional: str

    street_suffix: str
