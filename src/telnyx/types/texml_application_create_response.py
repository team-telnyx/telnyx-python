# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .texml_application import TexmlApplication

__all__ = ["TexmlApplicationCreateResponse"]


class TexmlApplicationCreateResponse(BaseModel):
    data: Optional[TexmlApplication] = None
