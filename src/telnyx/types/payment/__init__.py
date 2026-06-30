# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .auto_recharge_pref_update_params import AutoRechargePrefUpdateParams as AutoRechargePrefUpdateParams

if TYPE_CHECKING:
    from .auto_recharge_pref import AutoRechargePref as AutoRechargePref
    from .auto_recharge_pref_list_response import AutoRechargePrefListResponse as AutoRechargePrefListResponse
    from .auto_recharge_pref_update_response import AutoRechargePrefUpdateResponse as AutoRechargePrefUpdateResponse


def __getattr__(name: str) -> Any:
    if name == "AutoRechargePref":
        from .auto_recharge_pref import AutoRechargePref

        return AutoRechargePref
    if name == "AutoRechargePrefUpdateResponse":
        from .auto_recharge_pref_update_response import AutoRechargePrefUpdateResponse

        return AutoRechargePrefUpdateResponse
    if name == "AutoRechargePrefListResponse":
        from .auto_recharge_pref_list_response import AutoRechargePrefListResponse

        return AutoRechargePrefListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
