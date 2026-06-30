# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .recording_source import RecordingSource as RecordingSource
from .twiml_recording_channels import TwimlRecordingChannels as TwimlRecordingChannels
from .siprec_siprec_sid_json_params import SiprecSiprecSidJsonParams as SiprecSiprecSidJsonParams
from .stream_streaming_sid_json_params import StreamStreamingSidJsonParams as StreamStreamingSidJsonParams
from .recording_recording_sid_json_params import RecordingRecordingSidJsonParams as RecordingRecordingSidJsonParams
from .recordings_json_recordings_json_params import (
    RecordingsJsonRecordingsJsonParams as RecordingsJsonRecordingsJsonParams,
)

if TYPE_CHECKING:
    from .siprec_siprec_sid_json_response import SiprecSiprecSidJsonResponse as SiprecSiprecSidJsonResponse
    from .stream_streaming_sid_json_response import StreamStreamingSidJsonResponse as StreamStreamingSidJsonResponse
    from .texml_get_call_recordings_response_body import (
        TexmlGetCallRecordingsResponseBody as TexmlGetCallRecordingsResponseBody,
    )
    from .texml_create_call_recording_response_body import (
        TexmlCreateCallRecordingResponseBody as TexmlCreateCallRecordingResponseBody,
    )


def __getattr__(name: str) -> Any:
    if name == "TexmlCreateCallRecordingResponseBody":
        from .texml_create_call_recording_response_body import TexmlCreateCallRecordingResponseBody

        return TexmlCreateCallRecordingResponseBody
    if name == "TexmlGetCallRecordingsResponseBody":
        from .texml_get_call_recordings_response_body import TexmlGetCallRecordingsResponseBody

        return TexmlGetCallRecordingsResponseBody
    if name == "SiprecSiprecSidJsonResponse":
        from .siprec_siprec_sid_json_response import SiprecSiprecSidJsonResponse

        return SiprecSiprecSidJsonResponse
    if name == "StreamStreamingSidJsonResponse":
        from .stream_streaming_sid_json_response import StreamStreamingSidJsonResponse

        return StreamStreamingSidJsonResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
