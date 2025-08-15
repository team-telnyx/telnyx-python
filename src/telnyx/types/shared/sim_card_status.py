# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SimCardStatus"]


class SimCardStatus(BaseModel):
    reason: Optional[str] = None
    """It describes why the SIM card is in the current status."""

    value: Optional[
        Literal[
            "registering",
            "enabling",
            "enabled",
            "disabling",
            "disabled",
            "data_limit_exceeded",
            "setting_standby",
            "standby",
        ]
    ] = None
    """The current status of the SIM card. It will be one of the following: <br/>

    <ul>
     <li><code>registering</code> - the card is being registered</li>
     <li><code>enabling</code> - the card is being enabled</li>
     <li><code>enabled</code> - the card is enabled and ready for use</li>
     <li><code>disabling</code> - the card is being disabled</li>
     <li><code>disabled</code> - the card has been disabled and cannot be used</li>
     <li><code>data_limit_exceeded</code> - the card has exceeded its data consumption limit</li>
     <li><code>setting_standby</code> - the process to set the card in stand by is in progress</li>
     <li><code>standby</code> - the card is in stand by</li>
    </ul>
    Transitioning between the enabled and disabled states may take a period of time.
    """
