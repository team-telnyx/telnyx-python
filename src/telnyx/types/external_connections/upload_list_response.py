# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .upload import Upload
from ..._models import BaseModel
from ..external_voice_integrations_pagination_meta import ExternalVoiceIntegrationsPaginationMeta

__all__ = ["UploadListResponse"]


class UploadListResponse(BaseModel):
    data: Optional[List[Upload]] = None

    meta: Optional[ExternalVoiceIntegrationsPaginationMeta] = None
