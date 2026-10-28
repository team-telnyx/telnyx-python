# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["ScenarioGenerateBgParams"]


class ScenarioGenerateBgParams(TypedDict, total=False):
    num_scenarios: Required[int]
    """How many scenarios to generate."""

    agent_id: int

    extra_instructions: str
    """Optional guidance steering scenario generation."""

    first_message: str

    folder_path: Optional[str]

    generate_expected_outcomes: bool
    """Whether to generate expected-outcome prompts for the scenarios."""

    inbound_phone_number: Optional[int]

    personalities: Iterable[int]

    scenario_type: Literal["workflow", "red_teaming_voice", "red_teaming_text"]
    """Type of scenario to generate."""

    tags: SequenceNotStr[str]

    test_profile: int

    tool_ids: SequenceNotStr[str]
