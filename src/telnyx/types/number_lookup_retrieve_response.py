# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NumberLookupRetrieveResponse", "Data", "DataCallerName", "DataCarrier", "DataPortability"]


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

    line_type: Optional[str] = None
    """Type of number"""

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
    caller_name: Optional[DataCallerName] = None

    carrier: Optional[DataCarrier] = None

    country_code: Optional[str] = None
    """Region code that matches the specific country calling code"""

    fraud: Optional[str] = None
    """Unused"""

    national_format: Optional[str] = None
    """
    Hyphen-separated national number, preceded by the national destination code
    (NDC), with a 0 prefix, if an NDC is found
    """

    phone_number: Optional[str] = None
    """E164-formatted phone number"""

    portability: Optional[DataPortability] = None

    record_type: Optional[str] = None
    """Identifies the type of record"""


class NumberLookupRetrieveResponse(BaseModel):
    data: Optional[Data] = None
