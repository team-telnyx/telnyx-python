# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .authentication_provider import AuthenticationProvider

__all__ = ["AuthenticationProviderDeleteResponse"]


class AuthenticationProviderDeleteResponse(BaseModel):
    data: Optional[AuthenticationProvider] = None
