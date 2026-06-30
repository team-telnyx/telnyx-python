# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .call_calls_params import CallCallsParams as CallCallsParams
from .queue_list_params import QueueListParams as QueueListParams
from .call_update_params import CallUpdateParams as CallUpdateParams
from .queue_create_params import QueueCreateParams as QueueCreateParams
from .queue_update_params import QueueUpdateParams as QueueUpdateParams
from .call_siprec_json_params import CallSiprecJsonParams as CallSiprecJsonParams
from .call_streams_json_params import CallStreamsJsonParams as CallStreamsJsonParams
from .conference_update_params import ConferenceUpdateParams as ConferenceUpdateParams
from .call_retrieve_calls_params import CallRetrieveCallsParams as CallRetrieveCallsParams
from .conference_retrieve_conferences_params import (
    ConferenceRetrieveConferencesParams as ConferenceRetrieveConferencesParams,
)

if TYPE_CHECKING:
    from .call_resource import CallResource as CallResource
    from .queue_resource import QueueResource as QueueResource
    from .call_calls_response import CallCallsResponse as CallCallsResponse
    from .conference_resource import ConferenceResource as ConferenceResource
    from .call_siprec_json_response import CallSiprecJsonResponse as CallSiprecJsonResponse
    from .call_streams_json_response import CallStreamsJsonResponse as CallStreamsJsonResponse
    from .call_retrieve_calls_response import CallRetrieveCallsResponse as CallRetrieveCallsResponse
    from .conference_retrieve_recordings_response import (
        ConferenceRetrieveRecordingsResponse as ConferenceRetrieveRecordingsResponse,
    )
    from .conference_retrieve_conferences_response import (
        ConferenceRetrieveConferencesResponse as ConferenceRetrieveConferencesResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "CallResource":
        from .call_resource import CallResource

        return CallResource
    if name == "CallCallsResponse":
        from .call_calls_response import CallCallsResponse

        return CallCallsResponse
    if name == "CallRetrieveCallsResponse":
        from .call_retrieve_calls_response import CallRetrieveCallsResponse

        return CallRetrieveCallsResponse
    if name == "CallSiprecJsonResponse":
        from .call_siprec_json_response import CallSiprecJsonResponse

        return CallSiprecJsonResponse
    if name == "CallStreamsJsonResponse":
        from .call_streams_json_response import CallStreamsJsonResponse

        return CallStreamsJsonResponse
    if name == "ConferenceResource":
        from .conference_resource import ConferenceResource

        return ConferenceResource
    if name == "ConferenceRetrieveConferencesResponse":
        from .conference_retrieve_conferences_response import ConferenceRetrieveConferencesResponse

        return ConferenceRetrieveConferencesResponse
    if name == "ConferenceRetrieveRecordingsResponse":
        from .conference_retrieve_recordings_response import ConferenceRetrieveRecordingsResponse

        return ConferenceRetrieveRecordingsResponse
    if name == "QueueResource":
        from .queue_resource import QueueResource

        return QueueResource
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
