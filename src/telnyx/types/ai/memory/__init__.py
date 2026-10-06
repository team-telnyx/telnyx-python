# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .namespace_create_params import NamespaceCreateParams as NamespaceCreateParams

if TYPE_CHECKING:
    from .namespace import Namespace as Namespace
    from .namespace_list_response import NamespaceListResponse as NamespaceListResponse
    from .namespace_create_response import NamespaceCreateResponse as NamespaceCreateResponse
    from .namespace_retrieve_response import NamespaceRetrieveResponse as NamespaceRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "Namespace":
        from .namespace import Namespace

        return Namespace
    if name == "NamespaceCreateResponse":
        from .namespace_create_response import NamespaceCreateResponse

        return NamespaceCreateResponse
    if name == "NamespaceRetrieveResponse":
        from .namespace_retrieve_response import NamespaceRetrieveResponse

        return NamespaceRetrieveResponse
    if name == "NamespaceListResponse":
        from .namespace_list_response import NamespaceListResponse

        return NamespaceListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
