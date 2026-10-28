# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScreenshotActionParam"]


class ScreenshotActionParam(TypedDict, total=False):
    """Capture a screenshot of the current page."""

    type: Required[Literal["screenshot"]]

    idempotency_key: str

    include_observation: bool
