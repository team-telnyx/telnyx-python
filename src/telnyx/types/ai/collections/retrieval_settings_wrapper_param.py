# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .retrieval_settings_param import RetrievalSettingsParam

__all__ = ["RetrievalSettingsWrapperParam"]


class RetrievalSettingsWrapperParam(TypedDict, total=False):
    retrieval: RetrievalSettingsParam
    """How documents are retrieved when searching the collection."""
