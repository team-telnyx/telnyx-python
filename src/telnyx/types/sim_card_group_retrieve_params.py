# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimCardGroupRetrieveParams"]


class SimCardGroupRetrieveParams(TypedDict, total=False):
    include_iccids: bool
    """It includes a list of associated ICCIDs."""
