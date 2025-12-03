# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .campaign_suspended_event import CampaignSuspendedEvent
from .campaign_status_update_event import CampaignStatusUpdateEvent

__all__ = ["CampaignStatusUpdateWebhookEvent"]

CampaignStatusUpdateWebhookEvent: TypeAlias = Union[CampaignStatusUpdateEvent, CampaignSuspendedEvent]
