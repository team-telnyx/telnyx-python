# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .hangup_tool_params import HangupToolParams

__all__ = ["HangupTool"]


class HangupTool(BaseModel):
    hangup: HangupToolParams

    type: Literal["hangup"]
