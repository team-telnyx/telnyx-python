# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .public_internet_gateway_param import PublicInternetGatewayParam

__all__ = ["PublicInternetGatewayCreateParams", "Body"]


class PublicInternetGatewayCreateParams(TypedDict, total=False):
    body: Required[Body]


class Body(PublicInternetGatewayParam, total=False):
    pass
