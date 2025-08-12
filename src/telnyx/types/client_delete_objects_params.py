# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientDeleteObjectsParams", "Body"]


class ClientDeleteObjectsParams(TypedDict, total=False):
    delete: Required[Literal[True]]

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    key: Annotated[str, PropertyInfo(alias="Key")]
