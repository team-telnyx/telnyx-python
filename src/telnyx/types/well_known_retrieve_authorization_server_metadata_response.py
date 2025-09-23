# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WellKnownRetrieveAuthorizationServerMetadataResponse"]


class WellKnownRetrieveAuthorizationServerMetadataResponse(BaseModel):
    authorization_endpoint: Optional[str] = None
    """Authorization endpoint URL"""

    code_challenge_methods_supported: Optional[List[str]] = None
    """Supported PKCE code challenge methods"""

    grant_types_supported: Optional[List[str]] = None
    """Supported grant types"""

    introspection_endpoint: Optional[str] = None
    """Token introspection endpoint URL"""

    issuer: Optional[str] = None
    """Authorization server issuer URL"""

    jwks_uri: Optional[str] = None
    """JWK Set endpoint URL"""

    registration_endpoint: Optional[str] = None
    """Dynamic client registration endpoint URL"""

    response_types_supported: Optional[List[str]] = None
    """Supported response types"""

    scopes_supported: Optional[List[str]] = None
    """Supported OAuth scopes"""

    token_endpoint: Optional[str] = None
    """Token endpoint URL"""

    token_endpoint_auth_methods_supported: Optional[List[str]] = None
    """Supported token endpoint authentication methods"""
