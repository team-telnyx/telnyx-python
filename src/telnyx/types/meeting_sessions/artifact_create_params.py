# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ArtifactCreateParams"]


class ArtifactCreateParams(TypedDict, total=False):
    type: Required[Literal["summary", "action_items"]]
    """Type of artifact to generate from the session."""
