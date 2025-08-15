# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .conference_command_result import ConferenceCommandResult

__all__ = ["ActionSpeakResponse"]


class ActionSpeakResponse(BaseModel):
    data: Optional[ConferenceCommandResult] = None
