# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel
from .version_config import VersionConfig

__all__ = ["CanaryDeployResponse"]


class CanaryDeployResponse(BaseModel):
    assistant_id: str

    created_at: datetime

    updated_at: datetime

    versions: List[VersionConfig]
