# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .usage_retrieve_summary_params import UsageRetrieveSummaryParams as UsageRetrieveSummaryParams

if TYPE_CHECKING:
    from .usage_retrieve_summary_response import UsageRetrieveSummaryResponse as UsageRetrieveSummaryResponse


def __getattr__(name: str) -> Any:
    if name == "UsageRetrieveSummaryResponse":
        from .usage_retrieve_summary_response import UsageRetrieveSummaryResponse

        return UsageRetrieveSummaryResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
