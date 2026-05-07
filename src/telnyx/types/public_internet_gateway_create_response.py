# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .public_internet_gateway_read import PublicInternetGatewayRead

__all__ = ["PublicInternetGatewayCreateResponse"]


class PublicInternetGatewayCreateResponse(BaseModel):
    data: Optional[PublicInternetGatewayRead] = None
