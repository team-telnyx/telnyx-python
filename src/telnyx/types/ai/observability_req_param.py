# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ObservabilityReqParam"]


class ObservabilityReqParam(TypedDict, total=False):
    host: str

    public_key_ref: str

    secret_key_ref: str

    status: Literal["enabled", "disabled"]
