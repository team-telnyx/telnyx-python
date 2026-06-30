# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_list_params import ActionListParams as ActionListParams
from .action_set_public_ip_params import ActionSetPublicIPParams as ActionSetPublicIPParams
from .action_bulk_enable_voice_params import ActionBulkEnableVoiceParams as ActionBulkEnableVoiceParams
from .action_bulk_disable_voice_params import ActionBulkDisableVoiceParams as ActionBulkDisableVoiceParams
from .action_bulk_set_public_ips_params import ActionBulkSetPublicIPsParams as ActionBulkSetPublicIPsParams
from .action_validate_registration_codes_params import (
    ActionValidateRegistrationCodesParams as ActionValidateRegistrationCodesParams,
)

if TYPE_CHECKING:
    from .sim_card_action import SimCardAction as SimCardAction
    from .bulk_sim_card_action import BulkSimCardAction as BulkSimCardAction
    from .action_enable_response import ActionEnableResponse as ActionEnableResponse
    from .action_disable_response import ActionDisableResponse as ActionDisableResponse
    from .action_retrieve_response import ActionRetrieveResponse as ActionRetrieveResponse
    from .action_set_standby_response import ActionSetStandbyResponse as ActionSetStandbyResponse
    from .action_set_public_ip_response import ActionSetPublicIPResponse as ActionSetPublicIPResponse
    from .action_remove_public_ip_response import ActionRemovePublicIPResponse as ActionRemovePublicIPResponse
    from .action_bulk_enable_voice_response import ActionBulkEnableVoiceResponse as ActionBulkEnableVoiceResponse
    from .action_bulk_disable_voice_response import ActionBulkDisableVoiceResponse as ActionBulkDisableVoiceResponse
    from .action_bulk_set_public_ips_response import ActionBulkSetPublicIPsResponse as ActionBulkSetPublicIPsResponse
    from .action_validate_registration_codes_response import (
        ActionValidateRegistrationCodesResponse as ActionValidateRegistrationCodesResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "BulkSimCardAction":
        from .bulk_sim_card_action import BulkSimCardAction

        return BulkSimCardAction
    if name == "SimCardAction":
        from .sim_card_action import SimCardAction

        return SimCardAction
    if name == "ActionRetrieveResponse":
        from .action_retrieve_response import ActionRetrieveResponse

        return ActionRetrieveResponse
    if name == "ActionBulkDisableVoiceResponse":
        from .action_bulk_disable_voice_response import ActionBulkDisableVoiceResponse

        return ActionBulkDisableVoiceResponse
    if name == "ActionBulkEnableVoiceResponse":
        from .action_bulk_enable_voice_response import ActionBulkEnableVoiceResponse

        return ActionBulkEnableVoiceResponse
    if name == "ActionBulkSetPublicIPsResponse":
        from .action_bulk_set_public_ips_response import ActionBulkSetPublicIPsResponse

        return ActionBulkSetPublicIPsResponse
    if name == "ActionDisableResponse":
        from .action_disable_response import ActionDisableResponse

        return ActionDisableResponse
    if name == "ActionEnableResponse":
        from .action_enable_response import ActionEnableResponse

        return ActionEnableResponse
    if name == "ActionRemovePublicIPResponse":
        from .action_remove_public_ip_response import ActionRemovePublicIPResponse

        return ActionRemovePublicIPResponse
    if name == "ActionSetPublicIPResponse":
        from .action_set_public_ip_response import ActionSetPublicIPResponse

        return ActionSetPublicIPResponse
    if name == "ActionSetStandbyResponse":
        from .action_set_standby_response import ActionSetStandbyResponse

        return ActionSetStandbyResponse
    if name == "ActionValidateRegistrationCodesResponse":
        from .action_validate_registration_codes_response import ActionValidateRegistrationCodesResponse

        return ActionValidateRegistrationCodesResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
