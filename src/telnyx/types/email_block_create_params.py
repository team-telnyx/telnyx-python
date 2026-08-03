# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailBlockCreateParams"]


class EmailBlockCreateParams(TypedDict, total=False):
    to: Required[str]
    """Recipient address (normalized: trim + lower-case)."""

    domain_id: Optional[str]
    """`null` ⇒ account scope."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]
    """Sender address (normalized). `null` ⇒ account/domain scope."""
