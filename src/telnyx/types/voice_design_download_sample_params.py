# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoiceDesignDownloadSampleParams"]


class VoiceDesignDownloadSampleParams(TypedDict, total=False):
    version: int
    """Specific version number to download the sample for.

    Defaults to the latest version.
    """
