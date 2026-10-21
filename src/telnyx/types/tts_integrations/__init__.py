# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_test_connection_params import ActionTestConnectionParams as ActionTestConnectionParams

if TYPE_CHECKING:
    from .community_tts_conformance_run import CommunityTtsConformanceRun as CommunityTtsConformanceRun


def __getattr__(name: str) -> Any:
    if name == "CommunityTtsConformanceRun":
        from .community_tts_conformance_run import CommunityTtsConformanceRun

        return CommunityTtsConformanceRun
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
