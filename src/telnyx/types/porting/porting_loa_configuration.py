# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingLoaConfiguration", "Address", "Contact", "Logo"]


class Address(BaseModel):
    city: Optional[str] = None
    """The locality of the company"""

    country_code: Optional[str] = None
    """The country code of the company"""

    extended_address: Optional[str] = None
    """The extended address of the company"""

    state: Optional[str] = None
    """The administrative area of the company"""

    street_address: Optional[str] = None
    """The street address of the company"""

    zip_code: Optional[str] = None
    """The postal code of the company"""


class Contact(BaseModel):
    email: Optional[str] = None
    """The email address of the contact"""

    phone_number: Optional[str] = None
    """The phone number of the contact"""


class Logo(BaseModel):
    content_type: Optional[Literal["image/png"]] = None
    """The content type of the logo."""

    document_id: Optional[str] = None
    """Identifies the document that contains the logo."""


class PortingLoaConfiguration(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the LOA configuration."""

    address: Optional[Address] = None
    """The address of the company."""

    company_name: Optional[str] = None
    """The name of the company"""

    contact: Optional[Contact] = None
    """The contact information of the company."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    logo: Optional[Logo] = None
    """The logo to be used in the LOA."""

    name: Optional[str] = None
    """The name of the LOA configuration"""

    organization_id: Optional[str] = None
    """The organization that owns the LOA configuration"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
