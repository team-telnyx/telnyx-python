# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .setting_update_params import SettingUpdateParams as SettingUpdateParams
from .phone_number_list_params import PhoneNumberListParams as PhoneNumberListParams
from .phone_number_initialize_verification_params import (
    PhoneNumberInitializeVerificationParams as PhoneNumberInitializeVerificationParams,
)

if TYPE_CHECKING:
    from .waba_settings import WabaSettings as WabaSettings
    from .setting_update_response import SettingUpdateResponse as SettingUpdateResponse
    from .setting_retrieve_response import SettingRetrieveResponse as SettingRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "WabaSettings":
        from .waba_settings import WabaSettings

        return WabaSettings
    if name == "SettingRetrieveResponse":
        from .setting_retrieve_response import SettingRetrieveResponse

        return SettingRetrieveResponse
    if name == "SettingUpdateResponse":
        from .setting_update_response import SettingUpdateResponse

        return SettingUpdateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
