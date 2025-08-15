# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .external_connection_phone_number import ExternalConnectionPhoneNumber
from ..external_voice_integrations_pagination_meta import ExternalVoiceIntegrationsPaginationMeta

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
    data: Optional[List[ExternalConnectionPhoneNumber]] = None

    meta: Optional[ExternalVoiceIntegrationsPaginationMeta] = None
