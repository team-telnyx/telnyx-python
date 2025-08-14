# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta

__all__ = ["CsvDownloadListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["pending", "complete", "failed", "expired"]] = None
    """Indicates the completion level of the CSV report.

    Only complete CSV download requests will be able to be retrieved.
    """

    url: Optional[str] = None
    """The URL at which the CSV file can be retrieved."""


class CsvDownloadListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
