# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .filter_param import FilterParam as FilterParam
from .usage_report_retrieve_speech_to_text_params import (
    UsageReportRetrieveSpeechToTextParams as UsageReportRetrieveSpeechToTextParams,
)

if TYPE_CHECKING:
    from .filter import Filter as Filter
    from .usage_report_retrieve_speech_to_text_response import (
        UsageReportRetrieveSpeechToTextResponse as UsageReportRetrieveSpeechToTextResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "Filter":
        from .filter import Filter

        return Filter
    if name == "UsageReportRetrieveSpeechToTextResponse":
        from .usage_report_retrieve_speech_to_text_response import UsageReportRetrieveSpeechToTextResponse

        return UsageReportRetrieveSpeechToTextResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
