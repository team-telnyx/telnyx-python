# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .update_regulatory_requirement_param import UpdateRegulatoryRequirementParam

__all__ = ["SubNumberOrderUpdateParams"]


class SubNumberOrderUpdateParams(TypedDict, total=False):
    regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam]
