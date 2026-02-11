# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["EmbeddingCreateEmbeddingsParams"]


class EmbeddingCreateEmbeddingsParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str]]]
    """Input text to embed. Can be a string or array of strings."""

    model: Required[str]
    """ID of the model to use.

    Use the List embedding models endpoint to see available models.
    """

    dimensions: int
    """The number of dimensions the resulting output embeddings should have.

    Only supported in some models.
    """

    encoding_format: Literal["float", "base64"]
    """The format to return the embeddings in."""

    user: str
    """
    A unique identifier representing your end-user for monitoring and abuse
    detection.
    """
