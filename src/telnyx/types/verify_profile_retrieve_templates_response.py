# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .verify_profile_message_template_response import VerifyProfileMessageTemplateResponse

__all__ = ["VerifyProfileRetrieveTemplatesResponse"]


class VerifyProfileRetrieveTemplatesResponse(BaseModel):
    """A list of Verify profile message templates"""

    data: List[VerifyProfileMessageTemplateResponse]
