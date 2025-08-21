# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionSetPublicIPParams"]


class ActionSetPublicIPParams(TypedDict, total=False):
    region_code: str
    """The code of the region where the public IP should be assigned.

    A list of available regions can be found at the regions endpoint
    """
