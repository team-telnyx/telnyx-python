# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .upload_list_params import UploadListParams as UploadListParams
from .release_list_params import ReleaseListParams as ReleaseListParams
from .upload_create_params import UploadCreateParams as UploadCreateParams
from .log_message_list_params import LogMessageListParams as LogMessageListParams
from .phone_number_list_params import PhoneNumberListParams as PhoneNumberListParams
from .civic_address_list_params import CivicAddressListParams as CivicAddressListParams
from .phone_number_update_params import PhoneNumberUpdateParams as PhoneNumberUpdateParams

if TYPE_CHECKING:
    from .upload import Upload as Upload
    from .release import Release as Release
    from .location import Location as Location
    from .log_message import LogMessage as LogMessage
    from .civic_address import CivicAddress as CivicAddress
    from .tn_upload_entry import TnUploadEntry as TnUploadEntry
    from .tn_release_entry import TnReleaseEntry as TnReleaseEntry
    from .upload_retry_response import UploadRetryResponse as UploadRetryResponse
    from .upload_create_response import UploadCreateResponse as UploadCreateResponse
    from .upload_retrieve_response import UploadRetrieveResponse as UploadRetrieveResponse
    from .release_retrieve_response import ReleaseRetrieveResponse as ReleaseRetrieveResponse
    from .civic_address_list_response import CivicAddressListResponse as CivicAddressListResponse
    from .log_message_dismiss_response import LogMessageDismissResponse as LogMessageDismissResponse
    from .phone_number_update_response import PhoneNumberUpdateResponse as PhoneNumberUpdateResponse
    from .log_message_retrieve_response import LogMessageRetrieveResponse as LogMessageRetrieveResponse
    from .upload_pending_count_response import UploadPendingCountResponse as UploadPendingCountResponse
    from .phone_number_retrieve_response import PhoneNumberRetrieveResponse as PhoneNumberRetrieveResponse
    from .upload_refresh_status_response import UploadRefreshStatusResponse as UploadRefreshStatusResponse
    from .civic_address_retrieve_response import CivicAddressRetrieveResponse as CivicAddressRetrieveResponse
    from .external_connection_phone_number import ExternalConnectionPhoneNumber as ExternalConnectionPhoneNumber


def __getattr__(name: str) -> Any:
    if name == "LogMessage":
        from .log_message import LogMessage

        return LogMessage
    if name == "LogMessageRetrieveResponse":
        from .log_message_retrieve_response import LogMessageRetrieveResponse

        return LogMessageRetrieveResponse
    if name == "LogMessageDismissResponse":
        from .log_message_dismiss_response import LogMessageDismissResponse

        return LogMessageDismissResponse
    if name == "CivicAddress":
        from .civic_address import CivicAddress

        return CivicAddress
    if name == "Location":
        from .location import Location

        return Location
    if name == "CivicAddressRetrieveResponse":
        from .civic_address_retrieve_response import CivicAddressRetrieveResponse

        return CivicAddressRetrieveResponse
    if name == "CivicAddressListResponse":
        from .civic_address_list_response import CivicAddressListResponse

        return CivicAddressListResponse
    if name == "ExternalConnectionPhoneNumber":
        from .external_connection_phone_number import ExternalConnectionPhoneNumber

        return ExternalConnectionPhoneNumber
    if name == "PhoneNumberRetrieveResponse":
        from .phone_number_retrieve_response import PhoneNumberRetrieveResponse

        return PhoneNumberRetrieveResponse
    if name == "PhoneNumberUpdateResponse":
        from .phone_number_update_response import PhoneNumberUpdateResponse

        return PhoneNumberUpdateResponse
    if name == "Release":
        from .release import Release

        return Release
    if name == "TnReleaseEntry":
        from .tn_release_entry import TnReleaseEntry

        return TnReleaseEntry
    if name == "ReleaseRetrieveResponse":
        from .release_retrieve_response import ReleaseRetrieveResponse

        return ReleaseRetrieveResponse
    if name == "TnUploadEntry":
        from .tn_upload_entry import TnUploadEntry

        return TnUploadEntry
    if name == "Upload":
        from .upload import Upload

        return Upload
    if name == "UploadCreateResponse":
        from .upload_create_response import UploadCreateResponse

        return UploadCreateResponse
    if name == "UploadRetrieveResponse":
        from .upload_retrieve_response import UploadRetrieveResponse

        return UploadRetrieveResponse
    if name == "UploadPendingCountResponse":
        from .upload_pending_count_response import UploadPendingCountResponse

        return UploadPendingCountResponse
    if name == "UploadRefreshStatusResponse":
        from .upload_refresh_status_response import UploadRefreshStatusResponse

        return UploadRefreshStatusResponse
    if name == "UploadRetryResponse":
        from .upload_retry_response import UploadRetryResponse

        return UploadRetryResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
