# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .csv_download import CsvDownload
from ..pagination_meta import PaginationMeta

__all__ = ["CsvDownloadListResponse"]


class CsvDownloadListResponse(BaseModel):
    data: Optional[List[CsvDownload]] = None

    meta: Optional[PaginationMeta] = None
