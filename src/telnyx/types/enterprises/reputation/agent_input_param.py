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
    """
    The state or province of the partner's address, as its code, for example IL or
    ON.
    """

    city: Required[str]
    """The city of the partner's address."""

    contact_email: Required[str]
    """The email address of the contact person at the partner."""

    contact_name: Required[str]
    """The name of a contact person at the partner."""

    contact_phone: Required[str]
    """
    The phone number of the contact person at the partner, in E.164 format, for
    example +13125550000.
    """

    contact_title: Required[str]
    """The job title of the contact person at the partner."""

    country: Required[str]
    """The two-letter country code of the partner's address, for example US."""

    legal_name: Required[str]
    """
    The legal name of the third-party partner or reseller managing these numbers on
    your behalf.
    """

    postal_code: Required[str]
    """The postal or ZIP code of the partner's address."""

    street_address: Required[str]
    """
    The street address of the partner, including the building number and street
    name.
    """

    dba: Optional[str]
    """
    The trade name (Doing Business As) the partner operates under, if different from
    its legal name. Leave blank if it does not apply.
    """

    extended_address: Optional[str]
    """An optional second address line for the partner, such as a suite, unit, or
    floor.

    Leave blank if it does not apply.
    """
