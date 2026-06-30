# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .job_list_params import JobListParams as JobListParams
from .voice_list_params import VoiceListParams as VoiceListParams
from .cnam_listing_param import CnamListingParam as CnamListingParam
from .voice_update_params import VoiceUpdateParams as VoiceUpdateParams
from .call_recording_param import CallRecordingParam as CallRecordingParam
from .media_features_param import MediaFeaturesParam as MediaFeaturesParam
from .call_forwarding_param import CallForwardingParam as CallForwardingParam
from .messaging_list_params import MessagingListParams as MessagingListParams
from .job_delete_batch_params import JobDeleteBatchParams as JobDeleteBatchParams
from .job_update_batch_params import JobUpdateBatchParams as JobUpdateBatchParams
from .messaging_update_params import MessagingUpdateParams as MessagingUpdateParams
from .voicemail_create_params import VoicemailCreateParams as VoicemailCreateParams
from .voicemail_update_params import VoicemailUpdateParams as VoicemailUpdateParams
from .csv_download_list_params import CsvDownloadListParams as CsvDownloadListParams
from .csv_download_create_params import CsvDownloadCreateParams as CsvDownloadCreateParams
from .update_voice_settings_param import UpdateVoiceSettingsParam as UpdateVoiceSettingsParam
from .action_enable_emergency_params import ActionEnableEmergencyParams as ActionEnableEmergencyParams
from .action_verify_ownership_params import ActionVerifyOwnershipParams as ActionVerifyOwnershipParams
from .action_change_bundle_status_params import ActionChangeBundleStatusParams as ActionChangeBundleStatusParams
from .job_update_emergency_settings_batch_params import (
    JobUpdateEmergencySettingsBatchParams as JobUpdateEmergencySettingsBatchParams,
)

if TYPE_CHECKING:
    from .cnam_listing import CnamListing as CnamListing
    from .csv_download import CsvDownload as CsvDownload
    from .call_recording import CallRecording as CallRecording
    from .media_features import MediaFeatures as MediaFeatures
    from .call_forwarding import CallForwarding as CallForwarding
    from .phone_numbers_job import PhoneNumbersJob as PhoneNumbersJob
    from .job_retrieve_response import JobRetrieveResponse as JobRetrieveResponse
    from .voice_update_response import VoiceUpdateResponse as VoiceUpdateResponse
    from .voice_retrieve_response import VoiceRetrieveResponse as VoiceRetrieveResponse
    from .voicemail_pref_response import VoicemailPrefResponse as VoicemailPrefResponse
    from .job_delete_batch_response import JobDeleteBatchResponse as JobDeleteBatchResponse
    from .job_update_batch_response import JobUpdateBatchResponse as JobUpdateBatchResponse
    from .messaging_update_response import MessagingUpdateResponse as MessagingUpdateResponse
    from .voicemail_create_response import VoicemailCreateResponse as VoicemailCreateResponse
    from .voicemail_update_response import VoicemailUpdateResponse as VoicemailUpdateResponse
    from .messaging_retrieve_response import MessagingRetrieveResponse as MessagingRetrieveResponse
    from .voicemail_retrieve_response import VoicemailRetrieveResponse as VoicemailRetrieveResponse
    from .csv_download_create_response import CsvDownloadCreateResponse as CsvDownloadCreateResponse
    from .csv_download_retrieve_response import CsvDownloadRetrieveResponse as CsvDownloadRetrieveResponse
    from .action_enable_emergency_response import ActionEnableEmergencyResponse as ActionEnableEmergencyResponse
    from .action_verify_ownership_response import ActionVerifyOwnershipResponse as ActionVerifyOwnershipResponse
    from .phone_number_with_voice_settings import PhoneNumberWithVoiceSettings as PhoneNumberWithVoiceSettings
    from .action_change_bundle_status_response import (
        ActionChangeBundleStatusResponse as ActionChangeBundleStatusResponse,
    )
    from .job_update_emergency_settings_batch_response import (
        JobUpdateEmergencySettingsBatchResponse as JobUpdateEmergencySettingsBatchResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "PhoneNumberWithVoiceSettings":
        from .phone_number_with_voice_settings import PhoneNumberWithVoiceSettings

        return PhoneNumberWithVoiceSettings
    if name == "ActionChangeBundleStatusResponse":
        from .action_change_bundle_status_response import ActionChangeBundleStatusResponse

        return ActionChangeBundleStatusResponse
    if name == "ActionEnableEmergencyResponse":
        from .action_enable_emergency_response import ActionEnableEmergencyResponse

        return ActionEnableEmergencyResponse
    if name == "ActionVerifyOwnershipResponse":
        from .action_verify_ownership_response import ActionVerifyOwnershipResponse

        return ActionVerifyOwnershipResponse
    if name == "CsvDownload":
        from .csv_download import CsvDownload

        return CsvDownload
    if name == "CsvDownloadCreateResponse":
        from .csv_download_create_response import CsvDownloadCreateResponse

        return CsvDownloadCreateResponse
    if name == "CsvDownloadRetrieveResponse":
        from .csv_download_retrieve_response import CsvDownloadRetrieveResponse

        return CsvDownloadRetrieveResponse
    if name == "PhoneNumbersJob":
        from .phone_numbers_job import PhoneNumbersJob

        return PhoneNumbersJob
    if name == "JobRetrieveResponse":
        from .job_retrieve_response import JobRetrieveResponse

        return JobRetrieveResponse
    if name == "JobDeleteBatchResponse":
        from .job_delete_batch_response import JobDeleteBatchResponse

        return JobDeleteBatchResponse
    if name == "JobUpdateBatchResponse":
        from .job_update_batch_response import JobUpdateBatchResponse

        return JobUpdateBatchResponse
    if name == "JobUpdateEmergencySettingsBatchResponse":
        from .job_update_emergency_settings_batch_response import JobUpdateEmergencySettingsBatchResponse

        return JobUpdateEmergencySettingsBatchResponse
    if name == "MessagingRetrieveResponse":
        from .messaging_retrieve_response import MessagingRetrieveResponse

        return MessagingRetrieveResponse
    if name == "MessagingUpdateResponse":
        from .messaging_update_response import MessagingUpdateResponse

        return MessagingUpdateResponse
    if name == "CallForwarding":
        from .call_forwarding import CallForwarding

        return CallForwarding
    if name == "CallRecording":
        from .call_recording import CallRecording

        return CallRecording
    if name == "CnamListing":
        from .cnam_listing import CnamListing

        return CnamListing
    if name == "MediaFeatures":
        from .media_features import MediaFeatures

        return MediaFeatures
    if name == "VoiceRetrieveResponse":
        from .voice_retrieve_response import VoiceRetrieveResponse

        return VoiceRetrieveResponse
    if name == "VoiceUpdateResponse":
        from .voice_update_response import VoiceUpdateResponse

        return VoiceUpdateResponse
    if name == "VoicemailPrefResponse":
        from .voicemail_pref_response import VoicemailPrefResponse

        return VoicemailPrefResponse
    if name == "VoicemailCreateResponse":
        from .voicemail_create_response import VoicemailCreateResponse

        return VoicemailCreateResponse
    if name == "VoicemailRetrieveResponse":
        from .voicemail_retrieve_response import VoicemailRetrieveResponse

        return VoicemailRetrieveResponse
    if name == "VoicemailUpdateResponse":
        from .voicemail_update_response import VoicemailUpdateResponse

        return VoicemailUpdateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
