# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ToolPermissionCreateParams", "Server"]


class ToolPermissionCreateParams(TypedDict, total=False):
    instance_id: Required[str]

    servers: Required[Iterable[Server]]
    """The servers granted, each with its tools. `[]` grants none."""


class Server(TypedDict, total=False):
    id: Required[str]
    """An MCP server's or API's `id` on the instance."""

    tools: SequenceNotStr[str]
    """The tools the grant covers, by name without the server prefix.

    `[]` covers every tool the server exposes.
    """
