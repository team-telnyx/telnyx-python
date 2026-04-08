# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TexmlInitiateAICallResponse"]


class TexmlInitiateAICallResponse(BaseModel):
    call_sid: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    status: Optional[str] = None

    to: Optional[str] = None
