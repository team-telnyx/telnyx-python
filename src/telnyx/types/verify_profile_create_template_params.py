# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerifyProfileCreateTemplateParams"]


class VerifyProfileCreateTemplateParams(TypedDict, total=False):
    text: Required[str]
    """The text content of the message template."""
