# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .porting_order_type import PortingOrderType

__all__ = [
    "PortingOrderListParams",
    "Filter",
    "FilterActivationSettings",
    "FilterActivationSettingsFocDatetimeRequested",
    "FilterEndUser",
    "FilterEndUserAdmin",
    "FilterMisc",
    "FilterPhoneNumbers",
    "FilterPhoneNumbersPhoneNumber",
    "Page",
    "Sort",
]


class PortingOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference], filter[customer_group_reference],
    filter[parent_support_key], filter[phone_numbers.country_code],
    filter[phone_numbers.carrier_name], filter[misc.type],
    filter[end_user.admin.entity_name], filter[end_user.admin.auth_person_name],
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


class FilterActivationSettings(TypedDict, total=False):
    fast_port_eligible: bool
    """Filter results by fast port eligible"""

    foc_datetime_requested: FilterActivationSettingsFocDatetimeRequested
    """FOC datetime range filtering operations"""


class FilterEndUserAdmin(TypedDict, total=False):
    auth_person_name: str
    """Filter results by authorized person"""

    entity_name: str
    """Filter results by person or company name"""


class FilterEndUser(TypedDict, total=False):
    admin: FilterEndUserAdmin


class FilterMisc(TypedDict, total=False):
    type: PortingOrderType
    """Filter results by porting order type"""


class FilterPhoneNumbersPhoneNumber(TypedDict, total=False):
    contains: str
    """Filter results by full or partial phone_number"""


class FilterPhoneNumbers(TypedDict, total=False):
    carrier_name: str
    """Filter results by old service provider"""

    country_code: str
    """Filter results by country ISO 3166-1 alpha-2 code"""

    phone_number: FilterPhoneNumbersPhoneNumber
    """Phone number pattern filtering operations"""


class Filter(TypedDict, total=False):
    activation_settings: FilterActivationSettings

    customer_group_reference: str
    """Filter results by customer_group_reference"""

    customer_reference: str
    """Filter results by customer_reference"""

    end_user: FilterEndUser

    misc: FilterMisc

    parent_support_key: str
    """Filter results by parent_support_key"""

    phone_numbers: FilterPhoneNumbers


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
