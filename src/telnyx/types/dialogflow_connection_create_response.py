# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DialogflowConnectionCreateResponse", "Data"]


class Data(BaseModel):
    connection_id: Optional[str] = None
    """Uniquely identifies a Telnyx application (Call Control)."""

    conversation_profile_id: Optional[str] = None
    """The id of a configured conversation profile on your Dialogflow account.

    (If you use Dialogflow CX, this param is required)
    """

    environment: Optional[str] = None
    """Which Dialogflow environment will be used."""

    record_type: Optional[str] = None

    service_account: Optional[str] = None
    """The JSON map to connect your Dialoglow account."""


class DialogflowConnectionCreateResponse(BaseModel):
    data: Data
