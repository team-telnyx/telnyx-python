# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel

__all__ = ["Namespace"]


class Namespace(BaseModel):
    """An isolated memory store within your organization."""

    id: str
    """The namespace's unique identifier."""

    name: str
    """The namespace's name, used in the path.

    `default` exists for every organization.
    """
