# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .migration_source_params import MigrationSourceParams

__all__ = ["MigrationSourceCreateResponse"]


class MigrationSourceCreateResponse(BaseModel):
    data: Optional[MigrationSourceParams] = None
