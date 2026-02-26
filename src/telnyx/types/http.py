# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["HTTP", "Request", "Response"]


class Request(BaseModel):
    """Request details."""

    headers: Optional[List[List[str]]] = None
    """List of headers, limited to 10kB."""

    url: Optional[str] = None


class Response(BaseModel):
    """Response details, optional."""

    body: Optional[str] = None
    """Raw response body, limited to 10kB."""

    headers: Optional[List[List[str]]] = None
    """List of headers, limited to 10kB."""

    status: Optional[int] = None


class HTTP(BaseModel):
    """HTTP request and response information."""

    request: Optional[Request] = None
    """Request details."""

    response: Optional[Response] = None
    """Response details, optional."""
