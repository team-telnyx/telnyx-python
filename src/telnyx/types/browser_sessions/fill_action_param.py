# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FillActionParam"]


class FillActionParam(TypedDict, total=False):
    """Type text into the element identified by observation_id + ref."""

    observation_id: Required[str]

    ref: Required[str]

    type: Required[Literal["fill"]]

    value: Required[str]

    idempotency_key: str

    include_observation: bool
