# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DialogflowConnectionUpdateParams"]


class DialogflowConnectionUpdateParams(TypedDict, total=False):
    service_account: Required[Dict[str, object]]
    """The JSON map to connect your Dialoglow account."""

    conversation_profile_id: str
    """The id of a configured conversation profile on your Dialogflow account.

    (If you use Dialogflow CX, this param is required)
    """

    dialogflow_api: Literal["cx", "es"]
    """Determine which Dialogflow will be used."""

    environment: str
    """Which Dialogflow environment will be used."""

    location: str
    """The region of your agent is. (If you use Dialogflow CX, this param is required)"""
