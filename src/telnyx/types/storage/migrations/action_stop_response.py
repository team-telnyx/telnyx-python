# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...._models import BaseModel

if TYPE_CHECKING:
    from ..migration_params import MigrationParams

__all__ = ["ActionStopResponse"]


class ActionStopResponse(BaseModel):
    data: Optional[MigrationParams] = None
