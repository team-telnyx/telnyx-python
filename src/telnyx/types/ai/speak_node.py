# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .node_position import NodePosition

__all__ = ["SpeakNode"]


class SpeakNode(BaseModel):
    """A standalone scripted-message step in a flow, as returned by the API."""

    id: str
    """Caller-supplied unique identifier for this node within the flow."""

    message: str
    """Message delivered to the user verbatim when the flow reaches this node.

    No LLM turn — the text is spoken/sent exactly as written. `{{variable}}`
    placeholders are interpolated from the conversation's dynamic variables; an
    unresolved placeholder renders as an empty string. After delivering, the flow
    routes via the node's outgoing `llm` / `expression` edges (commonly a single
    unconditional edge).
    """

    name: Optional[str] = None
    """Optional human-readable label, displayed in authoring UIs."""

    position: Optional[NodePosition] = None
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    type: Optional[Literal["speak"]] = None
    """Node kind discriminator. Always `speak` for a speak node."""
