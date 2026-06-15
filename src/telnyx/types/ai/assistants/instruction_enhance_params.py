# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InstructionEnhanceParams"]


class InstructionEnhanceParams(TypedDict, total=False):
    enhancement_prompt: Optional[str]
    """Optional guidance describing how the instructions should be enhanced.

    When provided, the LLM applies these requested changes in addition to fixing any
    identified issues.
    """

    instructions: Optional[str]
    """The instructions to enhance.

    When omitted, the assistant's existing instructions are used.
    """
