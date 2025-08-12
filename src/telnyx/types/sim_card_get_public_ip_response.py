# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SimCardGetPublicIPResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    ip: Optional[str] = None
    """The provisioned IP address.

    This attribute will only be available when underlying resource status is in a
    "provisioned" status.
    """

    record_type: Optional[str] = None

    region_code: Optional[str] = None

    sim_card_id: Optional[str] = None

    type: Optional[Literal["ipv4"]] = None

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class SimCardGetPublicIPResponse(BaseModel):
    data: Optional[Data] = None
