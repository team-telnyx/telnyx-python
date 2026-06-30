# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .messaging_list_params import MessagingListParams as MessagingListParams

if TYPE_CHECKING:
    from .messaging_retrieve_response import MessagingRetrieveResponse as MessagingRetrieveResponse
    from .mobile_phone_number_with_messaging_settings import (
        MobilePhoneNumberWithMessagingSettings as MobilePhoneNumberWithMessagingSettings,
    )


def __getattr__(name: str) -> Any:
    if name == "MobilePhoneNumberWithMessagingSettings":
        from .mobile_phone_number_with_messaging_settings import MobilePhoneNumberWithMessagingSettings

        return MobilePhoneNumberWithMessagingSettings
    if name == "MessagingRetrieveResponse":
        from .messaging_retrieve_response import MessagingRetrieveResponse

        return MessagingRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
