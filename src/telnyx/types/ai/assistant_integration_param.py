# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AssistantIntegrationParam"]


class AssistantIntegrationParam(TypedDict, total=False):
    """Reference to a connected integration attached to an assistant.

    Discover available integrations with `/ai/integrations` and connected integrations with `/ai/integrations/connections`.
    """

    integration_id: Required[str]
    """Catalog integration ID to attach.

    This is the `id` from the integrations catalog at `/ai/integrations` (the same
    value also appears as `integration_id` on entries returned by
    `/ai/integrations/connections`). It is **not** the connection-level `id` from
    `/ai/integrations/connections`.
    """

    allowed_list: SequenceNotStr[str]
    """Optional per-assistant allowlist of integration tool names.

    When omitted or empty, all tools allowed by the connected integration are
    available to the assistant.
    """
