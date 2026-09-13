# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessagingProfileFeatures"]


class MessagingProfileFeatures(BaseModel):
    """
    Telnyx product features the messaging customer can enable on the messaging profile. Keys map to individual feature flags; unknown keys are accepted and preserved for forward compatibility with rolling deployments.
    """

    ai_opt_out_detection_enabled: Optional[bool] = None
    """
    Enables AI detection of inbound opt-out messages that do not follow the standard
    STOP/UNSTOP/HELP opt-out keyword pattern. When enabled, the messaging platform
    applies an AI model to identify non-standard opt-out requests (e.g.
    natural-language phrases) and treats them as opt-outs.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
