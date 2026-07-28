# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .inbound_thread import InboundThread
from .thread_message import ThreadMessage

__all__ = ["InboundThreadDetail"]


class InboundThreadDetail(InboundThread):
    messages: List[ThreadMessage]
