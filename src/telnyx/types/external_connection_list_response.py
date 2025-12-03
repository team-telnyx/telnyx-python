# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .external_connection import ExternalConnection
from .external_voice_integrations_pagination_meta import ExternalVoiceIntegrationsPaginationMeta

__all__ = ["ExternalConnectionListResponse"]


class ExternalConnectionListResponse(BaseModel):
    data: Optional[List[ExternalConnection]] = None

    meta: Optional[ExternalVoiceIntegrationsPaginationMeta] = None
