# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BookAppointmentTool"]


class BookAppointmentTool(TypedDict, total=False):
    book_appointment: Required["BookAppointmentToolParams"]

    type: Required[Literal["book_appointment"]]


from .book_appointment_tool_params import BookAppointmentToolParams
