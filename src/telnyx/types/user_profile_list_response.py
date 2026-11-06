# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .user_profile import UserProfile

__all__ = ["UserProfileListResponse"]


class UserProfileListResponse(BaseModel):
    data: UserProfile
    """The authenticated user's profile."""
