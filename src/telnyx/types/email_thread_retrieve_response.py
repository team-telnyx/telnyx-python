# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .email_inboxes.email_pagination_meta import EmailPaginationMeta
from .email_inboxes.inbound_thread_detail import InboundThreadDetail

__all__ = ["EmailThreadRetrieveResponse"]


class EmailThreadRetrieveResponse(BaseModel):
    data: InboundThreadDetail

    meta: EmailPaginationMeta
