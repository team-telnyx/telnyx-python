# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .ip_pool_create_params import IPPoolCreateParams as IPPoolCreateParams
from .ip_pool_delete_params import IPPoolDeleteParams as IPPoolDeleteParams
from .ip_pool_update_params import IPPoolUpdateParams as IPPoolUpdateParams
from .dedicated_ip_list_params import DedicatedIPListParams as DedicatedIPListParams
from .dedicated_ip_create_params import DedicatedIPCreateParams as DedicatedIPCreateParams
from .dedicated_ip_delete_params import DedicatedIPDeleteParams as DedicatedIPDeleteParams
from .dedicated_ip_update_params import DedicatedIPUpdateParams as DedicatedIPUpdateParams

if TYPE_CHECKING:
    from .ip_pool import IPPool as IPPool
    from .dedicated_ip import DedicatedIP as DedicatedIP
    from .ip_pool_list_response import IPPoolListResponse as IPPoolListResponse
    from .ip_pool_show_response import IPPoolShowResponse as IPPoolShowResponse
    from .dedicated_ip_list_response import DedicatedIPListResponse as DedicatedIPListResponse
    from .dedicated_ip_show_response import DedicatedIPShowResponse as DedicatedIPShowResponse


def __getattr__(name: str) -> Any:
    if name == "DedicatedIP":
        from .dedicated_ip import DedicatedIP

        return DedicatedIP
    if name == "DedicatedIPShowResponse":
        from .dedicated_ip_show_response import DedicatedIPShowResponse

        return DedicatedIPShowResponse
    if name == "DedicatedIPListResponse":
        from .dedicated_ip_list_response import DedicatedIPListResponse

        return DedicatedIPListResponse
    if name == "IPPool":
        from .ip_pool import IPPool

        return IPPool
    if name == "IPPoolShowResponse":
        from .ip_pool_show_response import IPPoolShowResponse

        return IPPoolShowResponse
    if name == "IPPoolListResponse":
        from .ip_pool_list_response import IPPoolListResponse

        return IPPoolListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
