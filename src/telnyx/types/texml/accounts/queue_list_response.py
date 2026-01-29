# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["QueueListResponse", "Queue"]


class Queue(BaseModel):
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


class QueueListResponse(BaseModel):
    end: Optional[int] = None
    """The number of the last element on the page, zero-indexed."""

    first_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Queues.json?Page=0&PageSize=1
    """

    next_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Queues.json?Page=1&PageSize=1&PageToken=MTY4AjgyNDkwNzIxMQ
    """

    page: Optional[int] = None
    """Current page number, zero-indexed."""

    page_size: Optional[int] = None
    """The number of items on the page"""

    queues: Optional[List[Queue]] = None

    start: Optional[int] = None
    """The number of the first element on the page, zero-indexed."""

    uri: Optional[str] = None
    """The URI of the current page."""
