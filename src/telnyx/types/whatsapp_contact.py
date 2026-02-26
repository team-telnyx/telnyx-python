# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WhatsappContact", "Address", "Email", "Org", "Phone", "URL"]


class Address(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    country_code: Optional[str] = None

    state: Optional[str] = None

    street: Optional[str] = None

    type: Optional[str] = None

    zip: Optional[str] = None


class Email(BaseModel):
    email: Optional[str] = None

    type: Optional[str] = None


class Org(BaseModel):
    company: Optional[str] = None

    department: Optional[str] = None

    title: Optional[str] = None


class Phone(BaseModel):
    phone: Optional[str] = None

    type: Optional[str] = None

    wa_id: Optional[str] = None


class URL(BaseModel):
    type: Optional[str] = None

    url: Optional[str] = None


class WhatsappContact(BaseModel):
    addresses: Optional[List[Address]] = None

    birthday: Optional[str] = None

    emails: Optional[List[Email]] = None

    name: Optional[str] = None

    org: Optional[Org] = None

    phones: Optional[List[Phone]] = None

    urls: Optional[List[URL]] = None
