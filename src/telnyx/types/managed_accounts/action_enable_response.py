# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..managed_account import ManagedAccount

__all__ = ["ActionEnableResponse"]


class ActionEnableResponse(BaseModel):
    data: Optional[ManagedAccount] = None
