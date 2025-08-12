# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionRequirementInitiateParams", "Params"]


class ActionRequirementInitiateParams(TypedDict, total=False):
    porting_order_id: Required[str]

    params: Required[Params]
    """
    Required information for initiating the action requirement for AU ID
    verification.
    """


class Params(TypedDict, total=False):
    first_name: Required[str]
    """The first name of the person that will perform the verification flow."""

    last_name: Required[str]
    """The last name of the person that will perform the verification flow."""
