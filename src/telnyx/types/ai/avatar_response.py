# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .avatar import Avatar
from ..._models import BaseModel

__all__ = ["AvatarResponse"]


class AvatarResponse(BaseModel):
    data: Avatar
