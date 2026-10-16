# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HostedSignupCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Hosted signup ID"""

    app_id: Optional[str] = None
    """Meta App ID the hosted signup onboards customers into"""

    created_at: Optional[datetime] = None

    expires_at: Optional[datetime] = None
    """When the onboarding URL stops working"""

    jwt: Optional[str] = None
    """Signed token embedded in `url`"""

    record_type: Optional[Literal["whatsapp_jwt"]] = None

    solution_id: Optional[str] = None
    """Meta Partner Solution ID linked to the app.

    Returned only when creating a hosted signup.
    """

    url: Optional[str] = None
    """Hosted onboarding URL to share with the end customer"""


class HostedSignupCreateResponse(BaseModel):
    data: Optional[Data] = None
