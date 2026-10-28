# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScrollActionParam"]


class ScrollActionParam(TypedDict, total=False):
    """Scroll the page."""

    type: Required[Literal["scroll"]]

    delta_x: int

    delta_y: int

    idempotency_key: str

    include_observation: bool
