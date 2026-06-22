# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NodePositionParam"]


class NodePositionParam(TypedDict, total=False):
    """2D coordinates for a node, used by authoring UIs to lay out the graph.

    Purely a presentation aid. The runtime ignores `position`; it round-trips
    through the API so frontends can persist the graph layout customers
    arrange in the editor.
    """

    x: Required[float]
    """Horizontal coordinate in the authoring canvas."""

    y: Required[float]
    """Vertical coordinate in the authoring canvas."""
