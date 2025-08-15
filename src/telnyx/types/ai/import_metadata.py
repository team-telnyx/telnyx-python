# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ImportMetadata"]


class ImportMetadata(BaseModel):
    import_id: Optional[str] = None
    """ID of the assistant in the provider's system."""

    import_provider: Optional[Literal["elevenlabs", "vapi"]] = None
    """Provider the assistant was imported from."""
