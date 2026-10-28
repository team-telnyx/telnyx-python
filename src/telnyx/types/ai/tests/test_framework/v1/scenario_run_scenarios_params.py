# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, TypedDict

from ......_types import SequenceNotStr

__all__ = ["ScenarioRunScenariosParams"]


class ScenarioRunScenariosParams(TypedDict, total=False):
    agent_id: int

    agent_number: str

    assistant_id: str

    concurrency_limit: int
    """Maximum number of concurrent simulated calls."""

    frequency: int

    mode: Literal["same_number", "different_numbers"]

    name: str

    outbound_phone_number: str

    personality_ids: Iterable[int]

    scenarios: Union[Iterable[object], str]
    """Scenario IDs to run, or the literal string 'all'."""

    tags: SequenceNotStr[str]

    test_profile_ids: Iterable[int]
