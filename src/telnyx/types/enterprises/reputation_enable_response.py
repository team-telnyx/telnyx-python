# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .enterprise_reputation_public import EnterpriseReputationPublic

__all__ = ["ReputationEnableResponse"]


class ReputationEnableResponse(BaseModel):
    data: EnterpriseReputationPublic
