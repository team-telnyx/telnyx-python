# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .account_retrieve_recordings_json_params import (
    AccountRetrieveRecordingsJsonParams as AccountRetrieveRecordingsJsonParams,
)
from .account_retrieve_transcriptions_json_params import (
    AccountRetrieveTranscriptionsJsonParams as AccountRetrieveTranscriptionsJsonParams,
)

if TYPE_CHECKING:
    from .texml_recording_subresources_uris import TexmlRecordingSubresourcesUris as TexmlRecordingSubresourcesUris
    from .texml_get_call_recording_response_body import (
        TexmlGetCallRecordingResponseBody as TexmlGetCallRecordingResponseBody,
    )
    from .account_retrieve_transcriptions_json_response import (
        AccountRetrieveTranscriptionsJsonResponse as AccountRetrieveTranscriptionsJsonResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "TexmlGetCallRecordingResponseBody":
        from .texml_get_call_recording_response_body import TexmlGetCallRecordingResponseBody

        return TexmlGetCallRecordingResponseBody
    if name == "TexmlRecordingSubresourcesUris":
        from .texml_recording_subresources_uris import TexmlRecordingSubresourcesUris

        return TexmlRecordingSubresourcesUris
    if name == "AccountRetrieveTranscriptionsJsonResponse":
        from .account_retrieve_transcriptions_json_response import AccountRetrieveTranscriptionsJsonResponse

        return AccountRetrieveTranscriptionsJsonResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
