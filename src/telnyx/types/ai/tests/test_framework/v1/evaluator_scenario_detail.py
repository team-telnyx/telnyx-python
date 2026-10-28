# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from ......_models import BaseModel

__all__ = ["EvaluatorScenarioDetail", "InboundPhoneNumberData", "OutboundPhoneNumberData", "TestProfileData"]


class InboundPhoneNumberData(BaseModel):
    id: Optional[int] = None

    number: Optional[str] = None

    phone_number_id: Optional[str] = None


class OutboundPhoneNumberData(BaseModel):
    id: Optional[int] = None

    number: Optional[str] = None

    phone_number_id: Optional[str] = None


class TestProfileData(BaseModel):
    __test__ = False
    id: Optional[int] = None

    agent: Optional[int] = None

    information: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    project: Optional[int] = None


class EvaluatorScenarioDetail(BaseModel):
    id: int

    agent: Optional[int] = None

    name: str

    dynamic_variable_values: Optional[Dict[str, str]] = None

    expected_outcome_prompt: Optional[str] = None

    first_message: Optional[str] = None

    folder_path: Optional[str] = None

    inbound_phone_number: Optional[int] = None

    inbound_phone_number_data: Optional[InboundPhoneNumberData] = None

    information_fields: Optional[Dict[str, str]] = None

    instructions: Optional[str] = None

    is_predefined: Optional[bool] = None

    max_duration: Optional[int] = None

    metric_names: Optional[List[str]] = None

    metrics: Optional[List[int]] = None

    outbound_phone_number_data: Optional[OutboundPhoneNumberData] = None

    personality: Optional[int] = None

    personality_name: Optional[str] = None

    phone_number: Optional[str] = None

    project: Optional[int] = None

    runs: Optional[List[int]] = None

    scenario_language: Optional[str] = None

    scenario_type: Optional[str] = None

    simulation_description: Optional[str] = None

    suite_type: Optional[str] = None

    tags: Optional[List[str]] = None

    test_profile: Optional[int] = None

    test_profile_data: Optional[TestProfileData] = None

    tool_ids: Optional[List[str]] = None
