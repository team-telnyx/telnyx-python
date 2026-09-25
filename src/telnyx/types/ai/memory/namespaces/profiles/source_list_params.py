# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["SourceListParams"]


class SourceListParams(TypedDict, total=False):
    namespace: Required[str]

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page to return, counting from 1.

    Bounded in depth: (page[number] - 1) \\** page[size] may be at most 10000.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """How many results a page holds."""

    session_id: Optional[str]
    """An ingested session, by the `session_id` it was ingested with.

    Narrows the request to the source that session was stored as.
    """
