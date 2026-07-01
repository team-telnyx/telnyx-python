# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_list_params import ActionListParams as ActionListParams
from .action_set_wireless_blocklist_params import ActionSetWirelessBlocklistParams as ActionSetWirelessBlocklistParams
from .action_set_private_wireless_gateway_params import (
    ActionSetPrivateWirelessGatewayParams as ActionSetPrivateWirelessGatewayParams,
)

if TYPE_CHECKING:
    from .sim_card_group_action import SimCardGroupAction as SimCardGroupAction
    from .action_retrieve_response import ActionRetrieveResponse as ActionRetrieveResponse
    from .action_set_wireless_blocklist_response import (
        ActionSetWirelessBlocklistResponse as ActionSetWirelessBlocklistResponse,
    )
    from .action_remove_wireless_blocklist_response import (
        ActionRemoveWirelessBlocklistResponse as ActionRemoveWirelessBlocklistResponse,
    )
    from .action_set_private_wireless_gateway_response import (
        ActionSetPrivateWirelessGatewayResponse as ActionSetPrivateWirelessGatewayResponse,
    )
    from .action_remove_private_wireless_gateway_response import (
        ActionRemovePrivateWirelessGatewayResponse as ActionRemovePrivateWirelessGatewayResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "SimCardGroupAction":
        from .sim_card_group_action import SimCardGroupAction

        return SimCardGroupAction
    if name == "ActionRetrieveResponse":
        from .action_retrieve_response import ActionRetrieveResponse

        return ActionRetrieveResponse
    if name == "ActionRemovePrivateWirelessGatewayResponse":
        from .action_remove_private_wireless_gateway_response import ActionRemovePrivateWirelessGatewayResponse

        return ActionRemovePrivateWirelessGatewayResponse
    if name == "ActionRemoveWirelessBlocklistResponse":
        from .action_remove_wireless_blocklist_response import ActionRemoveWirelessBlocklistResponse

        return ActionRemoveWirelessBlocklistResponse
    if name == "ActionSetPrivateWirelessGatewayResponse":
        from .action_set_private_wireless_gateway_response import ActionSetPrivateWirelessGatewayResponse

        return ActionSetPrivateWirelessGatewayResponse
    if name == "ActionSetWirelessBlocklistResponse":
        from .action_set_wireless_blocklist_response import ActionSetWirelessBlocklistResponse

        return ActionSetWirelessBlocklistResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
