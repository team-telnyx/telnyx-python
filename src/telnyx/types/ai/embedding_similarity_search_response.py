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
    distance: float

    document_chunk: str

    metadata: DataMetadata


class EmbeddingSimilaritySearchResponse(BaseModel):
    data: List[Data]
