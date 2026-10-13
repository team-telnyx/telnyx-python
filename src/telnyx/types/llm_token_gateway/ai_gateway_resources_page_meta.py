# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["AIGatewayResourcesPageMeta"]


class AIGatewayResourcesPageMeta(BaseModel):
    has_more: bool

    page_number: int

    page_size: int

    snapshot: str
