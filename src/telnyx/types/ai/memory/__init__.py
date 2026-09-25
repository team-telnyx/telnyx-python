# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .namespace_retrieve_response import NamespaceRetrieveResponse as NamespaceRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "NamespaceRetrieveResponse":
        from .namespace_retrieve_response import NamespaceRetrieveResponse

        return NamespaceRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
