# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .version_config_param import VersionConfigParam

__all__ = ["CanaryDeployUpdateParams"]


class CanaryDeployUpdateParams(TypedDict, total=False):
    versions: Required[Iterable[VersionConfigParam]]
    """List of version configurations"""
