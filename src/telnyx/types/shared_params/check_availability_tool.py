# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .check_availability_tool_params import CheckAvailabilityToolParams

__all__ = ["CheckAvailabilityTool"]


class CheckAvailabilityTool(TypedDict, total=False):
    check_availability: Required[CheckAvailabilityToolParams]

    type: Required[Literal["check_availability"]]
