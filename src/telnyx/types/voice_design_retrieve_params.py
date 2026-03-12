# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoiceDesignRetrieveParams"]


class VoiceDesignRetrieveParams(TypedDict, total=False):
    version: int
    """Specific version number to retrieve. Defaults to the latest version."""
