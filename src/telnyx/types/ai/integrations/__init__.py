# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .integration_connection import IntegrationConnection as IntegrationConnection
    from .connection_list_response import ConnectionListResponse as ConnectionListResponse
    from .connection_retrieve_response import ConnectionRetrieveResponse as ConnectionRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "IntegrationConnection":
        from .integration_connection import IntegrationConnection

        return IntegrationConnection
    if name == "ConnectionRetrieveResponse":
        from .connection_retrieve_response import ConnectionRetrieveResponse

        return ConnectionRetrieveResponse
    if name == "ConnectionListResponse":
        from .connection_list_response import ConnectionListResponse

        return ConnectionListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
