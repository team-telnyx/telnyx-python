# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AgentGatewayPolicyStep"]


class AgentGatewayPolicyStep(BaseModel):
    """
    One pipeline step: a guardrail, and what happens when it passes, fails, or errors.
    """

    guardrail: str
    """A guardrail on the instance, by name."""

    message: Optional[str] = None
    """The response that replaces the model's when an outcome is `respond`.

    Required with `respond`.
    """

    on_error: Optional[Literal["next", "allow", "block", "respond"]] = None
    """What happens when the guardrail errors. Left out, the same as `on_fail`."""

    on_fail: Optional[Literal["next", "allow", "block", "respond"]] = None
    """What happens when the guardrail fails."""

    on_pass: Optional[Literal["next", "allow", "block", "respond"]] = None
    """What happens when the guardrail passes.

    `next` goes on to the next step, `allow` allows the request, `block` blocks it,
    and `respond` answers with `message`.
    """

    pass_data: Optional[bool] = None
    """
    `true` hands the step's modified request, such as masked text, to the next step.
    """
