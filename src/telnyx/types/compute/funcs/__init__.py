# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .export_create_params import ExportCreateParams as ExportCreateParams

if TYPE_CHECKING:
    from .func_log_export_config_response import FuncLogExportConfigResponse as FuncLogExportConfigResponse


def __getattr__(name: str) -> Any:
    if name == "FuncLogExportConfigResponse":
        from .func_log_export_config_response import FuncLogExportConfigResponse

        return FuncLogExportConfigResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
