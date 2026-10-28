# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PressActionParam"]


class PressActionParam(TypedDict, total=False):
    """Press a keyboard key."""

    key: Required[
        Literal[
            "Enter",
            "Tab",
            "Escape",
            "Backspace",
            "ArrowUp",
            "ArrowDown",
            "ArrowLeft",
            "ArrowRight",
            "PageUp",
            "PageDown",
            "Home",
            "End",
        ]
    ]

    type: Required[Literal["press"]]

    idempotency_key: str

    include_observation: bool
