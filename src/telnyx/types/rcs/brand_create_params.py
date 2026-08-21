# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .brand_address_param import BrandAddressParam
from .brand_contact_param import BrandContactParam
from .brand_identifier_param import BrandIdentifierParam
from .brand_legal_entity_type import BrandLegalEntityType
from .brand_organization_type import BrandOrganizationType
from .ein_brand_identifier_param import EinBrandIdentifierParam
from .stock_symbol_brand_identifier_param import StockSymbolBrandIdentifierParam

__all__ = ["BrandCreateParams", "Contacts", "ContactsBrand", "Identifiers"]


class BrandCreateParams(TypedDict, total=False):
    addresses: Required[Dict[str, BrandAddressParam]]

    contacts: Required[Contacts]
    """Named business contacts. Use the `brand` key for the required BRAND contact."""

    display_name: Required[str]

    identifiers: Required[Identifiers]
    """Named business identifiers.

    Use the `ein` key for the required EIN and `stock_symbol` for a public-profit
    brand's stock symbol.
    """

    legal_entity_type: Required[BrandLegalEntityType]

    legal_name: Required[str]

    organization_type: Required[BrandOrganizationType]

    website_url: Required[str]

    profile_id: Optional[str]
    """A Messaging Profile owned by the authenticated organization.

    Agents inherit this value when they do not provide their own profile.
    """


class ContactsBrand(BrandContactParam, total=False):
    contact_type: Literal["BRAND"]  # type: ignore


class Contacts(TypedDict, total=False, extra_items=BrandContactParam):  # type: ignore[call-arg]
    """Named business contacts. Use the `brand` key for the required BRAND contact."""

    brand: Required[ContactsBrand]


class Identifiers(TypedDict, total=False, extra_items=BrandIdentifierParam):  # type: ignore[call-arg]
    """Named business identifiers.

    Use the `ein` key for the required EIN and `stock_symbol` for a public-profit brand's stock symbol.
    """

    ein: Required[EinBrandIdentifierParam]

    stock_symbol: StockSymbolBrandIdentifierParam
