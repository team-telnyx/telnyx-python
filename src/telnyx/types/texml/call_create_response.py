# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CallCreateResponse"]


class CallCreateResponse(BaseModel):
    call_sid: str
    """The call control ID of the created call."""

    from_: str = FieldInfo(alias="from")
    """The caller address."""

    status: Literal["queued"]
    """The initial status of the outbound call."""

    to: str
    """The called address."""
