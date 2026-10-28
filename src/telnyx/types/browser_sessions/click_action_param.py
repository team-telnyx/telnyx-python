# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClickActionParam"]


class ClickActionParam(TypedDict, total=False):
    """Click an element identified by observation_id + ref."""

    observation_id: Required[str]

    ref: Required[str]

    type: Required[Literal["click"]]

    idempotency_key: str

    include_observation: bool

    timeout_ms: int

    wait: Literal["no_wait", "dom_stable", "url_change"]
