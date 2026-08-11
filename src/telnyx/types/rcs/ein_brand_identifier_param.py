# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EinBrandIdentifierParam"]


class EinBrandIdentifierParam(TypedDict, total=False):
    identifier_type: Required[Literal["EIN"]]

    value: Required[str]
    """Nine digits, optionally formatted as NN-NNNNNNN."""
