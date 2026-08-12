# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["WhatsappContactParam", "Address", "Email", "Org", "Phone", "URL"]


class Address(TypedDict, total=False):
    city: str

    country: str

    country_code: str

    state: str

    street: str

    type: str

    zip: str


class Email(TypedDict, total=False):
    email: str

    type: str


class Org(TypedDict, total=False):
    company: str

    department: str

    title: str


class Phone(TypedDict, total=False):
    phone: str

    type: str

    wa_id: str


class URL(TypedDict, total=False):
    type: str

    url: str


class WhatsappContactParam(TypedDict, total=False):
    addresses: Iterable[Address]

    birthday: str

    emails: Iterable[Email]

    name: str

    org: Org

    phones: Iterable[Phone]

    urls: Iterable[URL]
