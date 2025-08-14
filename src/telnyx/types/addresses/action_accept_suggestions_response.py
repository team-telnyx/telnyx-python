# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionAcceptSuggestionsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The UUID of the location."""

    accepted: Optional[bool] = None
    """Indicates if the address suggestions are accepted."""

    record_type: Optional[Literal["address_suggestion"]] = None


class ActionAcceptSuggestionsResponse(BaseModel):
    data: Optional[Data] = None
