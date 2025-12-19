# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .global_ip_assignment_param import GlobalIPAssignmentParam

__all__ = ["GlobalIPAssignmentUpdateParams", "GlobalIPAssignmentUpdateRequest"]


class GlobalIPAssignmentUpdateParams(TypedDict, total=False):
    global_ip_assignment_update_request: Required[
        Annotated[GlobalIPAssignmentUpdateRequest, PropertyInfo(alias="globalIpAssignmentUpdateRequest")]
    ]


class GlobalIPAssignmentUpdateRequest(GlobalIPAssignmentParam, total=False):
    pass
