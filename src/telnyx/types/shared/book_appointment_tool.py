# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .book_appointment_tool_params import BookAppointmentToolParams

__all__ = ["BookAppointmentTool"]


class BookAppointmentTool(BaseModel):
    book_appointment: BookAppointmentToolParams

    type: Literal["book_appointment"]
