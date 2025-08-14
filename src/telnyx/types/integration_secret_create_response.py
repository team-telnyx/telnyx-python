# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .integration_secret import IntegrationSecret

__all__ = ["IntegrationSecretCreateResponse"]


class IntegrationSecretCreateResponse(BaseModel):
    data: IntegrationSecret
