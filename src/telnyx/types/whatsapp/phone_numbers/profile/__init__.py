# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .photo_upload_params import PhotoUploadParams as PhotoUploadParams

if TYPE_CHECKING:
    from .photo_upload_response import PhotoUploadResponse as PhotoUploadResponse
    from .photo_retrieve_response import PhotoRetrieveResponse as PhotoRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "PhotoRetrieveResponse":
        from .photo_retrieve_response import PhotoRetrieveResponse

        return PhotoRetrieveResponse
    if name == "PhotoUploadResponse":
        from .photo_upload_response import PhotoUploadResponse

        return PhotoUploadResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
