# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalConnectionUpdateLocationParams"]


class ExternalConnectionUpdateLocationParams(TypedDict, total=False):
    id: Required[str]

    static_emergency_address_id: Required[str]
    """A new static emergency address ID to update the location with"""
