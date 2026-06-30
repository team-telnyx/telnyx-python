# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...._models import BaseModel

if TYPE_CHECKING:
    from ..organization_user import OrganizationUser

__all__ = ["ActionRemoveResponse"]


class ActionRemoveResponse(BaseModel):
    data: Optional[OrganizationUser] = None
