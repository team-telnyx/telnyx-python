# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    category: Required[Literal["MARKETING", "UTILITY", "AUTHENTICATION"]]

    components: Required[Iterable[Dict[str, object]]]

    language: Required[str]

    name: Required[str]

    waba_id: Required[str]
