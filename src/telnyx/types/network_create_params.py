# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NetworkCreateParams"]


class NetworkCreateParams(TypedDict, total=False):
    network_create: Required["NetworkCreateParam"]


from .network_create_param import NetworkCreateParam
