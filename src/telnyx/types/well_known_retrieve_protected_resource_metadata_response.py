# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WellKnownRetrieveProtectedResourceMetadataResponse"]


class WellKnownRetrieveProtectedResourceMetadataResponse(BaseModel):
    authorization_servers: Optional[List[str]] = None
    """List of authorization server URLs"""

    resource: Optional[str] = None
    """Protected resource URL"""
