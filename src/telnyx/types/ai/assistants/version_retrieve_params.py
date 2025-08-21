# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VersionRetrieveParams"]


class VersionRetrieveParams(TypedDict, total=False):
    assistant_id: Required[str]

    include_mcp_servers: bool
