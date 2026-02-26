# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .organization_user import OrganizationUser

__all__ = ["UserRetrieveResponse"]


class UserRetrieveResponse(BaseModel):
    data: Optional[OrganizationUser] = None
