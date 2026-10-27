# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["CreateAITestMetricRequestParam"]


class CreateAITestMetricRequestParam(TypedDict, total=False):
    name: Required[str]

    add_to_new_agents: Optional[bool]

    agents: Iterable[int]

    assistant_id: str

    audio_enabled: bool

    description: str

    display_order: int

    enum_values: SequenceNotStr[str]

    eval_type: str
    """
    What the metric scores: numeric, continuous_qualitative, or
    binary_workflow_adherence.
    """

    observability_enabled: bool

    prompt: str
    """Judge prompt used by llm_judge metrics."""

    sampling_enabled: bool

    simulation_enabled: bool

    type: str
    """How the metric is evaluated: custom_code or llm_judge."""
