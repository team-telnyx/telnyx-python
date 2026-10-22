# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "NumberLookupRetrieveResponse",
    "Data",
    "DataCallerIdentity",
    "DataCallerIdentityAddress",
    "DataCallerName",
    "DataCarrier",
    "DataEnhancedCallerName",
    "DataNnidOverride",
    "DataPortability",
]


class DataCallerIdentityAddress(BaseModel):
    """Postal address associated with the phone number's owner."""

    city: Optional[str] = None
    """City."""

    country_code: Optional[str] = None
    """Two-letter ISO 3166-1 country code."""

    postal_code: Optional[str] = None
    """Postal or ZIP code."""

    state_code: Optional[str] = None
    """Two-letter state or province code."""

    street_line_1: Optional[str] = None
    """First line of the street address."""

    street_line_2: Optional[str] = None
    """Second line of the street address, if any."""

    zip4: Optional[str] = None
    """ZIP+4 extension, if available."""


class DataCallerIdentity(BaseModel):
    """
    Identity information for the phone number's owner, including name and postal address. Populated when `type=caller-identity` is requested.
    """

    address: Optional[DataCallerIdentityAddress] = None
    """Postal address associated with the phone number's owner."""

    confidence_score: Optional[float] = None
    """
    How strongly the phone number is linked to the returned name, on a scale of 50
    to 90 (higher means more supporting signals). Reflects signal strength, not
    probability: 70 indicates stronger, more consistent evidence than 60, not a 70%
    chance of being correct. As a guide, 70+ is high confidence, 60 moderate, and 50
    limited. Below 50 no name is returned, so scores under 50 are never present.
    """

    error_code: Optional[str] = None
    """
    A lookup-specific error code if the identity could not be resolved; otherwise
    null.
    """

    name: Optional[str] = None
    """The name associated with the phone number."""


class DataCallerName(BaseModel):
    caller_name: Optional[str] = None
    """The name of the requested phone number's owner as per the CNAM database"""

    error_code: Optional[str] = None
    """
    A caller-name lookup specific error code, expressed as a stringified 5-digit
    integer
    """


class DataCarrier(BaseModel):
    error_code: Optional[str] = None
    """Unused"""

    mobile_country_code: Optional[str] = None
    """
    Region code that matches the specific country calling code if the requested
    phone number type is mobile
    """

    mobile_network_code: Optional[str] = None
    """
    National destination code (NDC), with a 0 prefix, if an NDC is found and the
    requested phone number type is mobile
    """

    name: Optional[str] = None
    """
    SPID (Service Provider ID) name, if the requested phone number has been ported;
    otherwise, the name of carrier who owns the phone number block
    """

    normalized_carrier: Optional[str] = None
    """If known to Telnyx and applicable, the primary network carrier."""

    type: Optional[
        Literal[
            "fixed line",
            "mobile",
            "voip",
            "fixed line or mobile",
            "toll free",
            "premium rate",
            "shared cost",
            "personal number",
            "pager",
            "uan",
            "voicemail",
            "unknown",
        ]
    ] = None
    """
    A phone number type that identifies the type of service associated with the
    requested phone number
    """


class DataEnhancedCallerName(BaseModel):
    """Enhanced caller name for the phone number's owner.

    Populated when `type=enhanced-caller-name` is requested.
    """

    caller_name: Optional[str] = None
    """The name associated with the phone number."""

    error_code: Optional[str] = None
    """
    A lookup-specific error code if the enhanced caller name could not be resolved;
    otherwise null.
    """


class DataNnidOverride(BaseModel):
    """
    Network number ID (NNID) override for the phone number, when one applies (available only to accounts enabled for NNID); otherwise null.
    """

    name: Optional[str] = None
    """Name associated with the NNID."""

    nnid: Optional[str] = None
    """The network number ID."""

    type: Optional[str] = None
    """The NNID type."""


class DataPortability(BaseModel):
    altspid: Optional[str] = None
    """Alternative SPID (Service Provider ID).

    Often used when a carrier is using a number from another carrier
    """

    altspid_carrier_name: Optional[str] = None
    """Alternative service provider name"""

    altspid_carrier_type: Optional[str] = None
    """Alternative service provider type"""

    city: Optional[str] = None
    """
    City name extracted from the locality in the Local Exchange Routing Guide (LERG)
    database
    """

    line_type: Optional[
        Literal[
            "fixed line",
            "mobile",
            "voip",
            "fixed line or mobile",
            "toll free",
            "premium rate",
            "shared cost",
            "personal number",
            "pager",
            "uan",
            "voicemail",
            "unknown",
        ]
    ] = None
    """The line type of the phone number.

    Uses the same value set as carrier.type; see the API reference for the full
    list.
    """

    lrn: Optional[str] = None
    """Local Routing Number, if assigned to the requested phone number"""

    ocn: Optional[str] = None
    """
    Operating Company Name (OCN) as per the Local Exchange Routing Guide (LERG)
    database
    """

    ported_date: Optional[str] = None
    """ISO-formatted date when the requested phone number has been ported"""

    ported_status: Optional[Literal["Y", "N", ""]] = None
    """Indicates whether or not the requested phone number has been ported"""

    spid: Optional[str] = None
    """SPID (Service Provider ID)"""

    spid_carrier_name: Optional[str] = None
    """Service provider name"""

    spid_carrier_type: Optional[str] = None
    """Service provider type"""

    state: Optional[str] = None


class Data(BaseModel):
    caller_identity: Optional[DataCallerIdentity] = None
    """
    Identity information for the phone number's owner, including name and postal
    address. Populated when `type=caller-identity` is requested.
    """

    caller_name: Optional[DataCallerName] = None

    carrier: Optional[DataCarrier] = None

    country_code: Optional[str] = None
    """Region code that matches the specific country calling code"""

    enhanced_caller_name: Optional[DataEnhancedCallerName] = None
    """Enhanced caller name for the phone number's owner.

    Populated when `type=enhanced-caller-name` is requested.
    """

    fraud: Optional[str] = None
    """Unused"""

    national_format: Optional[str] = None
    """
    Hyphen-separated national number, preceded by the national destination code
    (NDC), with a 0 prefix, if an NDC is found
    """

    nnid_override: Optional[DataNnidOverride] = None
    """
    Network number ID (NNID) override for the phone number, when one applies
    (available only to accounts enabled for NNID); otherwise null.
    """

    phone_number: Optional[str] = None
    """E164-formatted phone number"""

    portability: Optional[DataPortability] = None

    record_type: Optional[str] = None
    """Identifies the type of record"""

    valid_number: Optional[bool] = None
    """Indicates whether the phone number is valid."""


class NumberLookupRetrieveResponse(BaseModel):
    data: Optional[Data] = None
