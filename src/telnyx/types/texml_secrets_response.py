# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TexmlSecretsResponse", "Data"]


class Data(BaseModel):
    name: Optional[str] = None

    value: Optional[Literal["REDACTED"]] = None


class TexmlSecretsResponse(BaseModel):
    data: Optional[Data] = None
