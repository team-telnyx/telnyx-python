# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .portout_event import PortoutEvent as PortoutEvent
from .event_list_params import EventListParams as EventListParams
from .report_list_params import ReportListParams as ReportListParams
from .report_create_params import ReportCreateParams as ReportCreateParams
from .comment_create_params import CommentCreateParams as CommentCreateParams
from .export_portouts_csv_report_param import ExportPortoutsCsvReportParam as ExportPortoutsCsvReportParam
from .supporting_document_create_params import SupportingDocumentCreateParams as SupportingDocumentCreateParams

if TYPE_CHECKING:
    from .portout_report import PortoutReport as PortoutReport
    from .portout_comment import PortoutComment as PortoutComment
    from .comment_list_response import CommentListResponse as CommentListResponse
    from .report_create_response import ReportCreateResponse as ReportCreateResponse
    from .comment_create_response import CommentCreateResponse as CommentCreateResponse
    from .event_retrieve_response import EventRetrieveResponse as EventRetrieveResponse
    from .report_retrieve_response import ReportRetrieveResponse as ReportRetrieveResponse
    from .export_portouts_csv_report import ExportPortoutsCsvReport as ExportPortoutsCsvReport
    from .webhook_portout_new_comment import WebhookPortoutNewComment as WebhookPortoutNewComment
    from .port_out_supporting_document import PortOutSupportingDocument as PortOutSupportingDocument
    from .webhook_portout_status_changed import WebhookPortoutStatusChanged as WebhookPortoutStatusChanged
    from .webhook_portout_foc_date_changed import WebhookPortoutFocDateChanged as WebhookPortoutFocDateChanged
    from .supporting_document_list_response import SupportingDocumentListResponse as SupportingDocumentListResponse
    from .supporting_document_create_response import (
        SupportingDocumentCreateResponse as SupportingDocumentCreateResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "WebhookPortoutFocDateChanged":
        from .webhook_portout_foc_date_changed import WebhookPortoutFocDateChanged

        return WebhookPortoutFocDateChanged
    if name == "WebhookPortoutNewComment":
        from .webhook_portout_new_comment import WebhookPortoutNewComment

        return WebhookPortoutNewComment
    if name == "WebhookPortoutStatusChanged":
        from .webhook_portout_status_changed import WebhookPortoutStatusChanged

        return WebhookPortoutStatusChanged
    if name == "EventRetrieveResponse":
        from .event_retrieve_response import EventRetrieveResponse

        return EventRetrieveResponse
    if name == "ExportPortoutsCsvReport":
        from .export_portouts_csv_report import ExportPortoutsCsvReport

        return ExportPortoutsCsvReport
    if name == "PortoutReport":
        from .portout_report import PortoutReport

        return PortoutReport
    if name == "ReportCreateResponse":
        from .report_create_response import ReportCreateResponse

        return ReportCreateResponse
    if name == "ReportRetrieveResponse":
        from .report_retrieve_response import ReportRetrieveResponse

        return ReportRetrieveResponse
    if name == "PortoutComment":
        from .portout_comment import PortoutComment

        return PortoutComment
    if name == "CommentCreateResponse":
        from .comment_create_response import CommentCreateResponse

        return CommentCreateResponse
    if name == "CommentListResponse":
        from .comment_list_response import CommentListResponse

        return CommentListResponse
    if name == "PortOutSupportingDocument":
        from .port_out_supporting_document import PortOutSupportingDocument

        return PortOutSupportingDocument
    if name == "SupportingDocumentCreateResponse":
        from .supporting_document_create_response import SupportingDocumentCreateResponse

        return SupportingDocumentCreateResponse
    if name == "SupportingDocumentListResponse":
        from .supporting_document_list_response import SupportingDocumentListResponse

        return SupportingDocumentListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
