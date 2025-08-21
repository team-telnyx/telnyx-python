# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["HangupToolParams"]


class HangupToolParams(BaseModel):
    description: Optional[str] = None
    """The description of the function that will be passed to the assistant."""
