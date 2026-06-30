# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..messaging_profile import MessagingProfile

__all__ = ["ActionRegenerateSecretResponse"]


class ActionRegenerateSecretResponse(BaseModel):
    data: Optional[MessagingProfile] = None
