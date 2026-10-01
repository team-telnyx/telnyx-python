# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DirDeleteResponse", "Data"]


class Data(BaseModel):
    id: str
    """Id of the DIR whose deletion was requested."""

    status: Literal["delete_requested"]
    """
    Always `delete_requested`: the DIR has been queued for removal, not yet removed.
    """


class DirDeleteResponse(BaseModel):
    data: Data
