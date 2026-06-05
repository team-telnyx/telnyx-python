# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .enterprise_public import EnterprisePublic

__all__ = ["EnterpriseUpdateResponse"]


class EnterpriseUpdateResponse(BaseModel):
    data: EnterprisePublic
