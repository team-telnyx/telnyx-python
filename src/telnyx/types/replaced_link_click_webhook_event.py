# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .replaced_link_click import ReplacedLinkClick

__all__ = ["ReplacedLinkClickWebhookEvent"]


class ReplacedLinkClickWebhookEvent(BaseModel):
    data: Optional[ReplacedLinkClick] = None
