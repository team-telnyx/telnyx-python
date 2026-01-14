# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["QueueListResponse"]


class QueueListResponse(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    average_wait_time: Optional[int] = None
    """The average wait time in seconds for members in the queue."""

    current_size: Optional[int] = None
    """The current number of members in the queue."""

    date_created: Optional[str] = None
    """The timestamp of when the resource was created."""

    date_updated: Optional[str] = None
    """The timestamp of when the resource was last updated."""

    max_size: Optional[int] = None
    """The maximum size of the queue."""

    sid: Optional[str] = None
    """The unique identifier of the queue."""

    subresource_uris: Optional[Dict[str, object]] = None
    """A list of related resources identified by their relative URIs."""

    uri: Optional[str] = None
    """The relative URI for this queue."""
