# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OAuthGrant"]


class OAuthGrant(BaseModel):
    id: str
    """Unique identifier for the OAuth grant"""

    client_id: str
    """OAuth client identifier"""

    created_at: datetime
    """Timestamp when the grant was created"""

    record_type: Literal["oauth_grant"]
    """Record type identifier"""

    scopes: List[str]
    """List of granted OAuth scopes"""

    last_used_at: Optional[datetime] = None
    """Timestamp when the grant was last used"""
