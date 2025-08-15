# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SimCardAction", "Status"]


class Status(BaseModel):
    reason: Optional[str] = None
    """It describes why the SIM card action is in the current status.

    This will be <code>null</code> for self-explanatory statuses, such as
    <code>in-progress</code> and <code>completed</code> but will include further
    information on statuses like <code>interrupted</code> and <code>failed</code>.
    """

    value: Optional[Literal["in-progress", "completed", "failed", "interrupted"]] = None
    """The current status of the SIM card action."""


class SimCardAction(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    action_type: Optional[Literal["enable", "enable_standby_sim_card", "disable", "set_standby"]] = None
    """The operation type. It can be one of the following: <br/>

    <ul>
     <li><code>enable</code> - move the SIM card to the <code>enabled</code> status</li>
     <li><code>enable_standby_sim_card</code> - move a SIM card previously on the <code>standby</code> status to the <code>enabled</code> status after it consumes data.</li>
     <li><code>disable</code> - move the SIM card to the <code>disabled</code> status</li>
     <li><code>set_standby</code> - move the SIM card to the <code>standby</code> status</li>
     </ul>
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    settings: Optional[Dict[str, object]] = None
    """A JSON object representation of the action params."""

    sim_card_id: Optional[str] = None
    """The related SIM card identifier."""

    status: Optional[Status] = None

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""
