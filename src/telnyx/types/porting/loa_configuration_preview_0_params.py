# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoaConfigurationPreview0Params", "Address", "Contact", "Logo"]


class LoaConfigurationPreview0Params(TypedDict, total=False):
    address: Required[Address]
    """The address of the company."""

    company_name: Required[str]
    """The name of the company"""

    contact: Required[Contact]
    """The contact information of the company."""

    logo: Required[Logo]
    """The logo of the LOA configuration"""

    name: Required[str]
    """The name of the LOA configuration"""


class Address(TypedDict, total=False):
    city: Required[str]
    """The locality of the company"""

    country_code: Required[str]
    """The country code of the company"""

    state: Required[str]
    """The administrative area of the company"""

    street_address: Required[str]
    """The street address of the company"""

    zip_code: Required[str]
    """The postal code of the company"""

    extended_address: str
    """The extended address of the company"""


class Contact(TypedDict, total=False):
    email: Required[str]
    """The email address of the contact"""

    phone_number: Required[str]
    """The phone number of the contact"""


class Logo(TypedDict, total=False):
    document_id: Required[str]
    """The document identification"""
