# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .import_create_params import ImportCreateParams as ImportCreateParams

if TYPE_CHECKING:
    from .email_block_import_response import EmailBlockImportResponse as EmailBlockImportResponse


def __getattr__(name: str) -> Any:
    if name == "EmailBlockImportResponse":
        from .email_block_import_response import EmailBlockImportResponse

        return EmailBlockImportResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
