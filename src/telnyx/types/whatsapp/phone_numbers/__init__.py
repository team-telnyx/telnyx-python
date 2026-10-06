# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .profile_update_params import ProfileUpdateParams as ProfileUpdateParams
from .calling_setting_update_params import CallingSettingUpdateParams as CallingSettingUpdateParams
from .calling_routing_patch_all_params import CallingRoutingPatchAllParams as CallingRoutingPatchAllParams
from .conversational_component_patch_all_params import (
    ConversationalComponentPatchAllParams as ConversationalComponentPatchAllParams,
)

if TYPE_CHECKING:
    from .whatsapp_profile_data import WhatsappProfileData as WhatsappProfileData
    from .profile_update_response import ProfileUpdateResponse as ProfileUpdateResponse
    from .profile_retrieve_response import ProfileRetrieveResponse as ProfileRetrieveResponse
    from .calling_routing_list_response import CallingRoutingListResponse as CallingRoutingListResponse
    from .whatsapp_calling_routing_data import WhatsappCallingRoutingData as WhatsappCallingRoutingData
    from .whatsapp_calling_settings_data import WhatsappCallingSettingsData as WhatsappCallingSettingsData
    from .calling_setting_update_response import CallingSettingUpdateResponse as CallingSettingUpdateResponse
    from .calling_setting_retrieve_response import CallingSettingRetrieveResponse as CallingSettingRetrieveResponse
    from .whatsapp_conversational_component import WhatsappConversationalComponent as WhatsappConversationalComponent
    from .calling_routing_patch_all_response import CallingRoutingPatchAllResponse as CallingRoutingPatchAllResponse
    from .conversational_component_list_response import (
        ConversationalComponentListResponse as ConversationalComponentListResponse,
    )
    from .conversational_component_patch_all_response import (
        ConversationalComponentPatchAllResponse as ConversationalComponentPatchAllResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "WhatsappCallingSettingsData":
        from .whatsapp_calling_settings_data import WhatsappCallingSettingsData

        return WhatsappCallingSettingsData
    if name == "CallingSettingRetrieveResponse":
        from .calling_setting_retrieve_response import CallingSettingRetrieveResponse

        return CallingSettingRetrieveResponse
    if name == "CallingSettingUpdateResponse":
        from .calling_setting_update_response import CallingSettingUpdateResponse

        return CallingSettingUpdateResponse
    if name == "WhatsappProfileData":
        from .whatsapp_profile_data import WhatsappProfileData

        return WhatsappProfileData
    if name == "ProfileRetrieveResponse":
        from .profile_retrieve_response import ProfileRetrieveResponse

        return ProfileRetrieveResponse
    if name == "ProfileUpdateResponse":
        from .profile_update_response import ProfileUpdateResponse

        return ProfileUpdateResponse
    if name == "WhatsappConversationalComponent":
        from .whatsapp_conversational_component import WhatsappConversationalComponent

        return WhatsappConversationalComponent
    if name == "ConversationalComponentListResponse":
        from .conversational_component_list_response import ConversationalComponentListResponse

        return ConversationalComponentListResponse
    if name == "ConversationalComponentPatchAllResponse":
        from .conversational_component_patch_all_response import ConversationalComponentPatchAllResponse

        return ConversationalComponentPatchAllResponse
    if name == "WhatsappCallingRoutingData":
        from .whatsapp_calling_routing_data import WhatsappCallingRoutingData

        return WhatsappCallingRoutingData
    if name == "CallingRoutingListResponse":
        from .calling_routing_list_response import CallingRoutingListResponse

        return CallingRoutingListResponse
    if name == "CallingRoutingPatchAllResponse":
        from .calling_routing_patch_all_response import CallingRoutingPatchAllResponse

        return CallingRoutingPatchAllResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
