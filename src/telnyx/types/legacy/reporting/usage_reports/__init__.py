# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .voice_list_params import VoiceListParams as VoiceListParams
from .voice_create_params import VoiceCreateParams as VoiceCreateParams
from .messaging_list_params import MessagingListParams as MessagingListParams
from .messaging_create_params import MessagingCreateParams as MessagingCreateParams
from .number_lookup_list_params import NumberLookupListParams as NumberLookupListParams
from .number_lookup_create_params import NumberLookupCreateParams as NumberLookupCreateParams

if TYPE_CHECKING:
    from .voice_create_response import VoiceCreateResponse as VoiceCreateResponse
    from .voice_delete_response import VoiceDeleteResponse as VoiceDeleteResponse
    from .telco_data_aggregation import TelcoDataAggregation as TelcoDataAggregation
    from .telco_data_usage_record import TelcoDataUsageRecord as TelcoDataUsageRecord
    from .voice_retrieve_response import VoiceRetrieveResponse as VoiceRetrieveResponse
    from .standard_pagination_meta import StandardPaginationMeta as StandardPaginationMeta
    from .messaging_create_response import MessagingCreateResponse as MessagingCreateResponse
    from .messaging_delete_response import MessagingDeleteResponse as MessagingDeleteResponse
    from .messaging_retrieve_response import MessagingRetrieveResponse as MessagingRetrieveResponse
    from .number_lookup_create_response import NumberLookupCreateResponse as NumberLookupCreateResponse
    from .number_lookup_retrieve_response import NumberLookupRetrieveResponse as NumberLookupRetrieveResponse
    from .cdr_usage_report_response_legacy import CdrUsageReportResponseLegacy as CdrUsageReportResponseLegacy
    from .mdr_usage_report_response_legacy import MdrUsageReportResponseLegacy as MdrUsageReportResponseLegacy
    from .telco_data_usage_report_response import TelcoDataUsageReportResponse as TelcoDataUsageReportResponse


def __getattr__(name: str) -> Any:
    if name == "MdrUsageReportResponseLegacy":
        from .mdr_usage_report_response_legacy import MdrUsageReportResponseLegacy

        return MdrUsageReportResponseLegacy
    if name == "StandardPaginationMeta":
        from .standard_pagination_meta import StandardPaginationMeta

        return StandardPaginationMeta
    if name == "MessagingCreateResponse":
        from .messaging_create_response import MessagingCreateResponse

        return MessagingCreateResponse
    if name == "MessagingRetrieveResponse":
        from .messaging_retrieve_response import MessagingRetrieveResponse

        return MessagingRetrieveResponse
    if name == "MessagingDeleteResponse":
        from .messaging_delete_response import MessagingDeleteResponse

        return MessagingDeleteResponse
    if name == "TelcoDataAggregation":
        from .telco_data_aggregation import TelcoDataAggregation

        return TelcoDataAggregation
    if name == "TelcoDataUsageRecord":
        from .telco_data_usage_record import TelcoDataUsageRecord

        return TelcoDataUsageRecord
    if name == "TelcoDataUsageReportResponse":
        from .telco_data_usage_report_response import TelcoDataUsageReportResponse

        return TelcoDataUsageReportResponse
    if name == "NumberLookupCreateResponse":
        from .number_lookup_create_response import NumberLookupCreateResponse

        return NumberLookupCreateResponse
    if name == "NumberLookupRetrieveResponse":
        from .number_lookup_retrieve_response import NumberLookupRetrieveResponse

        return NumberLookupRetrieveResponse
    if name == "CdrUsageReportResponseLegacy":
        from .cdr_usage_report_response_legacy import CdrUsageReportResponseLegacy

        return CdrUsageReportResponseLegacy
    if name == "VoiceCreateResponse":
        from .voice_create_response import VoiceCreateResponse

        return VoiceCreateResponse
    if name == "VoiceRetrieveResponse":
        from .voice_retrieve_response import VoiceRetrieveResponse

        return VoiceRetrieveResponse
    if name == "VoiceDeleteResponse":
        from .voice_delete_response import VoiceDeleteResponse

        return VoiceDeleteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
