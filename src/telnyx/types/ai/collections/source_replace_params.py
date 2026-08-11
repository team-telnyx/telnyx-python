# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .source_request_param import SourceRequestParam

__all__ = ["SourceReplaceParams"]


class SourceReplaceParams(TypedDict, total=False):
    sources: Required[Iterable[SourceRequestParam]]
