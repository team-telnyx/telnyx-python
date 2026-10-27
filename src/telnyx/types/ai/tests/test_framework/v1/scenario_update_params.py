# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from ......_types import SequenceNotStr

__all__ = ["ScenarioUpdateParams"]


class ScenarioUpdateParams(TypedDict, total=False):
    agent: Optional[int]

    expected_outcome_prompt: str

    first_message: str

    folder_path: Optional[str]

    inbound_phone_number: int

    instructions: str

    max_duration: Optional[int]

    metrics: Iterable[int]

    name: str

    personality: int

    phone_number: int

    scenario_language: str

    tags: SequenceNotStr[str]

    test_profile: int

    tool_ids: SequenceNotStr[str]
