# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["CallingRoutingPatchAllParams"]


class CallingRoutingPatchAllParams(TypedDict, total=False):
    connection_id: Required[Union[str, int, None]]
    """
    ID of the connection to deliver inbound WhatsApp calls to: a positive integer up
    to 9223372036854775807, sent as a decimal string or an integer. Send a string to
    keep large IDs exact. Non-null values are returned as strings. `null` clears the
    routing.
    """
