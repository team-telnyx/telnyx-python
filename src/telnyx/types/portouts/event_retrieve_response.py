# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .webhook_portout_new_comment import WebhookPortoutNewComment
from .webhook_portout_status_changed import WebhookPortoutStatusChanged
from .webhook_portout_foc_date_changed import WebhookPortoutFocDateChanged

__all__ = ["EventRetrieveResponse", "Data"]

Data: TypeAlias = Union[WebhookPortoutStatusChanged, WebhookPortoutNewComment, WebhookPortoutFocDateChanged]


class EventRetrieveResponse(BaseModel):
    data: Optional[Data] = None
