# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientListObjectsParams"]


class ClientListObjectsParams(TypedDict, total=False):
    list_type: Annotated[Literal[2], PropertyInfo(alias="list-type")]
