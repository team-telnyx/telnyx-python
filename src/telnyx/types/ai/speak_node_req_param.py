# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .node_position_param import NodePositionParam

__all__ = ["SpeakNodeReqParam"]


class SpeakNodeReqParam(TypedDict, total=False):
    """A standalone scripted-message step in a flow, as supplied by clients.

    Unlike a prompt node, a speak node has no instructions or model — it isn't
    an LLM turn. Reaching it delivers `message` to the user verbatim (with
    `{{variable}}` interpolation), then routes via outgoing `llm` /
    `expression` edges.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this node within the flow."""

    message: Required[str]
    """Message delivered to the user verbatim when the flow reaches this node.

    No LLM turn — the text is spoken/sent exactly as written. `{{variable}}`
    placeholders are interpolated from the conversation's dynamic variables; an
    unresolved placeholder renders as an empty string. After delivering, the flow
    routes via the node's outgoing `llm` / `expression` edges (commonly a single
    unconditional edge).
    """

    name: str
    """Optional human-readable label, displayed in authoring UIs."""

    position: NodePositionParam
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    type: Literal["speak"]
    """Node kind discriminator. Always `speak` for a speak node."""
