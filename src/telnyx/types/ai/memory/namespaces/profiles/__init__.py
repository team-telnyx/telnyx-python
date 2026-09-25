# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .memory_list_params import MemoryListParams as MemoryListParams
from .source_list_params import SourceListParams as SourceListParams

if TYPE_CHECKING:
    from .memory_list_response import MemoryListResponse as MemoryListResponse
    from .source_delete_response import SourceDeleteResponse as SourceDeleteResponse
    from .memory_retrieve_response import MemoryRetrieveResponse as MemoryRetrieveResponse
    from .source_retrieve_response import SourceRetrieveResponse as SourceRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "MemoryRetrieveResponse":
        from .memory_retrieve_response import MemoryRetrieveResponse

        return MemoryRetrieveResponse
    if name == "MemoryListResponse":
        from .memory_list_response import MemoryListResponse

        return MemoryListResponse
    if name == "SourceRetrieveResponse":
        from .source_retrieve_response import SourceRetrieveResponse

        return SourceRetrieveResponse
    if name == "SourceDeleteResponse":
        from .source_delete_response import SourceDeleteResponse

        return SourceDeleteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
