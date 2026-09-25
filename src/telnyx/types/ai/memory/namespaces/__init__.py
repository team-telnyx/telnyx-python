# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .profile_list_params import ProfileListParams as ProfileListParams
from .profile_ingest_params import ProfileIngestParams as ProfileIngestParams
from .profile_recall_params import ProfileRecallParams as ProfileRecallParams
from .profile_remember_params import ProfileRememberParams as ProfileRememberParams
from .setting_patch_all_params import SettingPatchAllParams as SettingPatchAllParams

if TYPE_CHECKING:
    from .page_meta import PageMeta as PageMeta
    from .profile_list_response import ProfileListResponse as ProfileListResponse
    from .profile_delete_response import ProfileDeleteResponse as ProfileDeleteResponse
    from .profile_ingest_response import ProfileIngestResponse as ProfileIngestResponse
    from .profile_recall_response import ProfileRecallResponse as ProfileRecallResponse
    from .profile_remember_response import ProfileRememberResponse as ProfileRememberResponse
    from .namespace_settings_response import NamespaceSettingsResponse as NamespaceSettingsResponse
    from .profile_retrieve_summary_response import ProfileRetrieveSummaryResponse as ProfileRetrieveSummaryResponse


def __getattr__(name: str) -> Any:
    if name == "PageMeta":
        from .page_meta import PageMeta

        return PageMeta
    if name == "ProfileListResponse":
        from .profile_list_response import ProfileListResponse

        return ProfileListResponse
    if name == "ProfileDeleteResponse":
        from .profile_delete_response import ProfileDeleteResponse

        return ProfileDeleteResponse
    if name == "ProfileIngestResponse":
        from .profile_ingest_response import ProfileIngestResponse

        return ProfileIngestResponse
    if name == "ProfileRecallResponse":
        from .profile_recall_response import ProfileRecallResponse

        return ProfileRecallResponse
    if name == "ProfileRememberResponse":
        from .profile_remember_response import ProfileRememberResponse

        return ProfileRememberResponse
    if name == "ProfileRetrieveSummaryResponse":
        from .profile_retrieve_summary_response import ProfileRetrieveSummaryResponse

        return ProfileRetrieveSummaryResponse
    if name == "NamespaceSettingsResponse":
        from .namespace_settings_response import NamespaceSettingsResponse

        return NamespaceSettingsResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
