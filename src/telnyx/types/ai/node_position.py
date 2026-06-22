# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["NodePosition"]


class NodePosition(BaseModel):
    """2D coordinates for a node, used by authoring UIs to lay out the graph.

    Purely a presentation aid. The runtime ignores `position`; it round-trips
    through the API so frontends can persist the graph layout customers
    arrange in the editor.
    """

    x: float
    """Horizontal coordinate in the authoring canvas."""

    y: float
    """Vertical coordinate in the authoring canvas."""
