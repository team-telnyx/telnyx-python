# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .brand_contact_param import BrandContactParam
from .brand_legal_entity_type import BrandLegalEntityType
from .brand_organization_type import BrandOrganizationType
from .ein_brand_identifier_param import EinBrandIdentifierParam
from .stock_symbol_brand_identifier_param import StockSymbolBrandIdentifierParam

__all__ = ["BrandUpdateParams", "Addresses", "Contacts", "ContactsBrand", "Identifiers", "Identifier"]


class BrandUpdateParams(TypedDict, total=False):
    addresses: Dict[str, Addresses]

    contacts: Contacts
    """Named business contacts. Use the `brand` key for the required BRAND contact."""

    display_name: str

    identifiers: Identifiers
    """Named business identifiers.

    Use the `ein` key for the required EIN and `stock_symbol` for a public-profit
    brand's stock symbol.
    """

    legal_entity_type: BrandLegalEntityType

    legal_name: str

    organization_type: BrandOrganizationType

    profile_id: str

    website_url: str


class Addresses(TypedDict, total=False):
    administrative_area: Required[str]

    city: Required[str]

    country_code: Required[str]
    """The two-letter ISO 3166-1 country code."""

    line_1: Required[str]

    postal_code: Required[str]

    line_2: Optional[str]


class ContactsBrand(BrandContactParam, total=False):
    contact_type: Literal["BRAND"]  # type: ignore


class Contacts(TypedDict, total=False, extra_items=BrandContactParam):  # type: ignore[call-arg]
    """Named business contacts. Use the `brand` key for the required BRAND contact."""

    brand: Required[ContactsBrand]


Identifier: TypeAlias = Union[EinBrandIdentifierParam, StockSymbolBrandIdentifierParam]


class Identifiers(TypedDict, total=False, extra_items=Identifier):  # type: ignore[call-arg]
    """Named business identifiers.

    Use the `ein` key for the required EIN and `stock_symbol` for a public-profit brand's stock symbol.
    """

    ein: Required[EinBrandIdentifierParam]

    stock_symbol: StockSymbolBrandIdentifierParam
