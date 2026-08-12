# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .brand_contact import BrandContact
from .ein_brand_identifier import EinBrandIdentifier
from .capabilities_response import CapabilitiesResponse
from .stock_symbol_brand_identifier import StockSymbolBrandIdentifier

__all__ = ["BrandResponse", "Addresses", "Identifiers"]


class Addresses(BaseModel):
    administrative_area: str

    city: str

    country_code: str
    """The two-letter ISO 3166-1 country code."""

    line_1: str

    postal_code: str

    line_2: Optional[str] = None


Identifiers: TypeAlias = Union[EinBrandIdentifier, StockSymbolBrandIdentifier]


class BrandResponse(BaseModel):
    addresses: Dict[str, Addresses]

    brand_id: str

    capabilities: CapabilitiesResponse

    contacts: Dict[str, BrandContact]

    display_name: str

    identifiers: Dict[str, Identifiers]

    legal_entity_type: str

    legal_name: str

    organization_type: str

    profile_id: Optional[str] = None

    status: Literal["CREATED", "CONFIGURED", "SUBMITTED", "REVIEWING", "VETTING", "VERIFIED", "REJECTED", "FAILED"]

    website_url: str
