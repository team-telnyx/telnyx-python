# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .label_create_params import LabelCreateParams as LabelCreateParams
from .label_delete_all_params import LabelDeleteAllParams as LabelDeleteAllParams

if TYPE_CHECKING:
    from .label_create_response import LabelCreateResponse as LabelCreateResponse
    from .label_delete_all_response import LabelDeleteAllResponse as LabelDeleteAllResponse


def __getattr__(name: str) -> Any:
    if name == "LabelCreateResponse":
        from .label_create_response import LabelCreateResponse

        return LabelCreateResponse
    if name == "LabelDeleteAllResponse":
        from .label_delete_all_response import LabelDeleteAllResponse

        return LabelDeleteAllResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
