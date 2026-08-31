# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .collection_retrieve_documents_params import CollectionRetrieveDocumentsParams as CollectionRetrieveDocumentsParams

if TYPE_CHECKING:
    from .collection_retrieve_documents_response import (
        CollectionRetrieveDocumentsResponse as CollectionRetrieveDocumentsResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "CollectionRetrieveDocumentsResponse":
        from .collection_retrieve_documents_response import CollectionRetrieveDocumentsResponse

        return CollectionRetrieveDocumentsResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
