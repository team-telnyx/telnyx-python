# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RequirementGroupCreateParams", "RegulatoryRequirement"]


class RequirementGroupCreateParams(TypedDict, total=False):
    action: Required[Literal["ordering", "porting"]]

    country_code: Required[str]
    """ISO alpha 2 country code"""

    phone_number_type: Required[Literal["local", "toll_free", "mobile", "national", "shared_cost"]]

    customer_reference: str

    regulatory_requirements: Iterable[RegulatoryRequirement]


class RegulatoryRequirement(TypedDict, total=False):
    field_value: str

    requirement_id: str
