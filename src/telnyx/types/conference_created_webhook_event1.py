# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_created import ConferenceCreated

__all__ = ["ConferenceCreatedWebhookEvent"]


class ConferenceCreatedWebhookEvent(BaseModel):
    data: Optional[ConferenceCreated] = None
