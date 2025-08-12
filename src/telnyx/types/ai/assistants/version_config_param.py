# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VersionConfigParam"]


class VersionConfigParam(TypedDict, total=False):
    percentage: Required[float]
    """Percentage of traffic for this version [1-99]"""

    version_id: Required[str]
    """Version ID string that references assistant_versions.version_id"""
