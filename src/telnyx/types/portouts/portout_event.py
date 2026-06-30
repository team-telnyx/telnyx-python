# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .webhook_portout_new_comment import WebhookPortoutNewComment
from .webhook_portout_status_changed import WebhookPortoutStatusChanged
from .webhook_portout_foc_date_changed import WebhookPortoutFocDateChanged

__all__ = ["PortoutEvent"]

PortoutEvent: TypeAlias = Union[WebhookPortoutStatusChanged, WebhookPortoutNewComment, WebhookPortoutFocDateChanged]
