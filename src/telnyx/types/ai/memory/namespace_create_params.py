# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamespaceCreateParams"]


class NamespaceCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the new namespace, unique within your organization."""
