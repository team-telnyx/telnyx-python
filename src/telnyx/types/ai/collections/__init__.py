# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .source_type import SourceType as SourceType
from .source_create_params import SourceCreateParams as SourceCreateParams
from .source_request_param import SourceRequestParam as SourceRequestParam
from .setting_create_params import SettingCreateParams as SettingCreateParams
from .source_replace_params import SourceReplaceParams as SourceReplaceParams
from .retrieval_settings_param import RetrievalSettingsParam as RetrievalSettingsParam
from .setting_patch_all_params import SettingPatchAllParams as SettingPatchAllParams
from .retrieval_settings_wrapper_param import RetrievalSettingsWrapperParam as RetrievalSettingsWrapperParam

if TYPE_CHECKING:
    from .source import Source as Source
    from .settings_envelope import SettingsEnvelope as SettingsEnvelope
    from .retrieval_settings import RetrievalSettings as RetrievalSettings
    from .source_list_response import SourceListResponse as SourceListResponse
    from .source_create_response import SourceCreateResponse as SourceCreateResponse
    from .source_replace_response import SourceReplaceResponse as SourceReplaceResponse
    from .retrieval_settings_wrapper import RetrievalSettingsWrapper as RetrievalSettingsWrapper


def __getattr__(name: str) -> Any:
    if name == "RetrievalSettings":
        from .retrieval_settings import RetrievalSettings

        return RetrievalSettings
    if name == "RetrievalSettingsWrapper":
        from .retrieval_settings_wrapper import RetrievalSettingsWrapper

        return RetrievalSettingsWrapper
    if name == "SettingsEnvelope":
        from .settings_envelope import SettingsEnvelope

        return SettingsEnvelope
    if name == "Source":
        from .source import Source

        return Source
    if name == "SourceCreateResponse":
        from .source_create_response import SourceCreateResponse

        return SourceCreateResponse
    if name == "SourceListResponse":
        from .source_list_response import SourceListResponse

        return SourceListResponse
    if name == "SourceReplaceResponse":
        from .source_replace_response import SourceReplaceResponse

        return SourceReplaceResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
