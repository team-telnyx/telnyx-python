# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .migration_params import MigrationParams

__all__ = ["MigrationCreateResponse"]


class MigrationCreateResponse(BaseModel):
    data: Optional[MigrationParams] = None
