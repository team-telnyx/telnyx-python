# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandContactParam"]


class BrandContactParam(TypedDict, total=False):
    contact_type: Required[Literal["BRAND", "PRIMARY", "OFFICER", "AGENT", "RESPONSIBLE_PARTY", "BILLING", "UNKNOWN"]]

    email: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    phone_number: Required[str]

    title: Optional[str]
