# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Observability"]


class Observability(BaseModel):
    host: Optional[str] = None

    public_key_ref: Optional[str] = None

    secret_key_ref: Optional[str] = None

    status: Optional[Literal["enabled", "disabled"]] = None
