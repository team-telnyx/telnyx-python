# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..shared.messaging_hosted_number_order import MessagingHostedNumberOrder

__all__ = ["ActionUploadFileResponse"]


class ActionUploadFileResponse(BaseModel):
    data: Optional[MessagingHostedNumberOrder] = None
