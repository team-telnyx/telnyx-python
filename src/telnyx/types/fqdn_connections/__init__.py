# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .fqdn_authentication_patch_all_params import FqdnAuthenticationPatchAllParams as FqdnAuthenticationPatchAllParams

if TYPE_CHECKING:
    from .fqdn_authentication import FqdnAuthentication as FqdnAuthentication
    from .fqdn_authentication_list_response import FqdnAuthenticationListResponse as FqdnAuthenticationListResponse
    from .fqdn_authentication_patch_all_response import (
        FqdnAuthenticationPatchAllResponse as FqdnAuthenticationPatchAllResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "FqdnAuthentication":
        from .fqdn_authentication import FqdnAuthentication

        return FqdnAuthentication
    if name == "FqdnAuthenticationListResponse":
        from .fqdn_authentication_list_response import FqdnAuthenticationListResponse

        return FqdnAuthenticationListResponse
    if name == "FqdnAuthenticationPatchAllResponse":
        from .fqdn_authentication_patch_all_response import FqdnAuthenticationPatchAllResponse

        return FqdnAuthenticationPatchAllResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
