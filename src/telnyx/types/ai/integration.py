# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Integration"]


class Integration(BaseModel):
    id: str

    available_tools: List[str]

    description: str

    display_name: str

    logo_url: str

    name: str

    status: Literal["disconnected", "connected"]
