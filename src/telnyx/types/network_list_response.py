# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record

__all__ = ["NetworkListResponse"]


class NetworkListResponse(Record):
    name: Optional[str] = None
    """A user specified name for the network."""
