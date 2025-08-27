# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AdvancedOrderUpdateParams"]


class AdvancedOrderUpdateParams(TypedDict, total=False):
    area_code: str

    comments: str

    country_code: str

    customer_reference: str

    features: List[Literal["sms", "mms", "voice", "fax", "emergency"]]

    phone_number_type: Literal["local", "mobile", "toll_free", "shared_cost", "national", "landline"]

    quantity: int

    requirement_group_id: str
    """The ID of the requirement group to associate with this advanced order"""
