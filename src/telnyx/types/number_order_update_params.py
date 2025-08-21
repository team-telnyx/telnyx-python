# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .update_regulatory_requirement_param import UpdateRegulatoryRequirementParam

__all__ = ["NumberOrderUpdateParams"]


class NumberOrderUpdateParams(TypedDict, total=False):
    customer_reference: str
    """A customer reference string for customer look ups."""

    regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam]
