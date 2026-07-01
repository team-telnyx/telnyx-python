# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .default_gateway import DefaultGateway as DefaultGateway
from .default_gateway_create_params import DefaultGatewayCreateParams as DefaultGatewayCreateParams

if TYPE_CHECKING:
    from .default_gateway_create_response import DefaultGatewayCreateResponse as DefaultGatewayCreateResponse
    from .default_gateway_delete_response import DefaultGatewayDeleteResponse as DefaultGatewayDeleteResponse
    from .default_gateway_retrieve_response import DefaultGatewayRetrieveResponse as DefaultGatewayRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "DefaultGatewayCreateResponse":
        from .default_gateway_create_response import DefaultGatewayCreateResponse

        return DefaultGatewayCreateResponse
    if name == "DefaultGatewayRetrieveResponse":
        from .default_gateway_retrieve_response import DefaultGatewayRetrieveResponse

        return DefaultGatewayRetrieveResponse
    if name == "DefaultGatewayDeleteResponse":
        from .default_gateway_delete_response import DefaultGatewayDeleteResponse

        return DefaultGatewayDeleteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
