# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional

from ......_models import BaseModel

__all__ = ["AITestMetric"]


class AITestMetric(BaseModel):
    id: int

    eval_type: str
    """
    What the metric scores: numeric, continuous_qualitative, or
    binary_workflow_adherence.
    """

    name: str

    type: str
    """How the metric is evaluated: custom_code or llm_judge."""

    add_to_new_agents: Optional[bool] = None
    """Whether the metric is attached to newly created test agents by default."""

    agent: Optional[int] = None

    agent_names: Optional[List[str]] = None

    agents: Optional[List[int]] = None
    """Test agent IDs the metric is attached to."""

    alert_filters: Optional[Dict[str, object]] = None

    alert_type: Optional[str] = None

    audio_enabled: Optional[bool] = None

    configuration: Optional[Dict[str, object]] = None

    description: Optional[str] = None

    display_order: Optional[int] = None

    enum_values: Optional[List[str]] = None
    """Allowed values for qualitative enum metrics."""

    evaluation_trigger: Optional[str] = None

    evaluation_trigger_custom_code: Optional[str] = None

    evaluation_trigger_prompt: Optional[str] = None

    ewma_alpha: Optional[float] = None
    """Smoothing factor for the alert trend."""

    function_name: Optional[str] = None
    """Built-in evaluation function used by custom_code metrics."""

    kb_file_ids: Optional[List[int]] = None

    knowledge_base_files: Optional[List[str]] = None

    metric_cost: Optional[float] = None

    observability_enabled: Optional[bool] = None

    overall_score: Union[float, str, None] = None

    priority_assignment_prompt: Optional[str] = None

    project: Optional[int] = None

    prompt: Optional[str] = None
    """Judge prompt used by llm_judge metrics."""

    sample_rate: Optional[float] = None

    sampling_enabled: Optional[bool] = None

    significant_change_alert_direction: Optional[str] = None

    significant_change_alert_status: Optional[str] = None

    simulation_enabled: Optional[bool] = None

    slug: Optional[str] = None
    """Stable identifier of a built-in metric."""

    std_multiplier: Optional[float] = None
    """Standard-deviation multiplier for significant-change alerts."""

    total_score: Union[float, str, None] = None

    trigger_type: Optional[str] = None

    user_defined: Optional[bool] = None

    uses_llm_judge: Optional[bool] = None

    window_size: Optional[int] = None
    """Sliding window size the alert status is computed over."""
