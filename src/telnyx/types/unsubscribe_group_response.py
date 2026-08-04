# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .unsubscribe_group import UnsubscribeGroup

__all__ = ["UnsubscribeGroupResponse"]


class UnsubscribeGroupResponse(BaseModel):
    data: UnsubscribeGroup
