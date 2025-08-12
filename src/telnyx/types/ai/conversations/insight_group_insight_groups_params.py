# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InsightGroupInsightGroupsParams"]


class InsightGroupInsightGroupsParams(TypedDict, total=False):
    name: Required[str]

    description: str

    webhook: str
