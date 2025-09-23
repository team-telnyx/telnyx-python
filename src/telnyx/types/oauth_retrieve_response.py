# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OAuthRetrieveResponse", "Data", "DataRequestedScope"]


class DataRequestedScope(BaseModel):
    id: Optional[str] = None
    """Scope ID"""

    description: Optional[str] = None
    """Scope description"""

    name: Optional[str] = None
    """Scope name"""


class Data(BaseModel):
    client_id: Optional[str] = None
    """Client ID"""

    logo_uri: Optional[str] = None
    """URL of the client logo"""

    name: Optional[str] = None
    """Client name"""

    policy_uri: Optional[str] = None
    """URL of the client's privacy policy"""

    redirect_uri: Optional[str] = None
    """The redirect URI for this authorization"""

    requested_scopes: Optional[List[DataRequestedScope]] = None

    tos_uri: Optional[str] = None
    """URL of the client's terms of service"""

    verified: Optional[bool] = None
    """Whether the client is verified"""


class OAuthRetrieveResponse(BaseModel):
    data: Optional[Data] = None
