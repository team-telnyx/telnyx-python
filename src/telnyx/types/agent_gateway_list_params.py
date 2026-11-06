# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentGatewayListParams"]


class AgentGatewayListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page to return, counting from 1."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Results per page."""
