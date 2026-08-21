# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["PayPromptValueParam", "PayPromptList"]


class PayPromptList(TypedDict, total=False):
    """A text-to-speech prompt with optional matching qualifiers."""

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers for which this prompt applies."""

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
        "timeout",
        "invalid-card-number",
        "invalid-card-type",
        "invalid-date",
        "invalid-security-code",
        "invalid-postal-code",
        "invalid-bank-routing-number",
        "invalid-bank-account-number",
        "input-matching-failed",
    ]
    """Step error for which this prompt applies."""


PayPromptValueParam: TypeAlias = Union[str, Iterable[PayPromptList]]
