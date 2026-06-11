# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssistantRetrieveParams"]


class AssistantRetrieveParams(TypedDict, total=False):
    call_control_id: str
    """Filter results by call control id."""

    fetch_dynamic_variables_from_webhook: bool
    """Whether to fetch dynamic variables from the configured webhook."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Start of the filter range."""

    to: str
    """End of the filter range."""
