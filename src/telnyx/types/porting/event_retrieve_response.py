# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .porting_event_split_event import PortingEventSplitEvent
from .porting_event_deleted_payload import PortingEventDeletedPayload
from .porting_event_without_webhook import PortingEventWithoutWebhook
from .porting_event_new_comment_event import PortingEventNewCommentEvent
from .porting_event_status_changed_event import PortingEventStatusChangedEvent
from .porting_event_messaging_changed_payload import PortingEventMessagingChangedPayload

__all__ = ["EventRetrieveResponse", "Data"]

Data: TypeAlias = Union[
    PortingEventDeletedPayload,
    PortingEventMessagingChangedPayload,
    PortingEventStatusChangedEvent,
    PortingEventNewCommentEvent,
    PortingEventSplitEvent,
    PortingEventWithoutWebhook,
]


class EventRetrieveResponse(BaseModel):
    data: Optional[Data] = None
