# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["WhatsappMessageTemplateUpdateParams"]


class WhatsappMessageTemplateUpdateParams(TypedDict, total=False):
    category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"]

    components: Iterable[object]
