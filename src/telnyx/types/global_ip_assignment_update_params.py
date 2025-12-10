# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .global_ip_assignment_param import GlobalIPAssignmentParam

__all__ = ["GlobalIPAssignmentUpdateParams", "Body"]


class GlobalIPAssignmentUpdateParams(TypedDict, total=False):
    body: Required[Body]


class Body(GlobalIPAssignmentParam, total=False):
    pass
