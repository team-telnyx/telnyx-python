# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..wireless_error import WirelessError
    from ..shared.simple_sim_card import SimpleSimCard

__all__ = ["RegisterCreateResponse"]


class RegisterCreateResponse(BaseModel):
    data: Optional[List[SimpleSimCard]] = None
    """Successfully registered SIM cards."""

    errors: Optional[List[WirelessError]] = None
