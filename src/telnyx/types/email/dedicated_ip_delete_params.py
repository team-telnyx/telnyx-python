# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DedicatedIPDeleteParams"]


class DedicatedIPDeleteParams(TypedDict, total=False):
    query_drain: Annotated[bool, PropertyInfo(alias="drain")]
    """Set together with `force=true` to release the last IP in a pool.

    Acknowledges that mail routed to the emptied pool is held until the pool has a
    sendable IP again. Also accepted in the JSON body.
    """

    query_force: Annotated[bool, PropertyInfo(alias="force")]
    """Set together with `drain=true` to release the last IP in a pool.

    Either flag alone has no effect. Also accepted in the JSON body.
    """

    query_reason: Annotated[str, PropertyInfo(alias="reason")]
    """Free-text reason recorded with the release. Also accepted in the JSON body."""

    body_drain: Annotated[bool, PropertyInfo(alias="drain")]
    """Set together with `force: true` to release the last IP in a pool.

    Acknowledges that mail routed to the emptied pool is held until the pool has a
    sendable IP again.
    """

    body_force: Annotated[bool, PropertyInfo(alias="force")]
    """Set together with `drain: true` to release the last IP in a pool.

    Either flag alone has no effect.
    """

    body_reason: Annotated[str, PropertyInfo(alias="reason")]
    """Free-text reason recorded with the release."""
