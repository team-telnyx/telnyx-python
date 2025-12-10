# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .interface_status import InterfaceStatus

__all__ = ["Interface"]


class Interface(BaseModel):
    name: Optional[str] = None
    """A user specified name for the interface."""

    network_id: Optional[str] = None
    """The id of the network associated with the interface."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""
