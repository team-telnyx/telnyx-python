# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["EmailTemplateRenderParams"]


class EmailTemplateRenderParams(TypedDict, total=False):
    template_variables: Dict[str, object]
    """Variables for Liquid template rendering.

    Non-object values are silently treated as an empty object.
    """
