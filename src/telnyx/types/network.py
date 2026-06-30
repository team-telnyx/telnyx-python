# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .record import Record

__all__ = ["Network"]


class Network(Record):
    name: Optional[str] = None
    """A user specified name for the network."""
