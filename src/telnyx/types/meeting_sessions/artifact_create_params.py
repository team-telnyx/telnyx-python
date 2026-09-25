# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ArtifactCreateParams", "NamedArtifact", "CustomArtifact"]


class NamedArtifact(TypedDict, total=False):
    type: Required[Literal["summary", "action_items", "decisions", "topics", "open_questions"]]
    """What to generate from the transcript.

    `custom` is answered from a `prompt` you supply; the five named types need none.
    """


class CustomArtifact(TypedDict, total=False):
    prompt: Required[str]
    """An open-ended request answered from the transcript.

    Required when `type` is `custom`, and rejected with 400 on any named type.
    Trimmed before storage and echoed back in artifact responses and the
    `artifact.completed` webhook.
    """

    type: Required[Literal["custom"]]
    """Answered from the `prompt` below rather than a fixed question."""


ArtifactCreateParams: TypeAlias = Union[NamedArtifact, CustomArtifact]
