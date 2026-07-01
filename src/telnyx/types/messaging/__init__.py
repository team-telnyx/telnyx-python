# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .rc_list_bulk_capabilities_params import RcListBulkCapabilitiesParams as RcListBulkCapabilitiesParams

if TYPE_CHECKING:
    from .rcs_capabilities import RcsCapabilities as RcsCapabilities
    from .rc_invite_test_number_response import RcInviteTestNumberResponse as RcInviteTestNumberResponse
    from .rc_retrieve_capabilities_response import RcRetrieveCapabilitiesResponse as RcRetrieveCapabilitiesResponse
    from .rc_list_bulk_capabilities_response import RcListBulkCapabilitiesResponse as RcListBulkCapabilitiesResponse


def __getattr__(name: str) -> Any:
    if name == "RcsCapabilities":
        from .rcs_capabilities import RcsCapabilities

        return RcsCapabilities
    if name == "RcInviteTestNumberResponse":
        from .rc_invite_test_number_response import RcInviteTestNumberResponse

        return RcInviteTestNumberResponse
    if name == "RcListBulkCapabilitiesResponse":
        from .rc_list_bulk_capabilities_response import RcListBulkCapabilitiesResponse

        return RcListBulkCapabilitiesResponse
    if name == "RcRetrieveCapabilitiesResponse":
        from .rc_retrieve_capabilities_response import RcRetrieveCapabilitiesResponse

        return RcRetrieveCapabilitiesResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
