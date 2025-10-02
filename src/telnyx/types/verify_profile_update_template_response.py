# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .verify_profile_message_template_response import VerifyProfileMessageTemplateResponse

__all__ = ["VerifyProfileUpdateTemplateResponse"]


class VerifyProfileUpdateTemplateResponse(BaseModel):
    data: Optional[VerifyProfileMessageTemplateResponse] = None
