# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["EmailEventType"]

EmailEventType: TypeAlias = Literal[
    "queued",
    "deferred",
    "scheduled",
    "cancelled",
    "sandbox",
    "sending",
    "sent",
    "failed",
    "delivered",
    "bounced",
    "complained",
    "rejected",
    "opened",
    "clicked",
    "unsubscribed",
    "daily_limit_exceeded",
]
