# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentGatewayGuardrail"]


class AgentGatewayGuardrail(BaseModel):
    id: str
    """Identifies the guardrail."""

    always_on: bool
    """Whether it runs on every request."""

    created_at: Optional[datetime] = None

    modes: List[
        Literal[
            "before_request",
            "during_request",
            "after_request",
            "logging_only",
            "before_tool_request",
            "during_tool_request",
            "after_tool_request",
        ]
    ]
    """When the guardrail runs."""

    name: str
    """What a request names in its `guardrails` field."""

    settings: Dict[str, object]
    """The type's settings.

    `content_filter`: `patterns` (prebuilt patterns by name, such as `us_ssn` or
    `email`), `regexes`, `keywords`, and `categories` (such as `prompt_injection`),
    each with an `action` of `block` or `mask`. `tool_permission`: `rules` (`id`,
    `tool_name`, `tool_type`, `decision`, `argument_patterns`), a `default`
    decision, and `on_denied` (`block` or `rewrite`). `model_judge`: a `model` on
    the instance and weighted `criteria` (`name`, `description`, `weight`, the
    weights summing to 100). `custom_code`: `code` defining
    `apply_guardrail(inputs, request_data, input_type)`. `lakera`: `api_key`,
    `project_id`, `api_base`. `presidio`: `analyzer_url`, `anonymizer_url`,
    `entities` (entity name to `block` or `mask`), `language`. `bedrock`:
    `guardrail_id`, `version`, `region`, and `access_key_id` with
    `secret_access_key`, or `role_name`. `azure_content_safety`: `api_key`,
    `endpoint`, `severity` (0 to 7). Provider secrets are write-only. Responses
    leave the secrets out.
    """

    type: Literal[
        "content_filter",
        "tool_permission",
        "model_judge",
        "custom_code",
        "lakera",
        "presidio",
        "bedrock",
        "azure_content_safety",
    ]

    updated_at: Optional[datetime] = None
