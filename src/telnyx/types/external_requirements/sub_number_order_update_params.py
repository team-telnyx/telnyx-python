# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubNumberOrderUpdateParams", "Requirement"]


class SubNumberOrderUpdateParams(TypedDict, total=False):
    regulatory_requirement_id: Required[str]

    requirement: Required[Requirement]
    """The end user's identity details for the action requirement.

    Australia mobile ID verification is currently the only action requirement. It
    requires `first_name` and `last_name`, the same fields the corresponding GET
    lists in `fields_required`.
    """


class Requirement(TypedDict, total=False):
    """The end user's identity details for the action requirement.

    Australia mobile ID verification is currently the only action requirement. It requires `first_name` and `last_name`, the same fields the corresponding GET lists in `fields_required`.
    """

    first_name: Required[str]
    """The end user's first name."""

    last_name: Required[str]
    """The end user's last name."""
