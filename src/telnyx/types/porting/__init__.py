# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .porting_event import PortingEvent as PortingEvent
from .event_list_params import EventListParams as EventListParams
from .report_list_params import ReportListParams as ReportListParams
from .report_create_params import ReportCreateParams as ReportCreateParams
from .loa_configuration_list_params import LoaConfigurationListParams as LoaConfigurationListParams
from .loa_configuration_create_params import LoaConfigurationCreateParams as LoaConfigurationCreateParams
from .loa_configuration_update_params import LoaConfigurationUpdateParams as LoaConfigurationUpdateParams
from .loa_configuration_preview_params import LoaConfigurationPreviewParams as LoaConfigurationPreviewParams
from .loa_configuration_preview_0_params import LoaConfigurationPreview0Params as LoaConfigurationPreview0Params
from .export_porting_orders_csv_report_param import (
    ExportPortingOrdersCsvReportParam as ExportPortingOrdersCsvReportParam,
)

if TYPE_CHECKING:
    from .porting_report import PortingReport as PortingReport
    from .report_create_response import ReportCreateResponse as ReportCreateResponse
    from .event_retrieve_response import EventRetrieveResponse as EventRetrieveResponse
    from .report_retrieve_response import ReportRetrieveResponse as ReportRetrieveResponse
    from .porting_event_split_event import PortingEventSplitEvent as PortingEventSplitEvent
    from .porting_loa_configuration import PortingLoaConfiguration as PortingLoaConfiguration
    from .porting_event_deleted_payload import PortingEventDeletedPayload as PortingEventDeletedPayload
    from .porting_event_without_webhook import PortingEventWithoutWebhook as PortingEventWithoutWebhook
    from .porting_event_new_comment_event import PortingEventNewCommentEvent as PortingEventNewCommentEvent
    from .export_porting_orders_csv_report import ExportPortingOrdersCsvReport as ExportPortingOrdersCsvReport
    from .loa_configuration_create_response import LoaConfigurationCreateResponse as LoaConfigurationCreateResponse
    from .loa_configuration_update_response import LoaConfigurationUpdateResponse as LoaConfigurationUpdateResponse
    from .porting_event_status_changed_event import PortingEventStatusChangedEvent as PortingEventStatusChangedEvent
    from .loa_configuration_retrieve_response import (
        LoaConfigurationRetrieveResponse as LoaConfigurationRetrieveResponse,
    )
    from .porting_event_messaging_changed_payload import (
        PortingEventMessagingChangedPayload as PortingEventMessagingChangedPayload,
    )


def __getattr__(name: str) -> Any:
    if name == "PortingEventDeletedPayload":
        from .porting_event_deleted_payload import PortingEventDeletedPayload

        return PortingEventDeletedPayload
    if name == "PortingEventMessagingChangedPayload":
        from .porting_event_messaging_changed_payload import PortingEventMessagingChangedPayload

        return PortingEventMessagingChangedPayload
    if name == "PortingEventNewCommentEvent":
        from .porting_event_new_comment_event import PortingEventNewCommentEvent

        return PortingEventNewCommentEvent
    if name == "PortingEventSplitEvent":
        from .porting_event_split_event import PortingEventSplitEvent

        return PortingEventSplitEvent
    if name == "PortingEventStatusChangedEvent":
        from .porting_event_status_changed_event import PortingEventStatusChangedEvent

        return PortingEventStatusChangedEvent
    if name == "PortingEventWithoutWebhook":
        from .porting_event_without_webhook import PortingEventWithoutWebhook

        return PortingEventWithoutWebhook
    if name == "EventRetrieveResponse":
        from .event_retrieve_response import EventRetrieveResponse

        return EventRetrieveResponse
    if name == "ExportPortingOrdersCsvReport":
        from .export_porting_orders_csv_report import ExportPortingOrdersCsvReport

        return ExportPortingOrdersCsvReport
    if name == "PortingReport":
        from .porting_report import PortingReport

        return PortingReport
    if name == "ReportCreateResponse":
        from .report_create_response import ReportCreateResponse

        return ReportCreateResponse
    if name == "ReportRetrieveResponse":
        from .report_retrieve_response import ReportRetrieveResponse

        return ReportRetrieveResponse
    if name == "PortingLoaConfiguration":
        from .porting_loa_configuration import PortingLoaConfiguration

        return PortingLoaConfiguration
    if name == "LoaConfigurationCreateResponse":
        from .loa_configuration_create_response import LoaConfigurationCreateResponse

        return LoaConfigurationCreateResponse
    if name == "LoaConfigurationRetrieveResponse":
        from .loa_configuration_retrieve_response import LoaConfigurationRetrieveResponse

        return LoaConfigurationRetrieveResponse
    if name == "LoaConfigurationUpdateResponse":
        from .loa_configuration_update_response import LoaConfigurationUpdateResponse

        return LoaConfigurationUpdateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
