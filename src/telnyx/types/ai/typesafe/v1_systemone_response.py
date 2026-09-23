# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "V1SystemoneResponse",
    "Answers",
    "AnswersDecisionModelChoiceAnswer",
    "AnswersDecisionModelNoulAnswer",
    "AnswersDecisionModelScoreAnswer",
    "Usage",
]


class AnswersDecisionModelChoiceAnswer(BaseModel):
    """A selected option and the distribution across all supplied option keys."""

    choice: str
    """The option key with the highest relative score.

    Ties favor the first option in request order.
    """

    confidence: float
    """
    Normalized entropy confidence: 1 - H(p) / ln(N), where H(p) = -sum(p \\** ln(p))
    and N is the number of options. Zero indicates a uniform distribution; one
    indicates concentration on one option. This is neither the winning probability
    nor calibrated correctness.
    """

    probabilities: Dict[str, float]
    """
    Relative scores normalized across the supplied options, summing approximately
    to 1. These are not calibrated probabilities of correctness.
    """

    type: Literal["choice"]
    """Answer type."""


class AnswersDecisionModelNoulAnswer(BaseModel):
    """A yes/no score with no separate confidence or probabilities fields."""

    noul: float
    """Score of the positive outcome.

    Values near 1 favor yes; values near 0 favor no. This is a number, not a
    Boolean, and is not calibrated correctness.
    """

    type: Literal["noul"]
    """Answer type."""


class AnswersDecisionModelScoreAnswer(BaseModel):
    """An expected rating over the ordered criteria."""

    confidence: float
    """
    Normalized entropy confidence: 1 - H(p) / ln(N), where H(p) = -sum(p \\** ln(p))
    and N is the number of options. Zero indicates a uniform distribution; one
    indicates concentration on one option. This is neither the winning probability
    nor calibrated correctness.
    """

    legend: Dict[str, str]
    """
    Criterion descriptions keyed by stringified zero-based indices, such as "0",
    "1", and "2".
    """

    probabilities: Dict[str, float]
    """Relative scores keyed by the same stringified indices as legend."""

    score: float
    """Expected zero-based criterion index: sum(index \\** probability).

    Ranges from 0 to N-1 for N criteria; fractional values are valid.
    """

    type: Literal["score"]
    """Answer type."""


Answers: TypeAlias = Annotated[
    Union[AnswersDecisionModelChoiceAnswer, AnswersDecisionModelNoulAnswer, AnswersDecisionModelScoreAnswer],
    PropertyInfo(discriminator="type"),
]


class Usage(BaseModel):
    """Token usage for the completed evaluation."""

    input_tokens: int
    """
    Input tokens processed, including shared-context preparation and question
    evaluation. This can exceed the token count of the unique input text.
    """

    output_tokens: int
    """Output tokens used for the evaluation, including shared-context preparation."""


class V1SystemoneResponse(BaseModel):
    """A complete synchronous evaluation.

    Answers are returned directly without a data wrapper.
    """

    answers: Dict[str, Answers]
    """Answers keyed by exactly the question IDs in the request.

    Each answer type matches its question.
    """

    model: str
    """
    Opaque Telnyx-controlled identifier retained for TypeSafe SDK response
    compatibility. It is not a selectable model name or a guarantee of a particular
    underlying model.
    """

    usage: Usage
    """Token usage for the completed evaluation."""
