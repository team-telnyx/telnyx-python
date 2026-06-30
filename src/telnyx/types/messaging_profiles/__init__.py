# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .autoresp_config_list_params import AutorespConfigListParams as AutorespConfigListParams
from .autoresp_config_create_params import AutorespConfigCreateParams as AutorespConfigCreateParams
from .autoresp_config_update_params import AutorespConfigUpdateParams as AutorespConfigUpdateParams
from .autoresp_config_delete_response import AutorespConfigDeleteResponse as AutorespConfigDeleteResponse

if TYPE_CHECKING:
    from .auto_resp_config import AutoRespConfig as AutoRespConfig
    from .auto_resp_config_response import AutoRespConfigResponse as AutoRespConfigResponse
    from .autoresp_config_list_response import AutorespConfigListResponse as AutorespConfigListResponse
    from .action_regenerate_secret_response import ActionRegenerateSecretResponse as ActionRegenerateSecretResponse


def __getattr__(name: str) -> Any:
    if name == "AutoRespConfig":
        from .auto_resp_config import AutoRespConfig

        return AutoRespConfig
    if name == "AutoRespConfigResponse":
        from .auto_resp_config_response import AutoRespConfigResponse

        return AutoRespConfigResponse
    if name == "AutorespConfigListResponse":
        from .autoresp_config_list_response import AutorespConfigListResponse

        return AutorespConfigListResponse
    if name == "ActionRegenerateSecretResponse":
        from .action_regenerate_secret_response import ActionRegenerateSecretResponse

        return ActionRegenerateSecretResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
