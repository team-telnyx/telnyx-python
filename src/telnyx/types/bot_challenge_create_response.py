# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BotChallengeCreateResponse", "Data"]


class Data(BaseModel):
    challenge_type: Literal["math", "string", "binary"]
    """Type of challenge."""

    nonce: str
    """Single-use challenge identifier.

    Submit it as `bot_challenge_nonce` on the signup request.
    """

    privacy_policy_url: str
    """Current privacy-policy URL. Echo this back on the signup request."""

    problem: str
    """Problem text to solve.

    Math problems are obfuscated and end with an unobfuscated rounding instruction;
    string and binary problems are returned as-is.
    """

    terms_and_conditions_url: str
    """Current terms-and-conditions URL. Echo this back on the signup request."""

    precision: Optional[int] = None
    """Decimal places expected in the answer. Present only for math challenges."""


class BotChallengeCreateResponse(BaseModel):
    data: Data
