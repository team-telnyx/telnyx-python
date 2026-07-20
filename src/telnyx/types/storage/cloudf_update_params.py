# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CloudfUpdateParams"]


class CloudfUpdateParams(TypedDict, total=False):
    name: str
    """New filesystem name, unique within your organization.

    Names are trimmed and lowercased; after normalization they may contain lowercase
    letters, numbers, `.`, `_`, and `-` only.
    """
