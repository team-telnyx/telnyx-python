# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ObserveActionParam"]


class ObserveActionParam(TypedDict, total=False):
    """Capture an observation (DOM snapshot) of the current page."""

    type: Required[Literal["observe"]]

    idempotency_key: str

    include_observation: bool
