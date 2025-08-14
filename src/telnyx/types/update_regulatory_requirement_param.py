# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UpdateRegulatoryRequirementParam"]


class UpdateRegulatoryRequirementParam(TypedDict, total=False):
    field_value: str
    """The value of the requirement.

    For address and document requirements, this should be the ID of the resource.
    For textual, this should be the value of the requirement.
    """

    requirement_id: str
    """Unique id for a requirement."""
