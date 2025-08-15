# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .integration_secret import IntegrationSecret

__all__ = ["IntegrationSecretListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class IntegrationSecretListResponse(BaseModel):
    data: List[IntegrationSecret]

    meta: Meta
