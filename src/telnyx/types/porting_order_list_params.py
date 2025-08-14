# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .porting_order_type import PortingOrderType

__all__ = [
    "PortingOrderListParams",
    "Filter",
    "FilterActivationSettingsFocDatetimeRequested",
    "FilterPhoneNumbersPhoneNumber",
    "Page",
    "Sort",
]


class PortingOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference], filter[parent_support_key],
    filter[phone_numbers.country_code], filter[phone_numbers.carrier_name],
    filter[misc.type], filter[end_user.admin.entity_name],
    filter[end_user.admin.auth_person_name],
    filter[activation_settings.fast_port_eligible],
    filter[activation_settings.foc_datetime_requested][gt],
    filter[activation_settings.foc_datetime_requested][lt],
    filter[phone_numbers.phone_number][contains]
    """

    include_phone_numbers: bool
    """Include the first 50 phone number objects in the results"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class FilterActivationSettingsFocDatetimeRequested(TypedDict, total=False):
    gt: str
    """Filter results by foc date later than this value"""

    lt: str
    """Filter results by foc date earlier than this value"""


class FilterPhoneNumbersPhoneNumber(TypedDict, total=False):
    contains: str
    """Filter results by full or partial phone_number"""


class Filter(TypedDict, total=False):
    activation_settings_fast_port_eligible: Annotated[
        bool, PropertyInfo(alias="activation_settings.fast_port_eligible")
    ]
    """Filter results by fast port eligible"""

    activation_settings_foc_datetime_requested: Annotated[
        FilterActivationSettingsFocDatetimeRequested, PropertyInfo(alias="activation_settings.foc_datetime_requested")
    ]
    """FOC datetime range filtering operations"""

    customer_reference: str
    """Filter results by customer_reference"""

    end_user_admin_auth_person_name: Annotated[str, PropertyInfo(alias="end_user.admin.auth_person_name")]
    """Filter results by authorized person"""

    end_user_admin_entity_name: Annotated[str, PropertyInfo(alias="end_user.admin.entity_name")]
    """Filter results by person or company name"""

    misc_type: Annotated[PortingOrderType, PropertyInfo(alias="misc.type")]
    """Filter results by porting order type"""

    parent_support_key: str
    """Filter results by parent_support_key"""

    phone_numbers_carrier_name: Annotated[str, PropertyInfo(alias="phone_numbers.carrier_name")]
    """Filter results by old service provider"""

    phone_numbers_country_code: Annotated[str, PropertyInfo(alias="phone_numbers.country_code")]
    """Filter results by country ISO 3166-1 alpha-2 code"""

    phone_numbers_phone_number: Annotated[
        FilterPhoneNumbersPhoneNumber, PropertyInfo(alias="phone_numbers.phone_number")
    ]
    """Phone number filtering operations"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""


class Sort(TypedDict, total=False):
    value: Literal[
        "created_at",
        "-created_at",
        "activation_settings.foc_datetime_requested",
        "-activation_settings.foc_datetime_requested",
    ]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """
