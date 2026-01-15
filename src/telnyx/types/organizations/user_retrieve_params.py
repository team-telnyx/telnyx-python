# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserRetrieveParams"]


class UserRetrieveParams(TypedDict, total=False):
    include_groups: bool
    """When set to true, includes the groups array for each user in the response.

    The groups array contains objects with id and name for each group the user
    belongs to.
    """
