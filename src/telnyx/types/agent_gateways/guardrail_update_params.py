# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GuardrailUpdateParams"]


class GuardrailUpdateParams(TypedDict, total=False):
    instance_id: Required[str]

    always_on: bool
    """`true` runs the guardrail on every request, and a request cannot turn it off.

    `false` runs it on the requests that name it.
    """

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
    """When the guardrail runs. Each type runs in some modes only."""

    name: str
    """A name, unique on the instance. A request names it in its `guardrails` field."""

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
    `endpoint`, `severity` (0 to 7). Provider secrets are write-only.
    """
