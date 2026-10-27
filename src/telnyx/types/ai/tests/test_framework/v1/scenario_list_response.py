# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime

from ......_models import BaseModel

__all__ = ["ScenarioListResponse", "Result", "ResultTestProfileData"]


class ResultTestProfileData(BaseModel):
    id: Optional[int] = None

    agent: Optional[int] = None

    information: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    project: Optional[int] = None


class Result(BaseModel):
    id: int

    agent: Optional[int] = None
    """ID of the test agent the scenario runs against."""

    created_at: datetime

    name: str

    updated_at: datetime

    dynamic_variable_values: Optional[Dict[str, str]] = None

    expected_outcome_prompt: Optional[str] = None
    """
    What a successful conversation looks like; scored by the expected-outcome
    metric.
    """

    first_message: Optional[str] = None
    """First message the simulated caller speaks or sends."""

    folder_path: Optional[str] = None

    inbound_phone_number: Optional[int] = None

    inbound_phone_number_data: Optional[str] = None

    instructions: Optional[str] = None
    """What the simulated caller should do during the conversation."""

    last_updated_by: Optional[int] = None

    metric_names: Optional[List[str]] = None

    metrics: Optional[List[int]] = None
    """Metric IDs applied to the scenario."""

    personality: Optional[int] = None
    """ID of the test personality the caller simulates."""

    personality_name: Optional[str] = None

    phone_number: Optional[str] = None
    """Outbound phone number used to place the simulated call."""

    scenario_language: Optional[str] = None

    scenario_type: Optional[str] = None
    """Type of scenario: workflow, red_teaming_voice, or red_teaming_text."""

    tags: Optional[List[str]] = None

    test_profile: Optional[int] = None

    test_profile_data: Optional[ResultTestProfileData] = None

    tool_ids: Optional[List[str]] = None


class ScenarioListResponse(BaseModel):
    count: int

    next: Optional[str] = None

    previous: Optional[str] = None

    results: List[Result]
