# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel
from .namespace_settings import NamespaceSettings

__all__ = ["NamespaceSettingsResponse"]


class NamespaceSettingsResponse(BaseModel):
    data: NamespaceSettings
    """A namespace's settings, grouped by what they affect."""
