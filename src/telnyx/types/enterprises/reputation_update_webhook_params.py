# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReputationUpdateWebhookParams"]


class ReputationUpdateWebhookParams(TypedDict, total=False):
    webhook_url: Required[Optional[str]]
    """HTTPS URL on a publicly routable host.

    Send `null` to stop receiving number-ownership events.
    """
