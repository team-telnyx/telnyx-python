# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .vertical import Vertical
from .entity_type import EntityType
from .stock_exchange import StockExchange

__all__ = ["BrandCreateParams"]


class BrandCreateParams(TypedDict, total=False):
    country: Required[str]
    """ISO2 2 characters country code. Example: US - United States"""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """Display name, marketing name, or DBA name of the brand."""

    email: Required[str]
    """Valid email address of brand support contact."""

    entity_type: Required[Annotated[EntityType, PropertyInfo(alias="entityType")]]
    """Entity type behind the brand. This is the form of business establishment."""

    vertical: Required[Vertical]
    """Vertical or industry segment of the brand or campaign."""

    business_contact_email: Annotated[str, PropertyInfo(alias="businessContactEmail")]
    """Business contact email.

    Required if `entityType` is `PUBLIC_PROFIT`.
    """

    city: str
    """City name"""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """(Required for Non-profit/private/public) Legal company name."""

    ein: str
    """(Required for Non-profit) Government assigned corporate tax ID.

    EIN is 9-digits in U.S.
    """

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of business contact."""

    ip_address: Annotated[str, PropertyInfo(alias="ipAddress")]
    """IP address of the browser requesting to create brand identity."""

    is_reseller: Annotated[bool, PropertyInfo(alias="isReseller")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of business contact."""

    mobile_phone: Annotated[str, PropertyInfo(alias="mobilePhone")]
    """Valid mobile phone number in e.164 international format."""

    mock: bool
    """Mock brand for testing purposes. Defaults to false."""

    phone: str
    """Valid phone number in e.164 international format."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """Postal codes. Use 5 digit zipcode for United States"""

    state: str
    """State. Must be 2 letters code for United States."""

    stock_exchange: Annotated[StockExchange, PropertyInfo(alias="stockExchange")]
    """(Required for public company) stock exchange."""

    stock_symbol: Annotated[str, PropertyInfo(alias="stockSymbol")]
    """(Required for public company) stock symbol."""

    street: str
    """Street number and name."""

    webhook_failover_url: Annotated[str, PropertyInfo(alias="webhookFailoverURL")]
    """Webhook failover URL for brand status updates."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookURL")]
    """Webhook URL for brand status updates."""

    website: str
    """Brand website URL."""
