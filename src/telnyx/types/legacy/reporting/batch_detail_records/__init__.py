# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .voice_create_params import VoiceCreateParams as VoiceCreateParams
from .messaging_create_params import MessagingCreateParams as MessagingCreateParams
from .speech_to_text_create_params import SpeechToTextCreateParams as SpeechToTextCreateParams

if TYPE_CHECKING:
    from .voice_list_response import VoiceListResponse as VoiceListResponse
    from .voice_create_response import VoiceCreateResponse as VoiceCreateResponse
    from .voice_delete_response import VoiceDeleteResponse as VoiceDeleteResponse
    from .messaging_list_response import MessagingListResponse as MessagingListResponse
    from .voice_retrieve_response import VoiceRetrieveResponse as VoiceRetrieveResponse
    from .batch_csv_pagination_meta import BatchCsvPaginationMeta as BatchCsvPaginationMeta
    from .cdr_detailed_req_response import CdrDetailedReqResponse as CdrDetailedReqResponse
    from .messaging_create_response import MessagingCreateResponse as MessagingCreateResponse
    from .messaging_delete_response import MessagingDeleteResponse as MessagingDeleteResponse
    from .mdr_detail_report_response import MdrDetailReportResponse as MdrDetailReportResponse
    from .stt_detail_report_response import SttDetailReportResponse as SttDetailReportResponse
    from .messaging_retrieve_response import MessagingRetrieveResponse as MessagingRetrieveResponse
    from .speech_to_text_list_response import SpeechToTextListResponse as SpeechToTextListResponse
    from .speech_to_text_create_response import SpeechToTextCreateResponse as SpeechToTextCreateResponse
    from .speech_to_text_delete_response import SpeechToTextDeleteResponse as SpeechToTextDeleteResponse
    from .voice_retrieve_fields_response import VoiceRetrieveFieldsResponse as VoiceRetrieveFieldsResponse
    from .speech_to_text_retrieve_response import SpeechToTextRetrieveResponse as SpeechToTextRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "BatchCsvPaginationMeta":
        from .batch_csv_pagination_meta import BatchCsvPaginationMeta

        return BatchCsvPaginationMeta
    if name == "MdrDetailReportResponse":
        from .mdr_detail_report_response import MdrDetailReportResponse

        return MdrDetailReportResponse
    if name == "MessagingCreateResponse":
        from .messaging_create_response import MessagingCreateResponse

        return MessagingCreateResponse
    if name == "MessagingRetrieveResponse":
        from .messaging_retrieve_response import MessagingRetrieveResponse

        return MessagingRetrieveResponse
    if name == "MessagingListResponse":
        from .messaging_list_response import MessagingListResponse

        return MessagingListResponse
    if name == "MessagingDeleteResponse":
        from .messaging_delete_response import MessagingDeleteResponse

        return MessagingDeleteResponse
    if name == "SttDetailReportResponse":
        from .stt_detail_report_response import SttDetailReportResponse

        return SttDetailReportResponse
    if name == "SpeechToTextCreateResponse":
        from .speech_to_text_create_response import SpeechToTextCreateResponse

        return SpeechToTextCreateResponse
    if name == "SpeechToTextRetrieveResponse":
        from .speech_to_text_retrieve_response import SpeechToTextRetrieveResponse

        return SpeechToTextRetrieveResponse
    if name == "SpeechToTextListResponse":
        from .speech_to_text_list_response import SpeechToTextListResponse

        return SpeechToTextListResponse
    if name == "SpeechToTextDeleteResponse":
        from .speech_to_text_delete_response import SpeechToTextDeleteResponse

        return SpeechToTextDeleteResponse
    if name == "CdrDetailedReqResponse":
        from .cdr_detailed_req_response import CdrDetailedReqResponse

        return CdrDetailedReqResponse
    if name == "VoiceCreateResponse":
        from .voice_create_response import VoiceCreateResponse

        return VoiceCreateResponse
    if name == "VoiceRetrieveResponse":
        from .voice_retrieve_response import VoiceRetrieveResponse

        return VoiceRetrieveResponse
    if name == "VoiceListResponse":
        from .voice_list_response import VoiceListResponse

        return VoiceListResponse
    if name == "VoiceDeleteResponse":
        from .voice_delete_response import VoiceDeleteResponse

        return VoiceDeleteResponse
    if name == "VoiceRetrieveFieldsResponse":
        from .voice_retrieve_fields_response import VoiceRetrieveFieldsResponse

        return VoiceRetrieveFieldsResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
