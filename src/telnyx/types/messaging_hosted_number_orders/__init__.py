# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_upload_file_params import ActionUploadFileParams as ActionUploadFileParams

if TYPE_CHECKING:
    from .action_upload_file_response import ActionUploadFileResponse as ActionUploadFileResponse


def __getattr__(name: str) -> Any:
    if name == "ActionUploadFileResponse":
        from .action_upload_file_response import ActionUploadFileResponse

        return ActionUploadFileResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
