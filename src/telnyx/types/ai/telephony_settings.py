# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TelephonySettings"]


class TelephonySettings(BaseModel):
    default_texml_app_id: Optional[str] = None
    """Default Texml App used for voice calls with your assistant.

    This will be created automatically on assistant creation.
    """

    supports_unauthenticated_web_calls: Optional[bool] = None
    """
    When enabled, allows users to interact with your AI assistant directly from your
    website without requiring authentication. This is required for FE widgets that
    work with assistants that have telephony enabled.
    """
