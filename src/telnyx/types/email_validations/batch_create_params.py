# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    emails: Required[SequenceNotStr[str]]

    webhook_url: str
    """URL for batch completion webhook.

    Empty string is treated as omitted. SSRF-protected; private/reserved IPs and
    internal hostnames are rejected.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
