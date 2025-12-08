# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InterruptionSettingsParam"]


class InterruptionSettingsParam(TypedDict, total=False):
    """Settings for handling user interruptions during assistant speech"""

    enable: bool
    """When true, allows users to interrupt the assistant while speaking"""
