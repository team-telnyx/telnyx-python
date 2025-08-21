# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["RequirementGroupUpdateParams", "RegulatoryRequirement"]


class RequirementGroupUpdateParams(TypedDict, total=False):
    customer_reference: str
    """Reference for the customer"""

    regulatory_requirements: Iterable[RegulatoryRequirement]


class RegulatoryRequirement(TypedDict, total=False):
    field_value: str
    """New value for the regulatory requirement"""

    requirement_id: str
    """Unique identifier for the regulatory requirement"""
