# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TexmlRecordingSubresourcesUris"]


class TexmlRecordingSubresourcesUris(BaseModel):
    """Subresources details for a recording if available."""

    transcriptions: Optional[str] = None
