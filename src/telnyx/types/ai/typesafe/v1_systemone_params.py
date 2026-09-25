# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "V1SystemoneParams",
    "Questions",
    "QuestionsDecisionModelChoiceQuestion",
    "QuestionsDecisionModelNoulQuestion",
    "QuestionsDecisionModelNoulQuestionCriteria",
    "QuestionsDecisionModelScoreQuestion",
]


class V1SystemoneParams(TypedDict, total=False):
    questions: Required[Dict[str, Questions]]
    """Between 1 and 64 named questions. Each key identifies the corresponding answer."""

    state: Required[Union[str, Dict[str, object], Iterable[object]]]
    """Shared context evaluated by every question."""

    model: Literal["telnyx/decision-flash", "telnyx/decision-pro"]
    """Public model alias.

    telnyx/decision-flash offers the lowest cost and latency; telnyx/decision-pro
    supports decisions that require long context, including inputs beyond Jev’s 32k
    per-decision limit. Applies to every question in the request. Other values are
    rejected.
    """


class QuestionsDecisionModelChoiceQuestion(TypedDict, total=False):
    """Select one of the supplied options."""

    criteria: Required[Dict[str, Optional[str]]]
    """Between 2 and 64 option keys mapped to description strings or null.

    A null description uses the option key as its text.
    """

    instructions: Required[Union[str, Dict[str, object], Iterable[object]]]
    """Required instructions describing what to decide about the shared state."""

    type: Required[Literal["choice"]]
    """Question type."""


class QuestionsDecisionModelNoulQuestionCriteria(TypedDict, total=False):
    """Optional descriptions for the positive and negative outcomes.

    Descriptions must be strings.
    """

    false: str
    """Description of the negative outcome."""

    true: str
    """Description of the positive outcome."""


class QuestionsDecisionModelNoulQuestion(TypedDict, total=False):
    """Evaluate a yes/no question. Omit criteria to use Yes and No descriptions."""

    instructions: Required[Union[str, Dict[str, object], Iterable[object]]]
    """Required instructions describing what to decide about the shared state."""

    type: Required[Literal["noul"]]
    """Question type."""

    criteria: QuestionsDecisionModelNoulQuestionCriteria
    """Optional descriptions for the positive and negative outcomes.

    Descriptions must be strings.
    """


class QuestionsDecisionModelScoreQuestion(TypedDict, total=False):
    """Rate the state against an ordered rubric."""

    criteria: Required[SequenceNotStr[str]]
    """Between 2 and 64 description strings in ascending score order.

    Indices start at zero.
    """

    instructions: Required[Union[str, Dict[str, object], Iterable[object]]]
    """Required instructions describing what to decide about the shared state."""

    type: Required[Literal["score"]]
    """Question type."""


Questions: TypeAlias = Union[
    QuestionsDecisionModelChoiceQuestion, QuestionsDecisionModelNoulQuestion, QuestionsDecisionModelScoreQuestion
]
