# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..migration_params import MigrationParams

__all__ = ["ActionStopResponse"]


class ActionStopResponse(BaseModel):
    data: Optional[MigrationParams] = None
