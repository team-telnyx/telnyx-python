# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["EmailWebhookEvent"]

EmailWebhookEvent: TypeAlias = Literal[
    "email.scheduled",
    "email.sandbox",
    "email.queued",
    "email.sending",
    "email.sent",
    "email.delivered",
    "email.deferred",
    "email.bounced",
    "email.failed",
    "email.complained",
    "email.opened",
    "email.clicked",
    "email.unsubscribed",
    "email.received",
    "email_domain.created",
    "email_domain.verified",
    "email_domain.degraded",
    "email_domain.suspended",
    "email_domain.deleted",
]
