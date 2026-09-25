# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page to return, counting from 1.

    Bounded in depth: (page[number] - 1) \\** page[size] may be at most 10000.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """How many results a page holds."""
