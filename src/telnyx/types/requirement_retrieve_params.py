# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RequirementRetrieveParams"]


class RequirementRetrieveParams(TypedDict, total=False):
    version: int
    """Filter by requirement version number.

    When omitted, returns the currently-active version.
    """
