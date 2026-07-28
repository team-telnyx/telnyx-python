# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .email_pagination_meta import EmailPaginationMeta
from .inbound_thread_detail import InboundThreadDetail

__all__ = ["ThreadRetrieveResponse"]


class ThreadRetrieveResponse(BaseModel):
    data: InboundThreadDetail

    meta: EmailPaginationMeta
