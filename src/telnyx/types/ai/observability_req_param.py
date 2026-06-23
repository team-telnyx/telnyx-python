# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .prompt_sync_status import PromptSyncStatus
from .observability_status import ObservabilityStatus

__all__ = ["ObservabilityReqParam"]


class ObservabilityReqParam(TypedDict, total=False):
    host: str

    prompt_label: str

    prompt_name: str

    prompt_sync: PromptSyncStatus
    """Whether to auto-publish the assistant's instructions as a Langfuse prompt.

    When ENABLED + prompt_name set, every assistant create/update pushes
    `instructions` to Langfuse via create_prompt and stores the returned version in
    prompt_version.
    """

    prompt_version: int

    public_key_ref: str

    secret_key_ref: str

    status: ObservabilityStatus
