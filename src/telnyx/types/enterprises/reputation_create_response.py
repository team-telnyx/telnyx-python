# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .enterprise_reputation_public import EnterpriseReputationPublic

__all__ = ["ReputationCreateResponse"]


class ReputationCreateResponse(BaseModel):
    data: Optional[EnterpriseReputationPublic] = None
