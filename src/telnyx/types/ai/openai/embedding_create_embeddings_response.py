# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["EmbeddingCreateEmbeddingsResponse", "Data", "Usage"]


class Data(BaseModel):
    embedding: List[float]
    """The embedding vector"""

    index: int
    """The index of the embedding in the list of embeddings"""

    object: str
    """The object type, always 'embedding'"""


class Usage(BaseModel):
    prompt_tokens: int
    """Number of tokens in the input"""

    total_tokens: int
    """Total number of tokens used"""


class EmbeddingCreateEmbeddingsResponse(BaseModel):
    data: List[Data]
    """List of embedding objects"""

    model: str
    """The model used for embedding"""

    object: str
    """The object type, always 'list'"""

    usage: Usage
