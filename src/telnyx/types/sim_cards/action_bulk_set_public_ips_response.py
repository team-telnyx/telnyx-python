# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionBulkSetPublicIPsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    action_type: Optional[Literal["bulk_set_public_ips"]] = None
    """The operation type. It can be one of the following: <br/>

    <ul>
    <li><code>bulk_set_public_ips</code> - set a public IP for each specified SIM card.</li>
    </ul>
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    settings: Optional[Dict[str, object]] = None
    """A JSON object representation of the bulk action payload."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class ActionBulkSetPublicIPsResponse(BaseModel):
    data: Optional[Data] = None
    """This object represents a bulk SIM card action.

    It groups SIM card actions created through a bulk endpoint under a single
    resource for further lookup.
    """
