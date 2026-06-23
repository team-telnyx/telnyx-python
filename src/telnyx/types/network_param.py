# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .record_param import RecordParam

__all__ = ["NetworkParam"]


class NetworkParam(RecordParam, total=False):
    name: str
    """A user specified name for the network."""
