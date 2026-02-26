# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WhatsappLocationParam"]


class WhatsappLocationParam(TypedDict, total=False):
    address: str

    latitude: str

    longitude: str

    name: str
