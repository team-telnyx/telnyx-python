# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentInputParam"]


class AgentInputParam(TypedDict, total=False):
    """Third-party reseller / partner managing the enterprise's phone numbers.

    Omit when the enterprise works directly with Telnyx.
    """

    administrative_area: Required[str]

    city: Required[str]

    contact_email: Required[str]

    contact_name: Required[str]

    contact_phone: Required[str]

    contact_title: Required[str]

    country: Required[str]

    legal_name: Required[str]

    postal_code: Required[str]

    street_address: Required[str]

    dba: Optional[str]

    extended_address: Optional[str]
