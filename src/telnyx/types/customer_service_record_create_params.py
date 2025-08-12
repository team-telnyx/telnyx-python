# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomerServiceRecordCreateParams", "AdditionalData"]


class CustomerServiceRecordCreateParams(TypedDict, total=False):
    phone_number: Required[str]
    """A valid US phone number in E164 format."""

    additional_data: AdditionalData

    webhook_url: str
    """Callback URL to receive webhook notifications."""


class AdditionalData(TypedDict, total=False):
    account_number: str
    """The account number of the customer service record."""

    address_line_1: str
    """The first line of the address of the customer service record."""

    authorized_person_name: str
    """The name of the authorized person."""

    billing_phone_number: str
    """The billing phone number of the customer service record."""

    city: str
    """The city of the customer service record."""

    customer_code: str
    """The customer code of the customer service record."""

    name: str
    """The name of the administrator of CSR."""

    pin: str
    """The PIN of the customer service record."""

    state: str
    """The state of the customer service record."""

    zip_code: str
    """The zip code of the customer service record."""
