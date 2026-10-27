# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["ScenarioCreateParams"]


class ScenarioCreateParams(TypedDict, total=False):
    name: Required[str]

    personality: Required[int]
    """ID of the personality the caller simulates."""

    agent: Optional[int]

    expected_outcome_prompt: str

    first_message: str

    folder_path: Optional[str]

    instructions: str

    metrics: Iterable[int]

    tags: SequenceNotStr[str]

    test_profile: int
