# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["EmbeddingSimilaritySearchResponse", "Data", "DataMetadata"]


class DataMetadata(BaseModel):
    checksum: str

    embedding: str

    filename: str

    source: str

    certainty: Optional[float] = None

    loader_metadata: Optional[Dict[str, object]] = None


class Data(BaseModel):
    """
    Example document response from embedding service
    {
      "document_chunk": "your status? This is Vanessa Bloome...",
      "distance": 0.18607724,
      "metadata": {
        "source": "https://us-central-1.telnyxstorage.com/scripts/bee_movie_script.txt",
        "checksum": "343054dd19bab39bbf6761a3d20f1daa",
        "embedding": "openai/text-embedding-ada-002",
        "filename": "bee_movie_script.txt",
        "certainty": 0.9069613814353943,
        "loader_metadata": {}
      }
    }
    """

    distance: float

    document_chunk: str

    metadata: DataMetadata


class EmbeddingSimilaritySearchResponse(BaseModel):
    data: List[Data]
