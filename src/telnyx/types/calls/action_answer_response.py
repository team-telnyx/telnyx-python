# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionAnswerResponse", "Data"]


class Data(BaseModel):
    recording_id: Optional[str] = None
    """The ID of the recording.

    Only present when the record parameter is set to record-from-answer.
    """

    result: Optional[str] = None


class ActionAnswerResponse(BaseModel):
    data: Optional[Data] = None
