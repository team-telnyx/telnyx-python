# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .email_inboxes.thread_message import ThreadMessage

__all__ = ["InboundMessage"]


class InboundMessage(ThreadMessage):
    direction: Optional[Literal["inbound"]] = None  # type: ignore

    status: Optional[Literal["received"]] = None  # type: ignore
